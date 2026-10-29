default persistent.dialogue_layout = "a2"
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

    # 旧自动头像素材保留兼容参考；A2/B2普通对白不再显示这些头像。
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


    # 保留旧剧情和存档中的双人标记；A2/B2不据此显示对话区头像。
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


    # A2/B2共用场景色板；由当前背景推导，回退/读档无需保存额外场景状态。
    DIALOGUE_SOFT_COLORS = {
        "a2": {"neutral": "#31312e", "cool": "#263639", "warm": "#3f352e"},
        "b2": {"neutral": "#2a3031", "cool": "#24373d", "warm": "#313735"},
    }
    DIALOGUE_SOFT_BACKDROPS = {
        layout: {
            palette: AlphaMask(
                Solid(color, xysize=(1920, 1080)),
                "gui/dialogue/soft_{}_mask.png".format(layout),
            )
            for palette, color in colors.items()
        }
        for layout, colors in DIALOGUE_SOFT_COLORS.items()
    }
    DIALOGUE_SOFT_PORTRAITS = {
        "c2_08_pq_surprise": "gui/dialogue/soft_pq_portrait.png",
        "c2_08_zl_tease": "gui/dialogue/soft_zl_portrait.png",
    }

    def get_dialogue_layout():
        value = persistent.dialogue_layout
        return value if value in ("a2", "b2") else "a2"

    def set_dialogue_layout(value):
        if value not in ("a2", "b2"):
            raise ValueError("Unknown dialogue layout: {!r}".format(value))
        persistent.dialogue_layout = value
        renpy.save_persistent()
        renpy.restart_interaction()

    def get_dialogue_palette():
        if not renpy.showing("bg"):
            return "neutral"
        name = "_".join(renpy.get_attributes("bg") or ())
        # 稳定代号与旧资源名遵循同一场次规则；蜈蚣岭日景不沿用夜廊色。
        if name in ("c2_08_wugong_memory_v1", "cg02_08_06"):
            return "neutral"
        if name.startswith(("c1_", "cg01_")):
            parts = name.split("_")
            if len(parts) > 1 and parts[1].isdigit() and 1 <= int(parts[1]) <= 12:
                return "cool"
        if name.startswith(("c2_05_", "c2_06_", "cg02_05_", "cg02_06_")):
            return "cool"
        if name in ("c2_03_fly_v1", "c2_03_river_v1", "cg02_03_07", "cg02_03_08"):
            return "cool"
        if name.startswith(("c2_08_", "cg02_08_")):
            return "warm"
        if name.startswith(("c2_07_", "cg02_07_")) and name not in ("c2_07_gate_v1", "cg02_07_01"):
            return "warm"
        return "neutral"

    def get_dialogue_ui(who, portrait=None, what=""):
        layout = get_dialogue_layout()
        palette = get_dialogue_palette()
        theme = resolve_dialogue_theme(who)
        small = renpy.variant("small")
        is_a2 = layout == "a2"
        # 仅这两种显式头像标记允许出现头像；旧自动/双人槽保留存档字段，停止显示。
        avatar = None
        if portrait is not None:
            spec = DIALOGUE_PORTRAIT_CONFIG.get(portrait)
            if spec is None or portrait not in DIALOGUE_SOFT_PORTRAITS:
                raise ValueError("Unknown dialogue portrait: {!r}".format(portrait))
            if spec["speaker"] != who:
                raise ValueError("Dialogue portrait {!r} does not belong to {!r}".format(portrait, who))
            avatar = DIALOGUE_SOFT_PORTRAITS[portrait]

        name = who
        tag = renpy.store.dialogue_paralanguage
        if theme in ("thought", "protagonist_thought"):
            if not name:
                name = tag or "心声"
            # 具名心声优先显示完整归属，避免再画一份相同的副语言标签。
            if tag and (tag in name or name in tag):
                tag = None
        left = 520 if avatar else (96 if small else 220)
        indent = 0 if is_a2 else 46
        name_size = (48 if is_a2 else 45) if small else (34 if is_a2 else 32)
        name_y = (738 if is_a2 else 722) if small else (800 if is_a2 else 780)
        body_y = 805 if small else (855 if is_a2 else 850)
        # 辅助字体由引擎放大；额外上移阅读区，给姓名和多行正文留足空间。
        font_scale = max(1.0, preferences.font_size)
        body_lift = int((font_scale - 1.0) * 180)
        name_lift = body_lift + int((font_scale - 1.0) * name_size * 1.3)
        return {
            "layout": layout,
            "palette": palette,
            "theme": theme,
            "backdrop": DIALOGUE_SOFT_BACKDROPS[layout][palette],
            "backdrop_scale": (1.30 if small else 1.0) + (font_scale - 1.0) * 0.6,
            "avatar": avatar,
            "show_avatar": avatar is not None,
            "show_pair": False,
            "show_name": bool(name),
            "name": name,
            "portrait": portrait,
            "paralanguage": tag,
            "name_x": left,
            "name_y": name_y - name_lift,
            "name_size": name_size,
            "name_bold": is_a2,
            "body_x": left + indent,
            "body_y": body_y - body_lift,
            "body_size": (45 if is_a2 else 43) if small else (38 if is_a2 else 36),
            "text_width": (1800 if small else 1720) - left - indent,
            "line_spacing": 8 if small else 6,
            "what_color": "#f2eadf",
            "name_color": "#f4ecdf",
        }


    def get_dialogue_pair_slot(name, who, ui):
        # 旧工具仍可解析槽位；当前say不调用此兼容路径。
        legacy_ui = dict(DIALOGUE_THEME_CONFIG.get(ui.get("theme"), DIALOGUE_THEME_CONFIG["speaker"]))
        legacy_ui.update(ui)
        ui = legacy_ui
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
