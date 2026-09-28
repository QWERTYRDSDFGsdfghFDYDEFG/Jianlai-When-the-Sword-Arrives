# Player-facing artwork collection. Only explicitly approved artwork belongs
# here; this is independent of the title screen's highest available stage.
define story_art_gallery_entries = (
    {
        "id": "prologue_memory",
        "title": _("书院送别"),
        "path": "gui/title_progress/prologue_memory.png",
        "unlock_field": "story_title_unlocks",
        "unlock_event": "academy_farewell",
        "locked_hint": _("完成序章后解锁"),
    },
)

init python:
    import builtins as story_art_builtins

    def story_art_entry(art_id):
        return next((entry for entry in story_art_gallery_entries
                     if entry["id"] == art_id), None)

    def story_art_unlocked(entry):
        if entry is None:
            return False
        # Read the exact persistent milestone. Do not infer completion from
        # current chapter, image visibility, gallery visits or title stage.
        events = getattr(persistent, entry["unlock_field"], None)
        collection_types = (story_art_builtins.set, story_art_builtins.frozenset,
                            story_art_builtins.list, story_art_builtins.tuple)
        return (isinstance(events, collection_types)
                and entry["unlock_event"] in events)

    def story_art_available(entry):
        return story_art_unlocked(entry) and renpy.loadable(entry["path"])

    def story_art_viewable_ids():
        return [entry["id"] for entry in story_art_gallery_entries
                if story_art_available(entry)]

    def story_art_neighbor(art_id, direction):
        available = story_art_viewable_ids()
        if len(available) < 2 or art_id not in available:
            return None
        return available[(available.index(art_id) + direction) % len(available)]

    def story_art_page_count():
        return max(1, (len(story_art_gallery_entries) + 5) // 6)


screen art_gallery():
    tag menu

    default page = 0
    $ gallery_total = len(story_art_gallery_entries)
    $ gallery_unlocked = sum(1 for entry in story_art_gallery_entries if story_art_unlocked(entry))
    $ gallery_pages = story_art_page_count()
    $ gallery_page = max(0, min(page, gallery_pages - 1))
    $ gallery_page_number = gallery_page + 1
    $ gallery_slice = story_art_gallery_entries[gallery_page * 6:(gallery_page + 1) * 6]

    use game_menu(_("画像鉴赏")):
        fixed:
            xsize 1380
            ysize 790

            text _("已解锁 [gallery_unlocked] / [gallery_total]"):
                style "art_gallery_heading"

            if not gallery_total:
                text _("画卷尚待收录。"):
                    style "art_gallery_note"
                    ypos 70
            else:
                if not gallery_unlocked:
                    text _("随着故事前行，画卷会在这里留存。"):
                        style "art_gallery_note"
                        ypos 43

                grid 3 2:
                    ypos 94
                    spacing 24

                    for entry in gallery_slice:
                        $ gallery_is_unlocked = story_art_unlocked(entry)
                        $ gallery_can_view = story_art_available(entry)
                        button:
                            id ("art_card_" + entry["id"])
                            style "art_gallery_card"
                            sensitive gallery_can_view
                            action Show("art_gallery_viewer", art_id=entry["id"])

                            vbox:
                                spacing 10
                                fixed:
                                    xysize (396, 222)
                                    add Solid("#171919")
                                    if gallery_can_view:
                                        add Transform(entry["path"], xysize=(396, 222), fit="contain"):
                                            align (0.5, 0.5)
                                    else:
                                        text (_("画像暂不可用") if gallery_is_unlocked else _("未解锁")):
                                            style "art_gallery_placeholder"
                                            align (0.5, 0.5)

                                text (_(entry["title"]) if gallery_is_unlocked else _(entry["locked_hint"])):
                                    style "art_gallery_caption"

                    for unused in range(6 - len(gallery_slice)):
                        null width 420 height 296

                if gallery_pages > 1:
                    hbox:
                        ypos 742
                        xalign 0.5
                        spacing 30
                        textbutton _("上一页"):
                            id "art_prev_page"
                            style "art_gallery_control"
                            sensitive gallery_page > 0
                            action SetScreenVariable("page", gallery_page - 1)
                        text _("[gallery_page_number] / [gallery_pages]"):
                            style "art_gallery_note"
                            yalign 0.5
                        textbutton _("下一页"):
                            id "art_next_page"
                            style "art_gallery_control"
                            sensitive gallery_page < gallery_pages - 1
                            action SetScreenVariable("page", gallery_page + 1)


screen art_gallery_viewer(art_id):
    modal True
    zorder 200

    default current_art_id = art_id
    $ gallery_entry = story_art_entry(current_art_id)
    $ gallery_can_view = story_art_available(gallery_entry)
    $ gallery_previous = story_art_neighbor(current_art_id, -1) if gallery_can_view else None
    $ gallery_next = story_art_neighbor(current_art_id, 1) if gallery_can_view else None

    add Solid("#0d0f10")

    if gallery_can_view:
        add Transform(gallery_entry["path"], xysize=(config.screen_width, config.screen_height - 110), fit="contain"):
            xalign 0.5
            ypos 0
    else:
        text _("暂无可查看的画像。"):
            style "art_gallery_placeholder"
            align (0.5, 0.45)

    # Controls occupy their own strip so none of the original artwork is hidden.
    frame:
        background Solid("#15191c")
        xfill True
        ysize 110
        yalign 1.0
        padding (36, 20)

        if gallery_can_view:
            text _(gallery_entry["title"]):
                style "art_gallery_heading"
                yalign 0.5

        hbox:
            align (1.0, 0.5)
            spacing 30
            if gallery_previous is not None:
                textbutton _("上一幅"):
                    id "art_view_previous"
                    style "art_gallery_control"
                    action SetScreenVariable("current_art_id", gallery_previous)
                textbutton _("下一幅"):
                    id "art_view_next"
                    style "art_gallery_control"
                    action SetScreenVariable("current_art_id", gallery_next)
            textbutton _("返回图册"):
                id "art_view_close"
                style "art_gallery_control"
                action Hide("art_gallery_viewer")

    key "game_menu" action Hide("art_gallery_viewer")
    if gallery_previous is not None:
        key "K_LEFT" action SetScreenVariable("current_art_id", gallery_previous)
        key "K_RIGHT" action SetScreenVariable("current_art_id", gallery_next)


style art_gallery_heading is gui_text:
    size 30
    color "#e2d8c4"

style art_gallery_note is gui_text:
    size 24
    color "#bcb3a2"

style art_gallery_card is empty:
    xysize (420, 296)
    padding (12, 12)
    background Solid("#b9a68120")
    hover_background Solid("#c9a06155")
    insensitive_background Solid("#b9a68112")

style art_gallery_caption is gui_text:
    size 26
    color "#e2d8c4"
    xmaximum 396

style art_gallery_placeholder is gui_text:
    size 28
    color "#bcb3a2"

style art_gallery_control is empty:
    padding (16, 9)
    hover_background Solid("#c9a06130")

style art_gallery_control_text is gui_text:
    size 28
    color "#d8cbb3"
    hover_color "#f0d4a8"
    insensitive_color "#686862"
