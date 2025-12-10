import heapq
import os 

from collections import Counter
import tqdm

def parse_input(fname: str) -> list[tuple[int, int, int]]:
    with open(fname, 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        parts = line.strip().split(",")
        data.append(tuple(int(part) for part in parts))
    return data

def solve_day_08_part_1(data: list[tuple[int, int, int]], n_times: int) -> int:
    pq = []
    
    for idx1, point in enumerate(data):
        x, y, z = point
        for  other_point in data[idx1 + 1:]:
            ox, oy, oz = other_point
            distance = (x - ox) ** 2 + (y - oy) ** 2 + (z - oz) ** 2
            heapq.heappush(pq, (distance, idx1, data.index(other_point)))
    
    cluster = [-1 for _ in data]
    cluster_id = 0
    for _ in tqdm.tqdm(range(n_times)):
        distance, idx1, idx2 = heapq.heappop(pq)
        # print(f"{idx1=} {data[idx1]=} {idx2=} {data[idx2]=} {distance=}")
        if cluster[idx1] == -1 and cluster[idx2] == -1:
            cluster_id += 1
            cluster[idx1] = cluster_id
            cluster[idx2] = cluster_id
        elif cluster[idx1] != -1 and cluster[idx2] == -1:
            cluster[idx2] = cluster[idx1]
        elif cluster[idx1] == -1 and cluster[idx2] != -1:
            cluster[idx1] = cluster[idx2]
        else:
            old_id = max(cluster[idx1], cluster[idx2])
            new_id = min(cluster[idx1], cluster[idx2])
            for i in range(len(cluster)):
                if cluster[i] == old_id:
                    cluster[i] = new_id
    
    c = Counter(cluster)
    top_clusters = [(v, k) for k, v in c.items() if k != -1]
    top_clusters.sort(reverse=True)
    return top_clusters[0][0] * top_clusters[1][0] * top_clusters[2][0]
            
def solve_day_08_part_2(data: list[tuple[int, int, int]], n_times: int) -> int:
    pq = []
    
    for idx1, point in enumerate(data):
        x, y, z = point
        for  other_point in data[idx1 + 1:]:
            ox, oy, oz = other_point
            distance = (x - ox) ** 2 + (y - oy) ** 2 + (z - oz) ** 2
            heapq.heappush(pq, (distance, idx1, data.index(other_point)))
    
    cluster = [-1 for _ in data]
    cluster_id = 0
    
    for step in tqdm.tqdm(range(n_times)):
        distance, idx1, idx2 = heapq.heappop(pq)
        # print(f"{step=} {idx1=} {data[idx1]=} {idx2=} {data[idx2]=} {distance=}")
        if cluster[idx1] == -1 and cluster[idx2] == -1:
            cluster_id += 1
            cluster[idx1] = cluster_id
            cluster[idx2] = cluster_id
        elif cluster[idx1] != -1 and cluster[idx2] == -1:
            cluster[idx2] = cluster[idx1]
            #print(cluster)
        elif cluster[idx1] == -1 and cluster[idx2] != -1:
            cluster[idx1] = cluster[idx2]
            # print(cluster)
        else:
            old_id = max(cluster[idx1], cluster[idx2])
            new_id = min(cluster[idx1], cluster[idx2])
            for i in range(len(cluster)):
                if cluster[i] == old_id:
                    cluster[i] = new_id
        if cluster[idx1] == 1:
            ok = True
            for c in cluster:
                if c != 1:
                    ok = False
                    break
            if ok == True:
                print(data[idx1], "\n", data[idx2])
                return data[idx1][0] * data[idx2][0]
    return -1

if __name__ == "__main__":
    data = parse_input(os.path.expanduser("~/day_08.txt"))
    print(solve_day_08_part_2(data, 10000))