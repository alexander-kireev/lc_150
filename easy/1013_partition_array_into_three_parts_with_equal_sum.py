def canThreePartsEqualSum(arr):
    buckets = 3
    total = sum(arr)

    if total % 3 != 0:
        return False

    step = total // 3
    target = step
    targets = []

    for _ in range(buckets):
        targets.append(target)
        target += step

    running_sum = 0
    index = 0

    for num in arr:
        running_sum += num

        if running_sum == targets[index]:
            index += 1

        if index == buckets:
            return True

    return False

tests = [
    ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], True),
    ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], False),
    ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4], True),

    ([1, 1, 1], True),
    ([1, 1, 2], False),

    ([0, 0, 0], True),
    ([0, 0, 0, 0], True),

    ([3, 3, 3, 3], False),

    ([1, -1, 1, -1, 1, -1], True),

    ([2, 2, 2, 2, 2, 2], True),

    ([1, 2, 3, 0, 3], True),

    ([-1, -1, -1], True),

    ([10, -10, 10, -10, 10, -10], True),
]


for arr, expected in tests:
    result = canThreePartsEqualSum(arr)

    print(f"arr={arr}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()