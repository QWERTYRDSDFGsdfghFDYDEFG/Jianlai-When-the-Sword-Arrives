# Local Windows demo packaging; keep production files separate from QA/source work.
init -2 python:
    for pattern in (
        "work/**", "tools/**", "**/.**", "**/AGENTS.md", "**.log",
        "**.psd", "**.cmo3", "**.cs", "**.md", "**.bak",
        "**.zip", "game/Codex/**", "game/saves/**", "game/tools/**", "game/**/tools/**",
        "errors.txt", "traceback.txt", "log.txt", "renpy-sdk-path.txt",
        "project.json", "*.exe",
    ):
        build.classify(pattern, None)
    build.directory_name = "Jianlai-When-the-Sword-Arrives-1.0"
    build.include_update = False
