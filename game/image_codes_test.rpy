# Run explicitly: SDK python.exe renpy.py <project> test image_codes
# A test-only early redirect is necessary: --savedir alone also merges game/saves.
# JIANLAI_IMAGE_CODE_QA_ROOT may also isolate lint or another named test suite.
python early:
    import os as _image_codes_qa_os
    import sys as _image_codes_qa_sys
    import time as _image_codes_qa_time

    _image_codes_qa_requested_root = _image_codes_qa_os.environ.get("JIANLAI_IMAGE_CODE_QA_ROOT")
    _image_codes_qa_isolated = (
        bool(_image_codes_qa_requested_root) and renpy.game.args.command in ("test", "lint")
    ) or (
        renpy.game.args.command == "test" and any(
            arg == "image_codes" or arg.startswith("image_codes.")
            for arg in _image_codes_qa_sys.argv
        )
    )
    _image_codes_qa_active = _image_codes_qa_isolated and renpy.game.args.command == "test"

    if _image_codes_qa_isolated:
        _image_codes_qa_root = _image_codes_qa_os.path.abspath(
            _image_codes_qa_requested_root or
            _image_codes_qa_os.path.join(renpy.config.basedir, "work", "image_codes", "qa")
        )
        _image_codes_qa_savedir = _image_codes_qa_os.path.join(
            _image_codes_qa_root, "saves", str(_image_codes_qa_time.time_ns())
        )
        _image_codes_qa_os.makedirs(_image_codes_qa_savedir, exist_ok=True)
        # Redirect the first persistent read, before savelocation.init runs.
        renpy.config.savedir = _image_codes_qa_savedir
        renpy.game.args.savedir = _image_codes_qa_savedir
        _image_codes_qa_original_location = renpy.savelocation.FileLocation

        class _ImageCodesQAFileLocation(_image_codes_qa_original_location):
            def __init__(self, directory):
                # MultiLocation deduplicates these identical locations. This also
                # isolates game/saves, extra_savedirs and persistent merge/write.
                super(_ImageCodesQAFileLocation, self).__init__(_image_codes_qa_savedir)

        renpy.savelocation.FileLocation = _ImageCodesQAFileLocation

init python:
    class ImageCodesQAChapterProbe:
        labels = set()

    def image_codes_qa_record_label(name, abnormal):
        ImageCodesQAChapterProbe.labels.add(name)

    def image_codes_qa_assert_isolated():
        assert _image_codes_qa_active, "Run test image_codes, or set JIANLAI_IMAGE_CODE_QA_ROOT for a test command."
        assert renpy.config.savedir == _image_codes_qa_savedir
        assert len(renpy.loadsave.location.locations) == 1
        assert renpy.loadsave.location.locations[0].directory == _image_codes_qa_savedir
        assert not renpy.list_slots(), "Image code QA must start with empty isolated saves."

    def image_codes_qa_rejects(code, error_type, reason):
        try:
            image_code(code)
        except error_type as error:
            assert code in str(error), "Rejected image code must appear in its error."
            assert reason in str(error), "Rejected image code must explain why: " + str(error)
        else:
            raise AssertionError("Image code unexpectedly accepted: " + code)


# This fixture has no jump/call from the game. Its second tag is a test marker,
# not a new character or a claim that a second portrait asset already exists.
transform image_codes_qa_pose_left:
    xalign 0.15
    yalign 0.0
    zoom 0.50

transform image_codes_qa_pose_center:
    xalign 0.5
    yalign 0.0
    zoom 0.50

transform image_codes_qa_pose_right:
    xalign 0.80
    yalign 0.0
    zoom 0.50

transform image_codes_qa_marker:
    xalign 0.92
    yalign 0.20

label image_codes_qa_scene:
    scene bg c1_02_midnight_lake_v1
    "图片代号验收：原有背景。"

    scene expression image_code("CG01·01·01")
    show expression image_code("立绘04·01·01·00") at image_codes_qa_pose_left
    show expression Solid("#9f8f70", xysize=(80, 180)) as image_codes_qa_partner at image_codes_qa_marker
    "图片代号验收甲：代号场景与两个独立标签。"

    show cds standard at image_codes_qa_pose_center
    "图片代号验收乙：旧名替换同一个角色。"

    show cds o01_p01_e00 at image_codes_qa_pose_right
    "图片代号验收乙二：新别名替换原有旧名。"

    scene bg c1_02_midnight_lake_v1
    show cds o01_p01_e00 at right_medium
    "图片代号验收丙：旧背景与新的立绘别名。"

    hide cds
    "图片代号验收丁：角色已经退场。"

    scene bg cg01_01_02
    "图片代号验收戊：原生场景别名。"
    return


testsuite global:
    teardown:
        exit


