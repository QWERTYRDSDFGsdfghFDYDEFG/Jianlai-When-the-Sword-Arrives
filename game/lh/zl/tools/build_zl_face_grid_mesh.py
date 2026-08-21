"""Build a regular, local-only deformation mesh over Zhu Lian's face views."""

from __future__ import annotations

import json
import math
from pathlib import Path

import cv2
import numpy as np


ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "game/lh/zl/exec-42da0fb1-b19a-4708-b3b4-2fc6f04516aa.png"
LANDMARKS = ROOT / "game/lh/zl/zl_face_mesh_v1.json"
OUT_JSON = ROOT / "game/lh/zl/zl_face_grid_mesh_v1.json"
OUT_IMAGE = ROOT / "game/lh/zl/zl_face_grid_mesh_map_v1.png"

GRID_SIZES = {
    "front": (20, 24),
    "three_quarter": (18, 24),
    "profile": (14, 24),
    "expression_inset": (16, 20),
}

HOLE_REGIONS = ["subject_right_eye", "subject_left_eye", "inner_lips"]
VIEW_COLORS = {
    "front": (0, 230, 255),
    "three_quarter": (70, 230, 70),
    "profile": (255, 150, 40),
    "expression_inset": (220, 80, 255),
}


def polygon(points, indices):
    return np.array([[points[i]["x_px"], points[i]["y_px"]] for i in indices], np.float32)


def inside(poly, x, y):
    return cv2.pointPolygonTest(poly, (float(x), float(y)), False) >= 0


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def rectangle_intersects_polygon(xmin, ymin, xmax, ymax, poly):
    # Reject a cell if a hole vertex enters it, a cell corner enters the hole,
    # or a hole edge crosses one of the cell's four local edges.
    if any(xmin <= p[0] <= xmax and ymin <= p[1] <= ymax for p in poly):
        return True
    corners = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
    if any(inside(poly, x, y) for x, y in corners):
        return True
    rect_edges = list(zip(corners, corners[1:] + corners[:1]))
    polygon_points = [(float(p[0]), float(p[1])) for p in poly]
    poly_edges = list(zip(polygon_points, polygon_points[1:] + polygon_points[:1]))
    for a, b in rect_edges:
        for c, d in poly_edges:
            if cv2.intersectConvexConvex(
                np.array([a, b, (b[0] + 0.001, b[1] + 0.001)], np.float32),
                np.array([c, d, (d[0] + 0.001, d[1] + 0.001)], np.float32),
            )[0] > 0:
                return True
    return False


