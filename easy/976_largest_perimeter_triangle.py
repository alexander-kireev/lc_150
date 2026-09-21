def largestPerimeter(nums):
    nums.sort()
    max_p = 0

    def is_triangle(a, b, c):
        return a + b > c and a + c > b and c + b > a

    for i in range(len(nums) - 1, 1, -1):
        if is_triangle(nums[i], nums[i - 1], nums[i - 2]):
            return nums[i] + nums[i - 1] + nums[i - 2]

    return max_p


tests = [
    ([2, 1, 2], 5),
    ([1, 2, 1, 10], 0),

    ([3, 6, 2, 3], 8),
    ([3, 2, 3, 4], 10),

    ([1, 1, 1], 3),
    ([1, 1, 2], 0),

    ([5, 5, 10], 0),
    ([5, 5, 9], 19),

    ([2, 3, 4, 5], 12),

    ([10, 2, 5, 1, 8, 20], 23),

    ([100, 100, 100], 300),

    ([1, 2, 3, 4, 5, 10], 12),
]


for nums, expected in tests:
    result = largestPerimeter(nums)

    print(f"nums={nums}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()