testsuite image_codes:
    # Literal is parsed before python early. An explicit test image_codes command
    # enables this suite through Ren'Py's selection logic.
    enabled False

    setup:
        $ image_codes_qa_assert_isolated()
        $ _test.timeout = 30
        $ _test.maximum_framerate = False
        $ _test.transition_timeout = 0.05
        $ _test.screenshot_directory = _image_codes_qa_os.path.join(_image_codes_qa_root, "screenshots")

    testcase aliases_and_save_restore:
        assert eval image_code("CG01·01·01") == "bg cg01_01_01"
        assert eval image_code("立绘04·01·01·00") == "cds o01_p01_e00"
        assert eval image_code("  立绘04·01·01·00  ") == "cds o01_p01_e00"
        run Start("image_codes_qa_scene")
        assert "图片代号验收：原有背景。"
        assert eval renpy.get_attributes("bg") == ("c1_02_midnight_lake_v1",)

        advance until "图片代号验收甲："
        assert eval set(renpy.get_showing_tags()) == {"bg", "cds", "image_codes_qa_partner"}
        assert eval renpy.get_attributes("bg") == ("cg01_01_01",)
        assert eval renpy.get_attributes("cds") == ("o01_p01_e00",)
        $ renpy.save("image-codes-qa-a")
        pause 0.5
        screenshot "aliases_two_tags"

        advance until "图片代号验收乙："
        assert eval set(renpy.get_showing_tags()) == {"bg", "cds", "image_codes_qa_partner"}
        assert eval renpy.get_attributes("cds") == ("standard",)
        $ renpy.save("image-codes-qa-b")

        advance until "图片代号验收乙二："
        assert eval set(renpy.get_showing_tags()) == {"bg", "cds", "image_codes_qa_partner"}
        assert eval renpy.get_attributes("cds") == ("o01_p01_e00",)

        advance until "图片代号验收丙："
        assert eval set(renpy.get_showing_tags()) == {"bg", "cds"}
        assert eval renpy.get_attributes("bg") == ("c1_02_midnight_lake_v1",)
        assert eval renpy.get_attributes("cds") == ("o01_p01_e00",)
        $ renpy.save("image-codes-qa-c")

        $ renpy.load("image-codes-qa-a")
        assert "图片代号验收甲："
        assert eval set(renpy.get_showing_tags()) == {"bg", "cds", "image_codes_qa_partner"}
        assert eval renpy.get_attributes("bg") == ("cg01_01_01",)
        assert eval renpy.get_attributes("cds") == ("o01_p01_e00",)
        pause 0.5
        screenshot "loaded_aliases"

        $ renpy.load("image-codes-qa-b")
        assert "图片代号验收乙："
        assert eval set(renpy.get_showing_tags()) == {"bg", "cds", "image_codes_qa_partner"}
        assert eval renpy.get_attributes("cds") == ("standard",)

        $ renpy.load("image-codes-qa-c")
        assert "图片代号验收丙："
        assert eval set(renpy.get_showing_tags()) == {"bg", "cds"}
        assert eval renpy.get_attributes("bg") == ("c1_02_midnight_lake_v1",)
        assert eval renpy.get_attributes("cds") == ("o01_p01_e00",)
        pause 0.5
        screenshot "loaded_legacy_background"

        run ShowMenu("history")
        assert screen "history"
        assert "图片代号验收甲："
        click "返回"
        assert screen "say"
        $ preferences.skip_unseen = True
        skip until "图片代号验收丁："
        assert eval set(renpy.get_showing_tags()) == {"bg"}
        advance until "图片代号验收戊："
        assert eval set(renpy.get_showing_tags()) == {"bg"}
        assert eval renpy.get_attributes("bg") == ("cg01_01_02",)
        advance until screen "main_menu"

    testcase unavailable_codes_fail_explicitly:
        $ image_codes_qa_rejects("立绘99·99·99·99", KeyError, "未登记")
        $ image_codes_qa_rejects("参考01·01", ValueError, "仅参考")
        $ image_codes_qa_rejects("立绘01·01·01·01", ValueError, "待制作")

    testcase main_menu_and_new_game:
        assert screen "main_menu"
        click id "story_preferences"
        assert screen "preferences"
        click "返回"
        click id "story_load"
        assert screen "load"
        click "返回"
        click "退出"
        assert screen "confirm"
        click "取消"
        click id "story_new_game"
        assert screen "say" timeout 30
        assert "李宝瓶快步穿过深夜庭院"
        pause 0.5
        screenshot "unchanged_new_game"
        keysym "K_ESCAPE"
        assert screen "save"
        keysym "K_ESCAPE"
        assert screen "say"
        run MainMenu(confirm=False)
        assert screen "main_menu"

    testcase existing_chapter_chain:
        $ ImageCodesQAChapterProbe.labels.clear()
        $ config.label_callbacks.append(image_codes_qa_record_label)
        click id "story_new_game"
        assert screen "say" timeout 30
        $ preferences.skip_unseen = True
        skip fast until screen "main_menu" timeout 300
        assert eval all("chapter%d_start" % n in ImageCodesQAChapterProbe.labels for n in range(2, 13))
        $ config.label_callbacks.remove(image_codes_qa_record_label)
        assert screen "main_menu"
