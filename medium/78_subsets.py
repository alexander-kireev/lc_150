def subsets(nums):
    res, sol = [], []
    n = len(nums)

    def dfs(i):

        if i == n:
            res.append(sol.copy())
            return

        # don't take
        dfs(i + 1)

        sol.append(nums[i])
        dfs(i + 1)
        sol.pop()

    dfs(0)
    return res


tests = [
    ([1, 2, 3], [
        [],
        [1], [2], [3],
        [1, 2], [1, 3], [2, 3],
        [1, 2, 3]
    ]),

    ([0], [
        [],
        [0]
    ]),

    ([1, 2], [
        [],
        [1], [2],
        [1, 2]
    ]),

    ([-1, 2], [
        [],
        [-1], [2],
        [-1, 2]
    ]),

    ([1, 2, 3, 4], None),  # should contain 16 subsets
]


for nums, expected in tests:
    result = subsets(nums)

    print(f"nums={nums}")
    print("result:", result)

    if expected is not None:
        result_sorted = sorted([sorted(x) for x in result])
        expected_sorted = sorted([sorted(x) for x in expected])

        print("correct:", result_sorted == expected_sorted)
    else:
        print("number of subsets:", len(result), "(expected 16)")

    print()