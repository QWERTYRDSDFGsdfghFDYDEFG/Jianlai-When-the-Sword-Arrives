# Story transitions
#
# Keep the vocabulary deliberately small so the prologue feels like one
# continuous piece instead of a collection of unrelated effects.

# Same place and time: a restrained change of framing.
define trans_short = Dissolve(0.30)

# A gentle passage forward while the emotional thread stays continuous.
define trans_passage = Dissolve(0.60)

# Cui Dongshan's illusion reveals. This can later be replaced by a dedicated
# mist/golden-light mask without changing every scene call in the script.
define trans_illusion = Dissolve(0.45)

# A clear change of place while the night continues.
define trans_location = Fade(0.45, 0.15, 0.55, color="#070b12")

# A larger change of time, especially night to morning.
define trans_time = Fade(0.80, 0.25, 0.80, color="#070b12")

# Opening and chapter-boundary timing.
define trans_opening = Fade(0.20, 0.10, 0.85, color="#05070a")
define trans_chapter_out = Dissolve(1.20)
define trans_chapter_in = Dissolve(0.85)
