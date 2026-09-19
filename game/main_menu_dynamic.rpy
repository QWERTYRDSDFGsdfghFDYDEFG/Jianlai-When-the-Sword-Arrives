################################################################################
## 随存档进度变化的静态标题场景
################################################################################

init -1 python:
    # Only the three approved prologue scenes are available. Unknown milestones
    # and missing later artwork always fall back to the initial academy night.
    story_title_backgrounds = {
        0: gui.main_menu_background,
        1: "gui/title_progress/prologue_gathering.png",
        2: "gui/title_progress/prologue_farewell.png",
    }

    def story_title_background():
        background = story_title_backgrounds.get(
            story_title_stage(), story_title_backgrounds[0])
        if renpy.loadable(background):
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
