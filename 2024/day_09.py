def read_input(file_path):
    with open(file_path, "r") as file:
        return [int(x) for x in file.read().strip()]


def expand(data):
    res = []
    idx = 0
    for i in range(len(data)):
        if i % 2 == 0:
            res += [idx] * data[i]
            idx += 1
        else:
            res += [-1] * data[i]
    return res


def solve_day_09_p1(data):
    expanded = expand(data)
    right = len(expanded) - 1
    left = 0
    while right > left:
        while right > left and expanded[right] == -1:
            right -= 1
        while right > left and expanded[left] != -1:
            left += 1
        if right > left:
            expanded[right], expanded[left] = expanded[left], expanded[right]

    res = 0
    for i, x in enumerate(expanded):
        if x == -1:
            continue
        else:
            res += i * x

    return res


def expand2(data):
    res = []
    idx = 0
    for i in range(len(data)):
        if i % 2 == 0:
            res.append([idx, data[i]])
            idx += 1
        else:
            res.append([-1, data[i]])
    return res, idx


def solve_day_09_p2(data):
    expanded, max_id = expand2(data)
    res = 0
    left = 0
    right = len(expanded) - 1

    done = [False] * max_id

    for right in range(len(expanded) - 1, -1, -1):
        if expanded[right][0] != -1:
            done[expanded[right][0]] = True
            for i in range(0, right):
                if expanded[i][0] == -1:
                    if expanded[i][1] >= expanded[right][1]:
                        expanded[i][0] = expanded[right][0]
                        delta = expanded[i][1] - expanded[right][1]
                        expanded[i][1] = expanded[right][1]
                        expanded[right][0] = -1
                        if delta > 0:
                            expanded.insert(i + 1, [-1, delta])
                        break
    ext2 = []
    for i in range(len(expanded)):
        ext2 += [expanded[i][0]] * expanded[i][1]

    res = 0
    for i, x in enumerate(ext2):
        if x == -1:
            continue
        else:
            res += i * x
    return res


if __name__ == "__main__":
    # print(solve_day_09_p1(read_input("2024/day_09_large.txt")))
    print(solve_day_09_p2(read_input("2024/day_09_large.txt")))
