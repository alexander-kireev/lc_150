def canPartition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False

    subset_sums = {0}
    target = total / 2

    for num in nums:
        new_sums = set()

        for s in subset_sums:
            if num + s == target:
                return True

            if num + s < target:
                new_sums.add(num + s)

        subset_sums = subset_sums.union(new_sums)

    return False

tests = [
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