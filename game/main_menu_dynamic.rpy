################################################################################
## 按第一章已完成场景累计解锁的静态标题背景
################################################################################

init -1 python:
    # Only the three approved prologue scenes are available. Unknown milestones
    # use the latest unlocked artwork that is actually available.
    story_title_backgrounds = {
        0: gui.main_menu_background,
        1: "gui/title_progress/prologue_gathering.png",
        2: "gui/title_progress/prologue_farewell.png",
    }

    def story_title_background():
        for stage in range(story_title_stage(), -1, -1):
            background = story_title_backgrounds.get(stage)
            if background and renpy.loadable(background):
                return background
        return story_title_backgrounds[0]


screen main_menu_dynamic_background():
    $ title_background = story_title_background()

    # Missing optional artwork never prevents reaching the save/load UI.
    if renpy.loadable(title_background):
        add title_background:
            xysize (config.screen_width, config.screen_height)
    else:
        add Solid("#172b32")
