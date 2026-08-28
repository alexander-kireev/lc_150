def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    subarrays = 0
    n = len(nums)
    cur_total = 1
    left = 0

    for right in range(n):
        cur_total *= nums[right]

        while cur_total >= k:
            cur_total //= nums[left]
            left += 1

        subarrays += right - left + 1
        
    return subarrays

tests = [
    ([10, 5, 2, 6], 100, 8),
    ([1, 2, 3], 0, 0),
    ([1, 1, 1], 2, 6),
    ([1, 2, 3], 7, 6),
    ([1, 2, 3], 6, 5),
    ([10], 10, 0),
    ([10], 11, 1),
    ([2, 5, 3, 10], 30, 6),
    ([1, 2, 1, 2], 3, 7),
    ([5, 1, 1, 1], 5, 6),
    ([1], 1, 0),
    ([1], 2, 1),
]

for nums, k, expected in tests:
    result = numSubarrayProductLessThanK(nums, k)
    print(
        f"nums={nums}, k={k} -> {result} "
        f"(expected {expected})"
    )