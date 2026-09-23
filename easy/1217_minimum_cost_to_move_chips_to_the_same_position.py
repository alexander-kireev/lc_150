def minCostToMoveChips(position):
    odd = 0
    even = 0

    for num in position:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return min(odd, even)


tests = [
    ([1, 2, 3], 1),
    ([2, 2, 2, 3, 3], 2),
    ([1, 1000000000], 1),

    ([1], 0),
    ([2, 4, 6], 0),
    ([1, 3, 5], 0),

    ([1, 2], 1),
    ([2, 3], 1),

    ([1, 1, 2, 2], 2),
    ([1, 1, 1, 2], 1),

    ([1, 2, 3, 4], 2),

    ([10, 20, 30, 40], 0),

    ([1, 100, 101, 200], 2),
]


for position, expected in tests:
    result = minCostToMoveChips(position)

    print(f"position={position}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()