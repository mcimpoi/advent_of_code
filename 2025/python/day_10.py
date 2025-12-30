import os
import tqdm
import heapq

def parse_input(fname: str):
    res = []
    configs = []
    with open(fname, 'r') as f:
        configs = [line.strip() for line in f.readlines()]
    for config_line in configs:
        parts = config_line.split(' ')
        display = parts[0]
        btn_cfg  = []
        for i in range(1, len(parts) - 1):
            buttons_str = parts[i][1:-1]
            buttons = [int(x) for x in buttons_str.split(',')]
            btn_cfg.append(buttons)
        joltage_cfg_str = parts[-1][1:-1]
        joltage_cfg = [int(x) for x in joltage_cfg_str.split(',')]
        res.append(([1 if x == "#" else 0 for x in display[1:-1]], btn_cfg, joltage_cfg))

    return res

def solve_day_10_part1(fname: str):
    data = parse_input(fname)
    
    res = 0
    for goal_cfg, btn_cfg, _ in data:
        min_cfg = None
        for mask_int in range(1 << len(btn_cfg)):
            crt_cfg = [0 for _ in goal_cfg]
            mask_bin = f"{mask_int:0{len(btn_cfg)}b}"
            for btn_idx, btn_state in enumerate(mask_bin):
                if btn_state == '1':
                    for led in btn_cfg[btn_idx]:
                        crt_cfg[led] ^= 1
            if crt_cfg == goal_cfg:
                if min_cfg is None:
                    min_cfg = sum(int(x) for x in mask_bin)
                else:
                    min_cfg = min(min_cfg, sum(int(x) for x in mask_bin))
        res += min_cfg
    return res


def solve_with_astar(vectors, target):
    target = tuple(target)
    n_dims = len(target)
    
    # Pre-calculate the "max mass" a single vector can contribute (for heuristic)
    # Avoid division by zero
    max_vec_sum = max([sum(v) for v in vectors]) if vectors else 1 
    
    # Priority Queue stores: (Priority, current_sum, coeffs, start_index)
    # Priority = (Cost so far + Estimated Cost to go)
    # We use a tuple for 'coeffs' so it's immutable/hashable if needed, or list is fine
    pq = [(0, tuple([0]*n_dims), [0]*len(vectors), 0)]
    
    visited = set()

    while pq:
        # Pop the element with the lowest estimated cost
        priority, curr_sum, coeffs, start_idx = heapq.heappop(pq)
        
        if curr_sum == target:
            return coeffs
        
        # Optimization: Early exit if we already visited this state with a lower/equal cost
        # (Simplified for this example)
        if curr_sum in visited: 
            continue
        visited.add(curr_sum)

        for i in range(start_idx, len(vectors)):
            vec = vectors[i]
            
            # Check constraints (Pruning)
            new_sum = tuple(c + v for c, v in zip(curr_sum, vec))
            if any(ns > t for ns, t in zip(new_sum, target)):
                continue
                
            new_coeffs = list(coeffs)
            new_coeffs[i] += 1
            
            # Cost so far = sum of coefficients
            g_score = sum(new_coeffs)
            
            # Heuristic (h): Remaining sum needed / Max possible reduction per step
            remaining_diff = sum(t - s for t, s in zip(target, new_sum))
            h_score = remaining_diff / max_vec_sum
            
            f_score = g_score + h_score
            
            heapq.heappush(pq, (f_score, new_sum, new_coeffs, i))
            
    return None

def solve_day_10_part2(fname: str):
    data = parse_input(fname)
    # Part 2 not implemented yet
    res = 0
    for _, btn_cfg, joltage_cfg in tqdm.tqdm(data):
        vectors = []
        for btn in btn_cfg:
            vec = [0 for _ in joltage_cfg]
            for btn_led in btn:
                vec[btn_led] = 1
            vectors.append(vec)
        crt_sum = sum(solve_with_astar(vectors, joltage_cfg))
        res += crt_sum
    return res
        

if __name__ == "__main__":
    print(solve_day_10_part1(os.path.expanduser("~/day_10.txt")))
    print(solve_day_10_part2(os.path.expanduser("~/day_10.txt")))


            
    