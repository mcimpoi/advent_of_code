
import os
import tqdm

def parse_input(fname: str) -> list[tuple[int, int]]:
    with open(fname, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    data = []
    for line in lines:
        data.append(tuple(int(x) for x in line.split(",")))
    return data

def solve_day_09_part1(fname: str):
    data = parse_input(fname)
    max_area = 0
    for x1, y1 in data:
        for x2, y2 in data:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            max_area = max(area, max_area)
    return max_area


def get_intersections(polygon_points, y_line):
    intersections = []
    n = len(polygon_points)
    
    for i in range(n):
        # Get the current edge P1 -> P2
        p1 = polygon_points[i]
        p2 = polygon_points[(i + 1) % n] # Wrap around to the start
        
        # Check if the edge is horizontal (parallel to line)
        if p1[1] == p2[1]:
            continue # Usually ignored in scan-line logic
            
        # Check if y_line bounds are strictly within the edge's Y range
        # We use strict comparison (<) for one end to handle vertices
        if min(p1[1], p2[1]) < y_line <= max(p1[1], p2[1]):
            
            # Calculate intersection X
            # (x2 - x1) * (y_line - y1) / (y2 - y1) + x1
            x_int = int(p1[0] + (p2[0] - p1[0]) * (y_line - p1[1]) / (p2[1] - p1[1]))
            intersections.append(x_int)
            
    # Sort X intersections from left to right (standard practice)
    return sorted(intersections)

def solve_day_09_part2(fname: str):
    data = parse_input(fname)
   
    min_x, min_y = min(x for x, y in data), min(y for x, y in data)
    print(min_x, min_y)
    max_x, max_y = max(x for x, y in data), max(y for x, y in data)
    print(max_x, max_y)

    line2_y = data[249][1]
    line1_y = data[247][1]
    print(f"{line1_y=}, {line2_y=}")
    max_area = 0
    for idx, point in tqdm.tqdm(enumerate(data)):
        _, y = point
        intersections = get_intersections(data, y)
        if len(intersections) < 2:
            print(f"! {y=}")
            continue
        area = 0
        if y > line1_y:
            area = (max(intersections) - min(intersections) + 1) * (y - line1_y + 1)

        elif y < line2_y:
            area = (max(intersections) - min(intersections) + 1) * (line2_y - y + 1)
        else:
            continue
        if area > max_area:
            max_area = area
            max_pt = point
            max_idx = idx
            max_isect = intersections

    print(max_pt, max_isect, max_idx)
    print(max_area)
    return max_area


if __name__ == "__main__":
    result = solve_day_09_part1(os.path.expanduser("~/day_09.txt"))
    print(f"Max area: {result}")
    solve_day_09_part2(os.path.expanduser("~/day_09.txt"))