def balancedStringSplit(s):
    strings = 0
    balance = 0

    for c in s:
        if c == "R":
            balance += 1
        else:
            balance -= 1

        if balance == 0:
            strings += 1

    return strings

tests = [
    ("RLRRLLRLRL", 4),
    ("RLRRRLLRLL", 2),
    ("LLLLRRRR", 1),

    ("LR", 1),
    ("RL", 1),

    ("LRLR", 2),
    ("RLRL", 2),

    ("LLRR", 1),
    ("RRLL", 1),

    ("LRRLLR", 2),

    ("RLLR", 2),

    ("LLRRLRRL", 3),

    ("RRRLLLRLRL", 3),
]


for s, expected in tests:
    result = balancedStringSplit(s)

    print(f"s={s!r}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()