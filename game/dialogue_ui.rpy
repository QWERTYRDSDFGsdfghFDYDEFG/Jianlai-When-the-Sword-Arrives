default dialogue_ui_theme = None
default dialogue_paralanguage = None


init -5 python:
    DIALOGUE_THEME_CONFIG = {
        "speaker": {
            "window_style": "say_window_speaker",
            "what_style": "say_dialogue",
            "what_color": "#f6efe4",
            "name_color": "#f3efe7",
            "name_background": "#15202adf",
            "window_background": "#091018e2",
            "accent_color": "#6f8ea3",
            "accent_glow": "#6f8ea340",
            "avatar_background": "#111a22f0",
            "seal_background": "#243845f0",
            "seal_color": "#e8f2f8",
            "para_background": "#173243e6",
            "para_color": "#d3e0e9",
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

    # 有现成头像素材的角色直接显示裁切图，没有素材时回退为单字印章。
    DIALOGUE_AVATAR_IMAGES = {
        "陈平安": im.Scale(
            im.Crop("lh/cpa/cpa_face_standard_01.png", 350, 40, 420, 420),
            150,
            150
        ),
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
        "裴钱": im.Scale(
            im.Crop("images/chapter1/c1_08_pq_pose_v1.png", 540, 60, 420, 420),
            150,
            150
        ),
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


    def resolve_dialogue_theme(who):
        current_theme = renpy.store.dialogue_ui_theme

        if current_theme:
            return current_theme

        if who is None:
            return "narration"

        if who == "陈平安":
            return "protagonist"

        return "speaker"


    def get_dialogue_ui(who):
        theme = resolve_dialogue_theme(who)
        ui = dict(DIALOGUE_THEME_CONFIG.get(theme, DIALOGUE_THEME_CONFIG["speaker"]))

        ui["theme"] = theme
        ui["avatar"] = DIALOGUE_AVATAR_IMAGES.get(who)
        ui["show_avatar"] = bool(who) and theme != "narration" and not renpy.variant("small")
        ui["show_name"] = bool(who) and theme not in ("thought", "protagonist_thought")
        ui["seal_text"] = who[:1] if who else ""
        ui["paralanguage"] = renpy.store.dialogue_paralanguage

        return ui
