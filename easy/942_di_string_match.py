def diStringMatch(s):
    smallest = 0
    largest = len(s)

    perm = []

    for i in range(len(s)):

        if s[i] == "I":
            perm.append(smallest)
            smallest += 1
        else:
            perm.append(largest)
            largest -= 1

    perm.append(smallest)

    return perm

tests = [
    ("IDID", [0, 4, 1, 3, 2]),
    ("III", [0, 1, 2, 3]),
    ("DDI", [3, 2, 0, 1]),

    ("I", [0, 1]),
    ("D", [1, 0]),

    ("IIID", [0, 1, 2, 4, 3]),
    ("DDDI", [4, 3, 2, 0, 1]),

    ("IIII", [0, 1, 2, 3, 4]),
    ("DDDD", [4, 3, 2, 1, 0]),

    ("DIDI", [4, 0, 3, 1, 2]),
]


def is_valid(s, perm):
    if len(perm) != len(s) + 1:
        return False

    if sorted(perm) != list(range(len(s) + 1)):
        return False

    for i, ch in enumerate(s):
        if ch == "I" and not (perm[i] < perm[i + 1]):
            return False
        if ch == "D" and not (perm[i] > perm[i + 1]):
            return False

    return True


for s, example_expected in tests:
    result = diStringMatch(s)

    print(f"s={s!r}")
    print("result:", result)
    print("example valid output:", example_expected)
    print("correct:", is_valid(s, result))
    print()