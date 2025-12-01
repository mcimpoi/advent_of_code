from tqdm.contrib.concurrent import process_map  # or thread_map
import time


def eval_with_concat(inputs):
    result, nums = inputs
    for x in range(3 ** (len(nums) - 1)):
        x1 = x
        digits = []
        # print(x)
        for _ in range(len(nums) - 1):
            digits.append(x1 % 3)
            x1 //= 3
        # print(digits)
        res = nums[0]
        for op, num in zip(digits, nums[1:]):
            if op == 2:
                res = int(str(res) + str(num))
            elif op == 0:
                res += num
            else:
                res *= num
        # print(res)
        if res == result:
            return True
    return False


if __name__ == "__main__":

    input_small = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

    lines = input_small.splitlines()
    eqns = []
    for line in lines:
        result, rest = line.split(":")
        result = int(result.split()[0])
        rest = [int(x) for x in rest.split()]
        eqns.append((result, rest))

    process_res = process_map(eval_with_concat, eqns, max_workers=8)

    total = 0
    for ok, val in zip(process_res, eqns):
        if ok:
            total += val[0]

    print(total)
