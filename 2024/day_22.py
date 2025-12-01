from functools import cache
import tqdm


@cache
def step(secret: int) -> int:
    mul64 = 64 * secret
    secret = secret ^ mul64
    secret = secret % 16777216
    div32 = secret // 32
    secret = secret ^ div32
    secret = secret % 16777216

    mul2048 = 2048 * secret
    secret = secret ^ mul2048
    secret = secret % 16777216

    return secret


def step_2k(secret: int) -> int:
    for _ in range(2000):
        secret = step(secret)
    return secret


def step_2k_mod(secret: int) -> list[int]:
    res = [-1 for _ in range(2000)]
    res[0] = secret % 10
    for i in range(1, 2000):
        secret = step(secret)
        res[i] = secret % 10
    return res


def solve_day_22_part_1(fname: str) -> int:
    with open(fname) as f:
        secrets = [int(x.strip()) for x in f.readlines()]

    res = 0
    for secret in secrets:
        secret = step_2k(secret)
        # print(secret)
        res += secret

    return res


def solve_day_22_part_2(fname: str) -> int:
    with open(fname) as f:
        secrets = [int(x.strip()) for x in f.readlines()]

    all_deltas = set()
    deltas_by_secret = {}
    res = 0
    for secret in tqdm.tqdm(secrets):
        nums = step_2k_mod(secret)
        num_deltas = {}
        for i in range(4, 2000):
            delta = (
                nums[i - 3] - nums[i - 4],
                nums[i - 2] - nums[i - 3],
                nums[i - 1] - nums[i - 2],
                nums[i] - nums[i - 1],
            )
            if num_deltas.get(delta, -1) == -1:
                num_deltas[delta] = nums[i]
                all_deltas.add(delta)
            else:
                continue
        deltas_by_secret[secret] = num_deltas

    max_res = 0
    for delta in tqdm.tqdm(all_deltas):
        res_delta = 0
        for secret in secrets:
            num_deltas = deltas_by_secret[secret]
            if num_deltas.get(delta, -1) != -1:
                # print(secret, num_deltas[delta])
                res_delta += num_deltas[delta]
        max_res = max(max_res, res_delta)

    return max_res


if __name__ == "__main__":
    print(solve_day_22_part_2("2024/day_22_large.txt"))
