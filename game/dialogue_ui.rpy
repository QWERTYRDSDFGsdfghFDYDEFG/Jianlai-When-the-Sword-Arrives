default dialogue_ui_theme = None
default dialogue_paralanguage = None
default dialogue_pair_left = None
default dialogue_pair_right = None


init -5 python:
    DIALOGUE_THEME_CONFIG = {
        "speaker": {
            "window_style": "say_window_speaker",
            "what_style": "say_dialogue",
            "what_color": "#f2eadf",
            "name_color": "#f4e7d4",
            "name_background": "#32271fe8",
            "window_background": "#15120fe9",
            "accent_color": "#9a654a",
            "accent_glow": "#c69a7040",
            "avatar_background": "#201a15f2",
            "seal_background": "#653a2fe8",
            "seal_color": "#f1dfca",
            "para_background": "#4d382be6",
            "para_color": "#ead8c3",
        },
        "protagonist": {
            "window_style": "say_window_protagonist",
            "what_style": "say_dialogue",
            "what_color": "#fff5e6",
            "name_color": "#f9e7c2",
            "name_background": "#352715ef",
            "window_background": "#121417ea",
            "accent_color": "#c9a061",
            "accent_glow": "#c9a06140",
            "avatar_background": "#20180ff2",
            "seal_background": "#4a3821ee",
            "seal_color": "#ffefcf",
            "para_background": "#47331ee6",
            "para_color": "#f6e0b6",
        },
        "narration": {
            "window_style": "say_window_narration",
            "what_style": "say_narration_text",
            "what_color": "#2a221b",
            "name_color": "#2a221b",
            "name_background": "#00000000",
            "window_background": "#e6d7c1e3",
            "accent_color": "#6f5b48",
            "accent_glow": "#6f5b4826",
            "avatar_background": "#00000000",
            "seal_background": "#00000000",
            "seal_color": "#2a221b",
            "para_background": "#cbb9a0e6",
            "para_color": "#44372a",
        },
        "thought": {
            "window_style": "say_window_thought",
            "what_style": "say_thought",
            "what_color": "#ece5de",
            "name_color": "#ece5de",
            "name_background": "#3a312be8",
            "window_background": "#25201ee8",
            "accent_color": "#9f8874",
            "accent_glow": "#9f887430",
            "avatar_background": "#00000000",
            "seal_background": "#57483de6",
            "seal_color": "#f4ece5",
            "para_background": "#4a3d34e6",
            "para_color": "#f2e6dd",
        },
        "protagonist_thought": {
            "window_style": "say_window_protagonist_thought",
            "what_style": "say_thought",
            "what_color": "#eef1f7",
            "name_color": "#eef1f7",
            "name_background": "#253042e8",
            "window_background": "#1d2530ea",
            "accent_color": "#91a3c1",
            "accent_glow": "#91a3c130",
            "avatar_background": "#00000000",
            "seal_background": "#304058e6",
            "seal_color": "#eff4fb",
            "para_background": "#394b66e6",
            "para_color": "#e2eaf7",
        },
    }

    # 只显示画风和裁切已经适配对话框的头像；没有合格素材时保持纯文字布局。
    DIALOGUE_AVATAR_IMAGES = {
        "李宝瓶": im.Scale(
            im.Crop("images/chapter1/c1_01_lbp_return_v2.png", 920, 100, 420, 420),
            150,
            150
        ),
        "李槐": im.Scale(
            im.Crop("images/chapter1/c1_03_lh_entry_v1.png", 620, 110, 420, 420),
            150,
            150
        ),
        "崔东山": im.Scale(
            im.Crop("lh/cds/cds-v1.png", 520, 110, 620, 620),
            150,
            150
        ),
        "裴钱": im.Scale(
            im.Crop("images/chapter1/c1_08_pq_pose_v1.png", 810, 60, 420, 420),
            150,
            150
        ),
    }

    # 独立对白头像：原图保持完整；显示裁切、适配与剧情选择分别管理。
    DIALOGUE_PORTRAIT_CONFIG = {
        "c2_08_pq_surprise": {
            "speaker": "裴钱",
            "path": "gui/dialogue/c2_08_pq_surprise_v1.png",
            "crop": (404, 0, 904, 941),
            "fit": "contain",
        },
        "c2_08_zl_tease": {
            "speaker": "朱敛",
            "path": "gui/dialogue/c2_08_zl_tease_v1.png",
            "crop": (302, 12, 1111, 929),
            "fit": "contain",
        },
    }

    DIALOGUE_PORTRAIT_LAYOUT = {
        "regular": {"content_size": (202, 210), "text_width": 1460},
        "small": {"content_size": (170, 178), "text_width": 1520},
    }

    def set_dialogue_theme(theme):
        def _dialogue_theme_callback(event, interact=True, **kwargs):
            if event == "begin":
                renpy.store.dialogue_ui_theme = theme
            elif event == "end":
                renpy.store.dialogue_ui_theme = None

        return _dialogue_theme_callback


    # 无配音段落可在台词前调用：$ set_dialogue_paralanguage("低声")
    def set_dialogue_paralanguage(text=None):
        renpy.store.dialogue_paralanguage = text


    # 台词后调用：$ clear_dialogue_paralanguage()
    def clear_dialogue_paralanguage():
        renpy.store.dialogue_paralanguage = None


    # 在明确标记的连续对话中启用双人头像槽。未调用时保持原有单人布局。
    def set_dialogue_pair(left=None, right=None):
        renpy.store.dialogue_pair_left = left
        renpy.store.dialogue_pair_right = right


    def clear_dialogue_pair():
        renpy.store.dialogue_pair_left = None
        renpy.store.dialogue_pair_right = None


    def resolve_dialogue_theme(who):
        current_theme = renpy.store.dialogue_ui_theme

        if current_theme:
            return current_theme

        if who is None:
            return "narration"

        if who == "陈平安":
            return "protagonist"

        return "speaker"


    def get_dialogue_ui(who, portrait=None):
        theme = resolve_dialogue_theme(who)
        ui = dict(DIALOGUE_THEME_CONFIG.get(theme, DIALOGUE_THEME_CONFIG["speaker"]))

        ui["theme"] = theme
        pair_left = renpy.store.dialogue_pair_left
        pair_right = renpy.store.dialogue_pair_right
        show_pair = (
            bool(who)
            and bool(pair_left)
            and bool(pair_right)
            and theme != "narration"
            and not renpy.variant("small")
            and portrait is None
        )

        ui["avatar"] = DIALOGUE_AVATAR_IMAGES.get(who)
        ui["show_pair"] = show_pair
        ui["show_avatar"] = bool(ui["avatar"]) and theme != "narration" and not show_pair and not renpy.variant("small")
        ui["show_name"] = bool(who) and theme not in ("thought", "protagonist_thought")
        ui["seal_text"] = who[:1] if who else ""
        ui["paralanguage"] = renpy.store.dialogue_paralanguage
        ui["portrait"] = portrait
        ui["avatar_frame_style"] = "say_avatar_frame"
        ui["avatar_yalign"] = 1.0
        ui["text_width"] = 1260

        if portrait is not None:
            spec = DIALOGUE_PORTRAIT_CONFIG.get(portrait)
            if spec is None:
                raise ValueError("Unknown dialogue portrait: {!r}".format(portrait))
            if spec["speaker"] != who:
                raise ValueError("Dialogue portrait {!r} does not belong to {!r}".format(portrait, who))

            layout = DIALOGUE_PORTRAIT_LAYOUT["small" if renpy.variant("small") else "regular"]
            # 先裁显示区域，再等比适配；不把横版透明留白或人物比例压进头像槽。
            ui["avatar"] = Transform(
                Transform(spec["path"], crop=spec["crop"]),
                xysize=layout["content_size"],
                fit=spec["fit"],
            )
            ui["show_avatar"] = True
            ui["show_pair"] = False
            ui["show_name"] = True
            ui["window_style"] = "say_window_portrait"
            ui["avatar_frame_style"] = "say_portrait_frame"
            ui["avatar_background"] = "#00000000"
            ui["avatar_yalign"] = 0.5
            ui["text_width"] = layout["text_width"]

        if show_pair:
            ui["pair_left"] = get_dialogue_pair_slot(pair_left, who, ui)
            ui["pair_right"] = get_dialogue_pair_slot(pair_right, who, ui)

        return ui


    def get_dialogue_pair_slot(name, who, ui):
        is_active = bool(who) and name in who

        return {
            "name": name,
            "avatar": DIALOGUE_AVATAR_IMAGES.get(name),
            "seal_text": name[:1],
            "active": is_active,
            "alpha": 1.0 if is_active else 0.58,
            "yoffset": 0 if is_active else 9,
            "background": ui["avatar_background"] if is_active else "#171411e0",
            "name_background": ui["accent_color"] if is_active else "#2a241fe0",
            "name_color": ui["name_color"] if is_active else "#b6aa9b",
        }
