init:
    # Keep the staging alias tied to the existing indexed full-body reference.
    image cds standard = "lh/cds/cds_full_base_v11.png"

transform left_front:
    xalign 0.18
    yalign 1.0
    zoom 0.98

transform left_medium:
    xalign 0.24
    yalign 1.0
    zoom 0.92

transform center_medium:
    xalign 0.50
    yalign 1.0
    zoom 0.92

transform right_medium:
    xalign 0.76
    yalign 1.0
    zoom 0.92

transform right_back:
    xalign 0.84
    yalign 1.0
    zoom 0.82
    alpha 0.96
