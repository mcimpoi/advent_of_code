from collections import defaultdict
from io import DEFAULT_BUFFER_SIZE
from typing import List, Tuple, Union, Optional, Dict
from collections import deque

INPUT_FILE: str = "2022/data/day_05.txt"
MAX_DIR_SIZE: int = 100000

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name: str, parent: Optional["Directory"]) -> None:
        self.total_size: int = 0
        self.subdirs: Dict[str, Directory] = {}
        self.files: List[File] = []
        self.parent: Optional[Directory] = parent
        self.updated = False

def parse_input(input_file: str) -> Directory:
    with open(input_file, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    root = Directory("<ROOT>", None)
    root.subdirs["/"] = Directory("/", None)
    idx = 0
    crt_path = []
    crt_dir = root

    while idx < len(lines):
        if lines[idx].startswith("$ cd"):
            dir_name = lines[idx][5:]
            if dir_name == "..":
                # crt_path.pop()
                crt_dir = crt_dir.parent if crt_dir is not None else root
            else:
                if crt_dir is None:
                    raise ValueError(f"This should not happen: Line: {lines[idx]}")
                crt_dir = crt_dir.subdirs[dir_name]

            idx += 1
        elif lines[idx].startswith("$ ls"):
            idx += 1
            if crt_dir is None:
                raise ValueError("This should not happen")
            while idx < len(lines) and not lines[idx].startswith("$"):
                if lines[idx].startswith("dir"):
                    subdir_name = lines[idx].split()[1]
                    crt_dir.subdirs[subdir_name] = Directory(subdir_name, crt_dir)
                else:
                    parts = lines[idx].split()
                    filename = parts[1]
                    filesize = int(parts[0])
                    crt_dir.files.append(File(filename, filesize))
                idx += 1
    return root

def update_total_size(root: Directory) -> Directory:
    if root.updated:
        return root
    total_size = sum(x.size for x in root.files)
    for subdir in root.subdirs:
        update_total_size(root.subdirs[subdir])
        total_size += root.subdirs[subdir].total_size
    root.total_size = total_size
    return root

def day_05_part1(input_file: str) -> int:
    root = parse_input(input_file)
    update_total_size(root.subdirs["/"])
    
    q = deque()
    q.append(root.subdirs["/"])
    total_sum = 0 
    while len(q) > 0:
        crt = q.pop()
        if crt.total_size <= MAX_DIR_SIZE:
            total_sum += crt.total_size
        for subdir in crt.subdirs:
            q.append(crt.subdirs[subdir]) 

    return total_sum

def day_05_part2(input_file: str) -> int:
    SYSTEM_SIZE = 70000000
    NEEDED_FREE = 30000000
    root = parse_input(input_file)
    update_total_size(root.subdirs["/"])
    to_delete = NEEDED_FREE - (SYSTEM_SIZE - root.subdirs["/"].total_size)

    q = deque( )   
    q.append(root.subdirs["/"])
    smallest_size = SYSTEM_SIZE
    while len(q) > 0:
        crt = q.pop()
        if crt.total_size >= to_delete:
            smallest_size = min(smallest_size, crt.total_size)
        for subdir in crt.subdirs:
            q.append(crt.subdirs[subdir]) 

    return smallest_size
    
if __name__ == "__main__": 
    print(day_05_part1(INPUT_FILE))
    print(day_05_part2(INPUT_FILE))