# 已停用：P5实验界面与当前人物、场景画风不协调（2026-10-26用户否决）。
# 当前say/quick_menu不再调用；保留旧定义及复查资料，不据此宣称旧存档兼容。
init -4 python:
    C2_08_COMIC_PORTRAITS = {
        "c2_08_pq_surprise": -20,
        "c2_08_zl_tease": -120,
    }

    def c2_08_comic_active():
        return bool(renpy.get_screen("say")) and (
            renpy.get_screen_variable("portrait", screen="say") in C2_08_COMIC_PORTRAITS
        )

    def c2_08_comic_avatar(portrait):
        spec = DIALOGUE_PORTRAIT_CONFIG[portrait]
        return Transform(
            Transform(spec["path"], crop=spec["crop"]),
            zoom=680.0 / spec["crop"][3],
        )

    class C2ComicButtonBackground(renpy.Displayable):
        """随按钮尺寸绘制斜切边框，避免缩放后描边和斜角失配。"""

        def __init__(self, fill, edge, **kwargs):
            super(C2ComicButtonBackground, self).__init__(**kwargs)
            self.fill = fill
            self.edge = edge

        def render(self, width, height, st, at):
            width, height = int(width), int(height)
            rv = renpy.Render(width, height)
            canvas = rv.canvas()
            cut = max(6, int(height * 0.20))
            border = max(2, int(height * 0.045))
            canvas.polygon(self.edge, [(cut, 0), (width, 0),
                                      (width-cut, height), (0, height)])
            canvas.polygon(self.fill, [(cut+border, border), (width-border, border),
                                      (width-cut-border, height-border), (border, height-border)])
            return rv


screen c2_08_comic_say(who, what, portrait):
    window:
        id "window"
        # Character 会覆盖 id 的 style；位置和字号直接声明，避免继承旧底栏。
        background None
        padding (0, 0, 0, 0)
        xpos 0
        ypos 0
        xanchor 0
        yanchor 0
        xfill False
        yfill False
        xysize (1920, 1080)

        fixed:
            xysize (1920, 1080)

            # 胸像属于UI前景，底端压出画面；不作为堂内人物层显示。
            add c2_08_comic_avatar(portrait):
                id "dialogue_avatar"
                xpos C2_08_COMIC_PORTRAITS[portrait]
                ypos 430

            # 以场景坐标留出底部操作区；背景与头像的构图保持。
            add "gui/dialogue/c2_08_comic_frame.svg" yoffset -90

            text who:
                id "who"
                font gui.name_text_font
                size 43
                bold True
                color "#080808"
                kerning 5
                outlines []
                xpos 594
                ypos 644
                at Transform(rotate=-7.0)

            text what:
                id "what"
                font gui.text_font
                size 38
                color "#ffffff"
                bold True
                line_spacing 12
                layout "greedy"
                outlines []
                xpos 654
                ypos 771
                xsize 890


screen c2_08_comic_quick_menu():
    # 锚定16:9游戏画面，而非桌面窗口外沿；随场景统一等比缩放。
    hbox:
        id "c2_08_comic_controls"
        xpos 0.60
        xanchor 0.5
        yalign 1.0
        yoffset -int(config.screen_height * 0.013)
        spacing int(config.screen_width * 0.00625)
        style_prefix "c2_08_comic_quick"

        textbutton _("回退") id "c2_08_quick_rollback" action Rollback()
        textbutton _("快进") id "c2_08_quick_skip" action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("自动") id "c2_08_quick_auto" action Preference("auto-forward", "toggle")
        textbutton _("快存") id "c2_08_quick_save" action StoryQuickSave()
        textbutton _("快读") id "c2_08_quick_load" action StoryQuickLoad()
        textbutton _("菜单") id "c2_08_quick_menu" action ShowMenu()


style c2_08_comic_quick_button is default:
    xsize int(config.screen_width * 0.06875)
    ysize int(config.screen_height * 0.04815)
    padding (12, 0, 12, 0)
    background C2ComicButtonBackground((8, 8, 8, 242), (235, 235, 235, 255))
    hover_background C2ComicButtonBackground((255, 255, 255, 255), (255, 255, 255, 255))
    selected_background C2ComicButtonBackground((255, 255, 255, 255), (255, 255, 255, 255))
    insensitive_background C2ComicButtonBackground((8, 8, 8, 210), (105, 105, 105, 255))

style c2_08_comic_quick_button_text is default:
    font gui.interface_text_font
    size int(config.screen_height * 0.0241)
    bold True
    color "#ffffff"
    hover_color "#080808"
    selected_color "#080808"
    insensitive_color "#777777"
    xalign 0.5
    yalign 0.5

style c2_08_comic_quick_button:
    variant "touch"
    xsize int(config.screen_width * 0.0771)
    ysize int(config.screen_height * 0.0593)

style c2_08_comic_quick_button_text:
    variant "touch"
    size int(config.screen_height * 0.0278)
