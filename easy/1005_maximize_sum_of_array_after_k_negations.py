def largestSumAfterKNegations(nums, k):
    n = len(nums)
    nums.sort()
    pointer = 0

    for _ in range(k):

        nums[pointer] = -nums[pointer]

        if pointer + 1 < n and nums[pointer + 1] < nums[pointer]:
            pointer += 1

    return sum(nums)

tests = [
    # ([4, 2, 3], 1, 5),
    # ([3, -1, 0, 2], 3, 6),
    ([8,-7,-3,-9,1,9,-6,-9,3], 8, 53),
    ([2, -3, -1, 5, -4], 2, 13),

    ([1], 1, -1),
    ([-1], 1, 1),
    ([0], 5, 0),

    ([-5, -2, -3], 2, 6),
    ([-5, -2, -3], 3, 10),

    ([1, 2, 3], 2, 6),
    ([1, 2, 3], 3, 4),

    ([-4, -2, 3, 5], 1, 14),
    ([-4, -2, 3, 5], 2, 14),
    ([-4, -2, 3, 5], 3, 10),

    ([-2, 0, 5], 100, 7),

    ([-8, -3, -1, 2, 4], 4, 16),
]


for nums, k, expected in tests:
    result = largestSumAfterKNegations(nums.copy(), k)

    print(f"nums={nums}, k={k}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()