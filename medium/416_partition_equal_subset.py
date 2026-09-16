def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total / 2

    reachable = {0}

    for num in nums:
        new_sums = set()

        for s in reachable:
            new_sum = s + num

            if new_sum == target:
                return True

            if new_sum < target:
                new_sums.add(new_sum)

        reachable = reachable.union(new_sums)

    return False

tests = [
    ([3,3,6,8,16,16,16,18,20], True),
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),

    ([1], False),
    ([2, 2], True),

    ([1, 1, 1, 1], True),
    ([1, 1, 1], False),

    ([2, 3, 5], True),
    ([2, 3, 7], False),

    ([3, 3, 3, 4, 5], True),

    ([1, 2, 5], False),

    ([100, 100], True),

    ([1, 2, 3, 4, 5, 6, 7], True),

    ([2, 2, 3, 5], False),

    ([14, 9, 8, 4, 3, 2], True),
]


for nums, expected in tests:
    result = canPartition(nums)

    print(f"nums={nums}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()