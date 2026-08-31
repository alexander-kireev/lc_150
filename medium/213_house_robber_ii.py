def rob(nums):
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    prev = nums[0]
    prev_prev = 0

    for i in range(1, len(nums) - 1):
        cur = max(prev, prev_prev + nums[i])
        prev_prev = prev
        prev = cur

    first_pass = prev

    prev = nums[1]
    prev_prev = 0

    for i in range(2, len(nums)):
        cur = max(prev, prev_prev + nums[i])
        prev_prev = prev
        prev = cur

    second_pass = prev

    return max(first_pass, second_pass)

tests = [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),

    ([1], 1),
    ([0], 0),
    ([5, 1], 5),

    ([1, 2, 1, 1], 3),
    ([2, 7, 9, 3, 1], 11),
    ([4, 1, 2, 7, 5, 3, 1], 14),

    ([10, 1, 1, 10], 11),
    ([100, 1, 1, 100, 1], 101),

    ([0, 0, 0, 0], 0),
    ([1, 1, 1, 1, 1], 2),
]


for nums, expected in tests:
    result = rob(nums)

    print(f"nums={nums}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()