def lengthOfLIS(nums):

    longest = 1
    lis = [1] * len(nums)

    for i in range(1, len(nums)):
        j = 0

        while j < i:
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)
            j += 1

        longest = max(longest, lis[i])

    return longest


tests = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),

    ([1], 1),
    ([1, 2, 3, 4, 5], 5),
    ([5, 4, 3, 2, 1], 1),

    ([3, 1, 2], 2),
    ([4, 10, 4, 3, 8, 9], 3),

    ([2, 2, 2, 3, 4], 3),
    ([-5, -4, -3, -2, -1], 5),

    ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
]


for nums, expected in tests:
    result = lengthOfLIS(nums)

    print(f"nums={nums}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()