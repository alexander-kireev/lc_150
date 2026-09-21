def arrayPairSum(nums):
    nums.sort()
    total = 0

    for i in range(0, len(nums), 2):
        total += min(nums[i], nums[i + 1])

    return total


tests = [
    ([1, 4, 3, 2], 4),
    ([6, 2, 6, 5, 1, 2], 9),

    ([1, 2], 1),
    ([5, 5], 5),

    ([1, 1, 1, 1], 2),
    ([1, 2, 3, 4, 5, 6], 9),

    ([-1, -2], -2),
    ([-4, -3, -2, -1], -6),

    ([-1, 0, 1, 2], 0),

    ([10, 1, 9, 2, 8, 3], 12),

    ([7, 3, 1, 0, 0, 6], 7),
]


for nums, expected in tests:
    result = arrayPairSum(nums)

    print(f"nums={nums}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()