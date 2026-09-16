def maximumSubarraySum(nums, k):

    max_sum = 0
    cur_sum = 0
    counts = {}
    left = 0
    n = len(nums)

    for right in range(n):
        counts[nums[right]] = counts.get(nums[right], 0) + 1
        cur_sum += nums[right]

        if (right - left) + 1 > k:
            counts[nums[left]] -= 1
            cur_sum -= nums[left]
            left += 1
        
        while counts[nums[right]] > 1:
            counts[nums[left]] -= 1
            cur_sum -= nums[left]
            left += 1

        if (right - left) + 1 == k:
            max_sum = max(max_sum, cur_sum)

    return max_sum


tests = [
    ([1, 5, 4, 2, 9, 9, 9], 3, 15),
    ([4, 4, 4], 3, 0),

    ([1], 1, 1),
    ([5, 1, 2], 1, 5),

    ([1, 2, 3, 4], 2, 7),
    ([1, 2, 3, 4], 4, 10),

    ([1, 2, 1, 3, 4], 3, 8),
    ([5, 5, 1, 2, 3], 3, 6),

    ([9, 1, 2, 3, 9], 3, 14),

    ([1, 1, 2, 3, 4, 4, 5], 3, 9),

    ([10, 20, 10, 30, 40], 3, 80),

    ([2, 3, 4, 5, 2, 6], 4, 17),

    ([7, 7, 8, 9], 2, 17),

    ([1, 2, 2, 3, 4], 3, 9),
]


for nums, k, expected in tests:
    result = maximumSubarraySum(nums, k)

    print(f"nums={nums}, k={k}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()