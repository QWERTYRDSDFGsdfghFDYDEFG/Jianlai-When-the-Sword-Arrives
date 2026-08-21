"""Extract Zhu Lian's fixed MediaPipe face topology and identity measurements."""

from __future__ import annotations

import json
import math
from pathlib import Path

import cv2
import mediapipe as mp
import numpy as np


ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "game/lh/zl/exec-42da0fb1-b19a-4708-b3b4-2fc6f04516aa.png"
MODEL = ROOT / ".codex_tools/face_mesh/models/face_landmarker.task"
OUT_JSON = ROOT / "game/lh/zl/zl_face_mesh_v1.json"
OUT_IMAGE = ROOT / "game/lh/zl/zl_face_mesh_map_v1.png"

REGIONS = {
    "face_oval": [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288,
                  397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136,
                  172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109],
    "subject_right_eyebrow": [70, 63, 105, 66, 107, 55, 65, 52, 53, 46],
    "subject_left_eyebrow": [336, 296, 334, 293, 300, 285, 295, 282, 283, 276],
    "subject_right_eye": [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157,
                          158, 159, 160, 161, 246],
    "subject_left_eye": [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388,
                         387, 386, 385, 384, 398],
    "nose_bridge": [168, 6, 197, 195, 5, 4, 1, 19],
    "nose_base": [129, 98, 97, 2, 326, 327, 358],
    "outer_lips": [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308,
                   324, 318, 402, 317, 14, 87, 178, 88, 95, 78],
    "inner_lips": [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318,
                   402, 317, 14, 87, 178, 88, 95],
    "subject_right_cheek": [234, 93, 132, 58, 172, 136, 150, 149],
    "subject_left_cheek": [454, 323, 361, 288, 397, 365, 379, 378],
    "chin_jaw": [172, 136, 150, 149, 176, 148, 152, 377, 400, 378, 379, 365, 397],
    "forehead_center": [10, 151, 9, 8, 107, 336],
    "subject_right_iris": [468, 469, 470, 471, 472],
    "subject_left_iris": [473, 474, 475, 476, 477],
}

VIEW_HINTS = {
    "front": (0.19, 0.38),
    "three_quarter": (0.48, 0.39),
    "profile": (0.75, 0.37),
    "expression_inset": (0.82, 0.82),
}

COLORS = {
    "face_oval": (60, 220, 255), "subject_right_eye": (40, 220, 40),
    "subject_left_eye": (40, 220, 40), "subject_right_eyebrow": (255, 180, 40),
    "subject_left_eyebrow": (255, 180, 40), "nose_bridge": (255, 80, 80),
    "nose_base": (255, 80, 80), "outer_lips": (200, 80, 255),
    "inner_lips": (200, 80, 255), "chin_jaw": (60, 220, 255),
    "forehead_center": (0, 165, 255), "subject_right_cheek": (180, 180, 40),
    "subject_left_cheek": (180, 180, 40), "subject_right_iris": (0, 255, 255),
    "subject_left_iris": (0, 255, 255),
}


def dist(a, b):
    return math.hypot(a["x_px"] - b["x_px"], a["y_px"] - b["y_px"])


def main():
    image = cv2.imread(str(SOURCE))
    if image is None:
        raise FileNotFoundError(SOURCE)
    height, width = image.shape[:2]
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    base = mp.tasks.BaseOptions(model_asset_path=str(MODEL))
    opts = mp.tasks.vision.FaceLandmarkerOptions(
        base_options=base,
        running_mode=mp.tasks.vision.RunningMode.IMAGE,
        num_faces=4,
        min_face_detection_confidence=0.35,
        min_face_presence_confidence=0.35,
        min_tracking_confidence=0.35,
        output_face_blendshapes=True,
        output_facial_transformation_matrixes=True,
    )
    with mp.tasks.vision.FaceLandmarker.create_from_options(opts) as detector:
        result = detector.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb))

    detected = []
    for i, face in enumerate(result.face_landmarks):
        xs = [p.x for p in face]
        ys = [p.y for p in face]
        center = (sum(xs) / len(xs), sum(ys) / len(ys))
        view = min(VIEW_HINTS, key=lambda k: math.dist(center, VIEW_HINTS[k]))
        detected.append((view, i, face, center))
    detected.sort(key=lambda item: list(VIEW_HINTS).index(item[0]))

    output = {
        "schema_version": "1.0",
        "character": "朱敛",
        "character_id": "zl",
        "identity_state": "t5_old_servant_mask",
        "topology": "MediaPipe Face Landmarker 478",
        "index_space": "canonical_0_based",
        "source_image": SOURCE.relative_to(ROOT).as_posix(),
        "source_size": {"width": width, "height": height},
        "regions": REGIONS,
        "views": {},
    }
    overlay = image.copy()

    for view, result_index, face, center in detected:
        points = []
        for idx, p in enumerate(face):
            points.append({
                "index": idx,
                "x_norm": round(float(p.x), 7),
                "y_norm": round(float(p.y), 7),
                "z_norm": round(float(p.z), 7),
                "x_px": round(float(p.x * width), 2),
                "y_px": round(float(p.y * height), 2),
            })
        xmin = min(p["x_px"] for p in points)
        xmax = max(p["x_px"] for p in points)
        ymin = min(p["y_px"] for p in points)
        ymax = max(p["y_px"] for p in points)
        bbox_width = max(1.0, xmax - xmin)
        bbox_height = max(1.0, ymax - ymin)
        for point in points:
            point["x_face_norm"] = round((point["x_px"] - xmin) / bbox_width, 7)
            point["y_face_norm"] = round((point["y_px"] - ymin) / bbox_height, 7)
        face_width = max(1.0, dist(points[234], points[454]))
        measures = {
            "face_height_over_width": round(dist(points[10], points[152]) / face_width, 4),
            "eye_spacing_over_face_width": round(dist(points[133], points[362]) / face_width, 4),
            "nose_length_over_face_width": round(dist(points[168], points[2]) / face_width, 4),
            "mouth_width_over_face_width": round(dist(points[61], points[291]) / face_width, 4),
            "jaw_width_over_face_width": round(dist(points[172], points[397]) / face_width, 4),
        }
        visibility = {name: "high" for name in REGIONS}
        if view == "profile":
            visibility["subject_left_eye"] = "low"
            visibility["subject_left_eyebrow"] = "low"
            visibility["subject_left_cheek"] = "low"
            visibility["subject_left_iris"] = "low"
        output["views"][view] = {
            "detector_result_index": result_index,
            "face_bbox_px": [round(xmin, 2), round(ymin, 2), round(xmax, 2), round(ymax, 2)],
            "center_norm": [round(center[0], 6), round(center[1], 6)],
            "region_visibility": visibility,
            "identity_measurements": measures,
            "landmarks": points,
        }

        for name, indices in REGIONS.items():
            color = COLORS[name]
            coords = np.array([[int(points[j]["x_px"]), int(points[j]["y_px"])] for j in indices], np.int32)
            if len(coords) > 1:
                cv2.polylines(overlay, [coords], False, color, 1, cv2.LINE_AA)
            for j in indices:
                x, y = int(points[j]["x_px"]), int(points[j]["y_px"])
                cv2.circle(overlay, (x, y), 2, color, -1, cv2.LINE_AA)
        cv2.rectangle(overlay, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 255, 255), 1)
        cv2.putText(overlay, view, (int(xmin), max(18, int(ymin) - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    OUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    cv2.imwrite(str(OUT_IMAGE), overlay)
    print(json.dumps({"faces": len(detected), "views": list(output["views"]),
                      "json": str(OUT_JSON), "image": str(OUT_IMAGE)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
