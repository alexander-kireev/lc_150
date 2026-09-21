def lemonadeChange(bills):
    till = {
        5: {
            "change": 0,
            "have": 0,
        },
        10: {
            "change": 5,
            "have": 0,
        },
        20: {
            "change": 15,
            "have": 0,
        },
    }

    for bill in bills:

        till[bill]["have"] += 1
        change = till[bill]["change"]

        while change >= 15 and till[10]["have"] > 0:
            change -= 10
            till[10]["have"] -= 1

        while change >= 5 and till[5]["have"] > 0:
            change -= 5
            till[5]["have"] -= 1

        if change > 0:
            return False

    return True



tests = [
    ([5, 5, 5, 10, 20], True),
    ([5, 5, 10, 10, 20], False),

    ([5], True),
    ([10], False),
    ([20], False),

    ([5, 10], True),
    ([5, 20], False),

    ([5, 5, 10], True),
    ([5, 5, 20], False),

    ([5, 5, 5, 20], True),
    ([5, 5, 5, 10, 10, 20], True),

    ([5, 5, 10, 20], True),
    ([5, 10, 5, 20], True),

    ([5, 5, 10, 10, 5, 20, 20], False),

    ([5, 5, 5, 5, 10, 20, 10, 20], True),
]


for bills, expected in tests:
    result = lemonadeChange(bills)

    print(f"bills={bills}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()