def main():
    data = json.loads(LANDMARKS.read_text(encoding="utf-8"))
    image = cv2.imread(str(SOURCE), cv2.IMREAD_UNCHANGED)
    if image is None:
        raise FileNotFoundError(SOURCE)
    if image.ndim == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    if image.shape[2] == 4:
        alpha = image[:, :, 3]
        canvas = image[:, :, :3].copy()
        has_alpha = True
    else:
        alpha = np.full(image.shape[:2], 255, np.uint8)
        canvas = image[:, :, :3].copy()
        has_alpha = False
    height, width = canvas.shape[:2]

    output = {
        "schema_version": "1.0",
        "character": "朱敛",
        "character_id": "zl",
        "identity_state": "t5_old_servant_mask",
        "mesh_type": "regular_quad_grid_split_to_local_triangles",
        "source_image": SOURCE.relative_to(ROOT).as_posix(),
        "source_size": {"width": width, "height": height},
        "source_has_alpha": has_alpha,
        "semantic_landmark_source": LANDMARKS.relative_to(ROOT).as_posix(),
        "rules": {
            "cell_vertex_order": ["top_left", "top_right", "bottom_right", "bottom_left"],
            "triangle_split_even": [[0, 1, 2], [0, 2, 3]],
            "triangle_split_odd": [[0, 1, 3], [1, 2, 3]],
            "cell_requires_all_four_vertices_active": True,
            "forbid_cross_grid_edges": True,
            "forbid_cross_transparent_edges": True,
            "forbid_cross_region_edges": True,
            "hole_regions": HOLE_REGIONS,
        },
        "views": {},
    }

    for view_name, view in data["views"].items():
        cols, rows = GRID_SIZES[view_name]
        points = view["landmarks"]
        face_poly = polygon(points, data["regions"]["face_oval"])
        holes = [polygon(points, data["regions"][name]) for name in HOLE_REGIONS]
        xmin, ymin, xmax, ymax = view["face_bbox_px"]
        step_x = (xmax - xmin) / (cols - 1)
        step_y = (ymax - ymin) / (rows - 1)
        local_diag = math.hypot(step_x, step_y)
        max_edge = local_diag * 1.01

        vertices = []
        for row in range(rows):
            for col in range(cols):
                x = xmin + col * step_x
                y = ymin + row * step_y
                in_face = inside(face_poly, x, y)
                in_hole = any(inside(hole, x, y) for hole in holes)
                px = int(round(min(max(x, 0), width - 1)))
                py = int(round(min(max(y, 0), height - 1)))
                opaque = int(alpha[py, px]) > 0
                active = bool(in_face and not in_hole and opaque)
                vertices.append({
                    "index": row * cols + col,
                    "row": row,
                    "col": col,
                    "x_px": round(x, 3),
                    "y_px": round(y, 3),
                    "x_face_norm": round(col / (cols - 1), 7),
                    "y_face_norm": round(row / (rows - 1), 7),
                    "active": active,
                    "region": "face_skin" if active else "excluded",
                })

        cells, triangles = [], []
        for row in range(rows - 1):
            for col in range(cols - 1):
                tl = row * cols + col
                tr = tl + 1
                bl = (row + 1) * cols + col
                br = bl + 1
                quad = [tl, tr, br, bl]
                if not all(vertices[i]["active"] for i in quad):
                    continue
                cx = sum(vertices[i]["x_px"] for i in quad) / 4
                cy = sum(vertices[i]["y_px"] for i in quad) / 4
                if not inside(face_poly, cx, cy) or any(inside(h, cx, cy) for h in holes):
                    continue
                cell_xmin = min(vertices[i]["x_px"] for i in quad)
                cell_xmax = max(vertices[i]["x_px"] for i in quad)
                cell_ymin = min(vertices[i]["y_px"] for i in quad)
                cell_ymax = max(vertices[i]["y_px"] for i in quad)
                if any(rectangle_intersects_polygon(cell_xmin, cell_ymin, cell_xmax, cell_ymax, h)
                       for h in holes):
                    continue
                split = [[tl, tr, br], [tl, br, bl]] if (row + col) % 2 == 0 else [[tl, tr, bl], [tr, br, bl]]
                cell_index = len(cells)
                cells.append({"index": cell_index, "row": row, "col": col, "vertices": quad,
                              "triangles": [len(triangles), len(triangles) + 1]})
                for tri in split:
                    triangles.append({"index": len(triangles), "vertices": tri, "cell": cell_index})

        anchors = {}
        active_vertices = [v for v in vertices if v["active"]]
        for region, indices in data["regions"].items():
            anchors[region] = []
            for landmark_index in indices:
                lp = points[landmark_index]
                nearest = min(active_vertices, key=lambda v: (v["x_px"] - lp["x_px"]) ** 2 +
                                                             (v["y_px"] - lp["y_px"]) ** 2)
                anchors[region].append({"landmark_index": landmark_index,
                                        "grid_vertex_index": nearest["index"]})

        errors = []
        for tri in triangles:
            vs = [vertices[i] for i in tri["vertices"]]
            rows_used = {v["row"] for v in vs}
            cols_used = {v["col"] for v in vs}
            if max(rows_used) - min(rows_used) > 1 or max(cols_used) - min(cols_used) > 1:
                errors.append(f"triangle_{tri['index']}_crosses_grid")
            if not all(v["active"] and v["region"] == "face_skin" for v in vs):
                errors.append(f"triangle_{tri['index']}_crosses_region")
            coords = [(v["x_px"], v["y_px"]) for v in vs]
            lengths = [math.dist(coords[0], coords[1]), math.dist(coords[1], coords[2]),
                       math.dist(coords[2], coords[0])]
            if max(lengths) > max_edge:
                errors.append(f"triangle_{tri['index']}_long_edge")
            if abs(orient(*coords)) < 1e-6:
                errors.append(f"triangle_{tri['index']}_zero_area")

        output["views"][view_name] = {
            "grid": {"cols": cols, "rows": rows, "step_x_px": round(step_x, 4),
                     "step_y_px": round(step_y, 4)},
            "face_bbox_px": view["face_bbox_px"],
            "vertices": vertices,
            "cells": cells,
            "triangles": triangles,
            "semantic_anchors": anchors,
            "validation": {"passed": not errors, "errors": errors,
                           "active_vertices": len(active_vertices), "cells": len(cells),
                           "triangles": len(triangles), "max_allowed_edge_px": round(max_edge, 4)},
        }

        color = VIEW_COLORS[view_name]
        for cell in cells:
            quad = cell["vertices"]
            q = [(int(round(vertices[i]["x_px"])), int(round(vertices[i]["y_px"]))) for i in quad]
            for a, b in zip(q, q[1:] + q[:1]):
                cv2.line(canvas, a, b, color, 1, cv2.LINE_AA)
            if (cell["row"] + cell["col"]) % 2 == 0:
                cv2.line(canvas, q[0], q[2], color, 1, cv2.LINE_AA)
            else:
                cv2.line(canvas, q[1], q[3], color, 1, cv2.LINE_AA)
        for v in active_vertices:
            cv2.circle(canvas, (int(round(v["x_px"])), int(round(v["y_px"]))), 1, (255, 255, 255), -1)
        cv2.putText(canvas, f"{view_name}: {len(cells)} quads / {len(triangles)} tris",
                    (int(xmin), max(20, int(ymin) - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.42,
                    color, 1, cv2.LINE_AA)

    OUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    cv2.imwrite(str(OUT_IMAGE), canvas)
    summary = {name: view["validation"] for name, view in output["views"].items()}
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
