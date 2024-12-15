input_small = """125 17"""
input_large = """0 4 4979 24 4356119 914 85734 698829"""

from tqdm import tqdm
from functools import lru_cache


def solve_day_11_part_1(input):
    def step(nums):
        new_nums = []
        for num in nums:
            if num == 0:
                new_nums.append(1)
            elif len(str(num)) % 2 == 0:
                numstr = str(num)
                new_len = len(numstr) // 2
                n1 = int(numstr[:new_len])
                n2 = int(numstr[new_len:])
                new_nums.append(n1)
                new_nums.append(n2)
            else:
                new_nums.append(num * 2024)
        return new_nums

    nums = map(int, input.split())

    for i in tqdm(range(25)):
        nums = step(nums)
        print(i, len(nums))
    return len(nums)


def solve_day_11_part_2(nums):
    @lru_cache(None)
    def step(num):
        if num == 0:
            return [1]
        elif len(str(num)) % 2 == 0:
            numstr = str(num)
            new_len = len(numstr) // 2
            n1 = int(numstr[:new_len])
            n2 = int(numstr[new_len:])
            return [n1, n2]
        else:
            return [num * 2024]

    for i in range(25):
        new_nums = []
        for num in nums:
            new_nums.extend(step(num))
        nums = new_nums
        del new_nums
    return len(nums), nums


cache = {}


def solve_25(x):

    @lru_cache(None)
    def step(num):
        if num == 0:
            return [1]
        elif len(str(num)) % 2 == 0:
            numstr = str(num)
            new_len = len(numstr) // 2
            n1 = int(numstr[:new_len])
            n2 = int(numstr[new_len:])
            return [n1, n2]
        else:
            return [num * 2024]

    if x in cache:
        return cache[x]

    nums = [x]
    for i in range(25):
        new_nums = []
        for num in nums:
            new_nums.extend(step(num))
        nums = new_nums
        del new_nums
    cache[x] = tuple(nums)
    return cache[x]


cache50 = {}


def solve_50(x):
    if x in cache50:
        return cache50[x]
    res = 0
    for y in solve_25(x):
        res += len(solve_25(y))
    cache50[x] = res
    return cache50[x]


if __name__ == "__main__":
    nums = list(map(int, input_large.split()))

    total = 0
    for n in tqdm(nums):
        res = solve_25(n)
        for n1 in tqdm(res):
            total += solve_50(n1)

    print(total)
