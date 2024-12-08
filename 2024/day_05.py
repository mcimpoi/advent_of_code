def parse_input(input_text):
    lines = input_text.splitlines()
    rules = [x for x in lines if "|" in x]
    updates = [x for x in lines if "," in x]

    ret_rules = []
    for rule in rules:
        ret_rules.append([int(x) for x in rule.split("|")])
    ret_updates = []
    for update in updates:
        ret_updates.append([int(x) for x in update.split(",")])
    return ret_rules, ret_updates


def solve_p1(rules, updates):
    res = 0
    for upd in updates:
        correct = True
        for idx1, x in enumerate(upd):
            for idx2, y in enumerate(upd):
                if x == y:
                    continue
                if idx1 < idx2 and [y, x] in rules:
                    correct = False
                    break
                if idx1 > idx2 and [x, y] in rules:
                    correct = False
                    break
        if correct:
            res += upd[len(upd) // 2]

    print(res)


def is_correct(update, rules):
    for idx1, x in enumerate(update):
        for idx2, y in enumerate(update):
            if x == y:
                continue
            if idx1 < idx2 and [y, x] in rules:
                return False, idx1, idx2

            if idx1 > idx2 and [x, y] in rules:
                return False, idx1, idx2
    return True, -1, -1


def solve2(rules, updates):
    res = 0
    to_fix = []
    for upd in updates:
        if not is_correct(upd, rules)[0]:
            to_fix.append(upd)

    for upd in to_fix:
        # print(upd)
        correct = False
        while not correct:
            correct, idx1, idx2 = is_correct(upd, rules)
            if not correct:
                upd[idx1], upd[idx2] = upd[idx2], upd[idx1]

        res += upd[len(upd) // 2]

    print(res)


if __name__ == "__main__":
    input_text = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    rules, updates = parse_input(input_text)
    solve_p1(rules, updates)
    solve2(rules, updates)
