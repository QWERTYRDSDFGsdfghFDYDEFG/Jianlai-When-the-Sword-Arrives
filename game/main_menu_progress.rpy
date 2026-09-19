# The title follows the last successfully saved or loaded story, including after
# a restart. Keep this separate from global read/unlock history.
default story_chapter = 0
default story_prologue_phase = 0
default story_complete = False
default persistent.story_title_selection = None

# Enable only when a real final ending calls story_mark_complete(). Chapter 12
# currently ends the prototype; reaching its return is not full-game completion.
define story_title_completion_enabled = False
define story_title_available_stage = 2

init -5 python:
    import re as story_re
    import threading as story_threading
    import time as story_time
    import uuid as story_uuid

    story_autosave_context = story_threading.local()
    story_previous_autosave_prefix = config.autosave_prefix_callback
    story_prologue_markers = {
        "start": 0,
        "prologue_lakeside_gathering": 1,
        "prologue_academy_farewell": 2,
    }
    story_prologue_scene_ids = ("night_lake", "lakeside_gathering", "academy_farewell")
    story_prologue_phase_names = (_("夜湖"), _("湖畔相聚"), _("书院送别"))

    def story_prologue_locations():
        # Derive positions from stable scene/label names in the CURRENT script,
        # never from hardcoded line numbers or permanent read-history flags.
        positions = []
        try:
            with renpy.file("script.rpy") as script_file:
                source = script_file.read().decode("utf-8-sig")
        except (IOError, OSError, UnicodeError):
            return positions
        for number, line in enumerate(source.splitlines(), 1):
            label = story_re.match(r"\s*label\s+([A-Za-z0-9_]+)\s*:", line)
            if label and label.group(1) in story_prologue_markers:
                positions.append((number, story_prologue_markers[label.group(1)]))
            elif story_re.match(r"\s*scene\s+bg\s+c1_03_lh_entry_v1(?:\s|$)", line):
                positions.append((number, 1))
            elif story_re.match(r"\s*scene\s+bg\s+c1_13_academy_gate_farewell_v1(?:\s|$)", line):
                positions.append((number, 2))
        return positions

    story_prologue_positions = story_prologue_locations()

    def story_valid_phase(value):
        return type(value) is int and 0 <= value <= 2

    def story_phase_from_location(filename, line):
        if story_chapter_from_filename(filename) != 1:
            return None
        for threshold, phase in reversed(story_prologue_positions):
            if line >= threshold:
                return phase
        return None

    def story_phase_from_background():
        # The existing prologue's scene identifiers are stable even in a build
        # containing only compiled scripts, where source positions are absent.
        for attribute in renpy.get_attributes("bg") or ():
            match = story_re.match(r"c1_(\d+)_", attribute)
            if match:
                scene = int(match.group(1))
                return 2 if scene >= 13 else 1 if scene >= 3 else 0
        return None

    def story_state_change_begin():
        renpy.session["story_state_serial"] = renpy.session.get("story_state_serial", 0) + 1

    def story_state_change_end():
        serial = renpy.session.get("story_state_serial", 0)
        if serial % 2:
            renpy.session["story_state_serial"] = serial + 1

    def story_autosave_prefix():
        # This official callback runs before the background save freezes the
        # store. A thread-local marker avoids mixing manual/background saves.
        story_autosave_context.attempt = (
            renpy.session.get("story_state_serial", 0), story_time.time(),
            (story_chapter, story_prologue_phase, bool(story_complete and story_title_completion_enabled)))
        return story_previous_autosave_prefix() if story_previous_autosave_prefix else "auto-"

    def story_stage_for(chapter, complete=False, phase=None):
        # Only the completed prologue has title artwork. Draft later chapters
        # keep its final scene, never imply whole-game completion.
        if chapter is None:
            return 0
        if chapter >= 2:
            return 2
        return phase if story_valid_phase(phase) else 0

    def story_valid_chapter(value):
        return type(value) is int and 1 <= value <= 12

    def story_chapter_from_filename(filename):
        filename = filename.replace("\\", "/").rsplit("/", 1)[-1]
        if filename == "script.rpy":
            return 1
        if filename.startswith("script_chapter") and filename.endswith(".rpy"):
            number = filename[len("script_chapter"):-4]
            if number.isdigit() and 2 <= int(number) <= 12:
                return int(number)
        return None

    def story_label_progress(label, abnormal):
        if label in story_prologue_markers:
            story_state_change_begin()
            store.story_chapter = 1
            store.story_prologue_phase = story_prologue_markers[label]
            if label == "start":
                store.story_complete = False
            story_state_change_end()
        elif label.startswith("chapter") and label.endswith("_start"):
            number = label[len("chapter"):-len("_start")]
            if number.isdigit() and 2 <= int(number) <= 12:
                story_state_change_begin()
                store.story_chapter = int(number)
                store.story_prologue_phase = 2
                story_state_change_end()

    def story_save_metadata(metadata):
        # Official save_json_callbacks run during saving (also in the autosave
        # thread): only fill the supplied JSON; never update persistent here.
        attempt = getattr(story_autosave_context, "attempt", None)
        if attempt is not None:
            del story_autosave_context.attempt
        serial_before = renpy.session.get("story_state_serial", 0)
        chapter = story_chapter
        phase = story_prologue_phase
        complete = bool(story_complete and story_title_completion_enabled)
        serial_after = renpy.session.get("story_state_serial", 0)
        if attempt is not None:
            metadata["story_autosave_started"] = attempt[1]
            if (attempt[0] % 2 or attempt[0] != serial_before or serial_before != serial_after
                    or attempt[2] != (chapter, phase, complete)):
                # A chapter change/load overlapped the SDK's freeze-to-JSON
                # window. Do not attribute its snapshot to the wrong chapter.
                chapter, phase, complete = 0, None, False
        metadata["story_progress_version"] = 2
        metadata["story_save_id"] = story_uuid.uuid4().hex
        metadata["story_chapter"] = chapter
        metadata["story_prologue_phase"] = phase
        metadata["story_scene"] = story_prologue_scene_ids[phase] if story_valid_phase(phase) else None
        metadata["story_complete"] = complete

    def story_save_record(slot):
        # Ignore developer/test/checkpoint/internal slots and exception saves.
        # These are the numeric player pages plus Ren'Py's auto/quick pages.
        if not isinstance(slot, str) or not story_re.fullmatch(r"(?:\d+(?:-\d+)?|auto-\d+|quick-\d+)", slot):
            return None
        try:
            metadata = renpy.slot_json(slot)
            modified = renpy.slot_mtime(slot)
        except Exception:
            return None
        if not isinstance(metadata, dict) or modified is None or "_traceback" in metadata:
            return None
        save_id = metadata.get("story_save_id")
        if isinstance(save_id, str) and save_id:
            fingerprint = "id:" + save_id
        else:
            # Old saves have no project chapter metadata. This identity follows
            # an unchanged file when its auto/quick slot number rotates.
            fingerprint = "legacy:{!r}:{!r}".format(metadata.get("_ctime"), modified)
        chapter = metadata.get("story_chapter")
        version = metadata.get("story_progress_version")
        if version not in (1, 2) or not story_valid_chapter(chapter):
            chapter = None
        phase = metadata.get("story_prologue_phase")
        if version != 2 or not story_valid_phase(phase) or chapter is None:
            phase = 2 if chapter is not None and chapter >= 2 else None
        created = metadata.get("_ctime")
        if not isinstance(created, (int, float)):
            created = modified
        started = metadata.get("story_autosave_started", created)
        if not isinstance(started, (int, float)):
            started = created
        return {
            "slot": slot,
            "fingerprint": fingerprint,
            "chapter": chapter,
            "phase": phase,
            "complete": bool(chapter is not None and metadata.get("story_complete") is True),
            "modified": modified,
            "created": created,
            "started": started,
        }

    def story_save_records():
        records = []
        for slot in renpy.list_slots(r"[^_]"):
            record = story_save_record(slot)
            if record is not None:
                records.append(record)
        return records

    def story_selected_save():
        records = story_save_records()
        if not records:
            return None
        selected = persistent.story_title_selection
        if isinstance(selected, dict):
            matches = [record for record in records
                       if record["fingerprint"] == selected.get("fingerprint")]
            if matches:
                record = next((record for record in matches
                               if record["slot"] == selected.get("slot")), matches[0])
                if (record["chapter"] is None or selected.get("verified")) and story_valid_chapter(selected.get("chapter")):
                    record = dict(record, chapter=selected["chapter"], complete=bool(selected.get("complete")))
                if (record["phase"] is None or selected.get("verified")) and story_valid_phase(selected.get("phase")):
                    record = dict(record, phase=selected["phase"])
                return record
        # Deleted/overwritten selections fall back to the newest extant save.
        # The same resolver drives the title AND the continue button.
        return max(records, key=lambda record: (record["modified"], record["slot"]))

    def story_selected_slot():
        record = story_selected_save()
        return record["slot"] if record else None

    def story_title_chapter():
        record = story_selected_save()
        return record["chapter"] if record else None

    def story_title_raw_stage():
        record = story_selected_save()
        return story_stage_for(record["chapter"], record["complete"], record["phase"]) if record else 0

    def story_title_phase_label(phase=None):
        if phase is None:
            phase = story_title_stage()
        return story_prologue_phase_names[phase] if story_valid_phase(phase) else ""

    def story_title_stage():
        # Only the three prologue scenes are ready.
        return min(story_title_raw_stage(), story_title_available_stage)

    def story_remember(record, source, event_time=None):
        if record is None:
            return
        selected = dict(record)
        selected["source"] = source
        selected["event_time"] = story_time.time() if event_time is None else event_time
        persistent.story_title_selection = selected
        renpy.save_persistent()

    def story_record_saved(slot):
        story_remember(story_save_record(slot), "save")

    def story_autosave_finished():
        # Ren'Py delivers autosave_callback on the main thread, possibly after
        # the player has loaded another save. Ignore an older delayed event.
        slot = renpy.newest_slot(r"auto-")
        record = story_save_record(slot) if slot else None
        if record is None:
            return
        selected = persistent.story_title_selection
        if isinstance(selected, dict) and record["started"] <= selected.get("event_time", 0):
            return
        story_remember(record, "autosave", record["created"])

    def story_after_load():
        story_state_change_end()
        pending = renpy.session.pop("story_pending_load", None)
        if pending is None:
            return
        record = story_save_record(pending["slot"])
        if record is None or record["fingerprint"] != pending["fingerprint"]:
            return
        story_remember(record, "load")
        # Verify every load against the actual resumed story, including older
        # builds whose metadata could have been captured during a save race.
        renpy.session["story_loaded_record"] = record["fingerprint"]

    def story_statement_progress(statement):
        if main_menu or renpy.context_nesting_level() != 0:
            return
        filename, line = renpy.get_filename_line()
        chapter = story_chapter_from_filename(filename)
        if chapter is None:
            return
        phase = 2 if chapter >= 2 else story_phase_from_location(filename, line)
        selected = persistent.story_title_selection
        if phase is None and renpy.session.get("story_loaded_record"):
            if not isinstance(selected, dict) or selected.get("phase") is None:
                phase = story_phase_from_background()
        if phase is None:
            phase = store.story_prologue_phase if story_valid_phase(store.story_prologue_phase) else 0
        # Repairs old saves and follows rollback across prologue milestones.
        if store.story_chapter != chapter or store.story_prologue_phase != phase:
            story_state_change_begin()
            store.story_chapter = chapter
            store.story_prologue_phase = phase
            story_state_change_end()
        fingerprint = renpy.session.pop("story_loaded_record", None)
        if fingerprint and isinstance(selected, dict) and selected.get("fingerprint") == fingerprint:
            record = dict(selected, chapter=chapter, phase=phase,
                          complete=bool(store.story_complete and story_title_completion_enabled), verified=True)
            story_remember(record, "load", selected["event_time"])

    def story_mark_complete():
        """Reserved for the future final ending; inactive in this prototype."""
        if not story_title_completion_enabled:
            return False
        story_state_change_begin()
        store.story_complete = True
        story_state_change_end()
        renpy.force_autosave(block=True)
        story_autosave_finished()
        return True

    def story_slot_name(name, page=None):
        # Match FileSave/FileLoad naming, including documented folder, linear
        # saves, and file_slotname_callback settings; no engine monkey-patch.
        page = FileCurrentPage() if page is None else str(page)
        try:
            page = int(page) + persistent._file_folder * config.file_pages_per_folder
        except ValueError:
            pass
        if config.linear_saves_page_size is not None:
            try:
                return str((int(page) - 1) * config.linear_saves_page_size + int(name))
            except ValueError:
                pass
        page, name = str(page), str(name)
        if config.file_slotname_callback is not None:
            return config.file_slotname_callback(page, name)
        return page + "-" + name

    class StoryLoad(Action):
        def __init__(self, slot, confirm=True):
            self.slot = slot
            self.confirm = confirm

        def get_sensitive(self):
            return not _in_replay and self.slot is not None and story_save_record(self.slot) is not None

        def get_selected(self):
            return self.slot is not None and self.slot == story_selected_slot()

        def __call__(self):
            if not self.get_sensitive():
                return
            if self.confirm and not main_menu:
                return renpy.run(Confirm(_("读取存档将丢失尚未保存的进度。继续吗？"), StoryLoad(self.slot, False), confirm_selected=True))
            record = story_save_record(self.slot)
            if record is None:
                return
            renpy.session.pop("story_loaded_record", None)
            renpy.session["story_pending_load"] = record
            story_state_change_begin()
            try:
                renpy.load(self.slot)
            except Exception:
                story_state_change_end()
                renpy.session.pop("story_pending_load", None)
                raise
            # A rejected save signature can make load return without loading.
            renpy.session.pop("story_pending_load", None)
            story_state_change_end()

    class StoryContinue(Action):
        def get_sensitive(self):
            return not _in_replay and story_selected_slot() is not None

        def __call__(self):
            if self.get_sensitive():
                return renpy.run(StoryLoad(story_selected_slot()))

    def StoryFileAction(name, page=None):
        slot = story_slot_name(name, page)
        if renpy.current_screen().screen_name[0] == "load":
            return StoryLoad(slot)
        return FileSave(name, page=page, action=Function(story_record_saved, slot))

    def StoryQuickSave():
        after_save = [Function(story_record_saved, story_slot_name(1, "quick")),
                      Notify(_("快速保存完成。"))]
        actions = [FileSave(1, page="quick", confirm=False, cycle=True, action=after_save)]
        if not getattr(renpy.context(), "_menu", False):
            actions.insert(0, FileTakeScreenshot())
        return actions

    def StoryQuickLoad():
        return StoryLoad(story_slot_name(1, "quick"))

    config.label_callbacks.append(story_label_progress)
    config.statement_callbacks.append(story_statement_progress)
    config.save_json_callbacks.append(story_save_metadata)
    config.autosave_prefix_callback = story_autosave_prefix
    config.after_load_callbacks.append(story_after_load)
    if config.autosave_callback is None:
        config.autosave_callback = story_autosave_finished
    else:
        config.autosave_callback = [config.autosave_callback, story_autosave_finished]
