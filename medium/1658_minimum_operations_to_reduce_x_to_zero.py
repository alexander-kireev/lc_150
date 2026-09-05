from math import inf

def minOperations(nums, x):
    total = sum(nums)

    n = len(nums)
    left = 0
    best = inf
    target = total - x

    cur = 0

    for right in range(n):

        cur += nums[right]

        while cur > target and left <= right:
            cur -= nums[left]
            left += 1

        if cur == target:
            best = min(best, n - ((right - left) + 1))

    if best == inf:
        return -1
    return best

tests = [
    ([1, 1, 4, 2, 3], 5, 2),
    ([5, 6, 7, 8, 9], 4, -1),
    ([3, 2, 20, 1, 1, 3], 10, 5),

    ([1], 1, 1),
    ([1], 2, -1),

    ([1, 2, 3], 6, 3),
    ([1, 2, 3], 3, 1),
    ([1, 2, 3], 4, 2),

    ([5, 1, 1, 1, 5], 10, 2),
    ([5, 1, 1, 1, 5], 7, 3),

    ([1, 1, 1, 1, 1], 3, 3),

    ([2, 3, 1, 1, 1], 5, 2),

    ([10, 1, 1, 1, 10], 20, 2),

    ([1, 2, 3, 4, 5], 10, 3),

    ([100, 1, 1, 1, 1, 100], 102, 3),
]


for nums, x, expected in tests:
    result = minOperations(nums, x)

    print(f"nums={nums}, x={x}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()