def combinationSum3(k, n):
    res = []
    nums = list(range(1, 10))

    def dfs(sol, i, cur_sum):

        if len(sol) == k and cur_sum == n:
            res.append(sol)
            return
        
        if len(sol) > k or cur_sum > n or i >= len(nums):
            return
        
        # take
        dfs(sol + [nums[i]], i + 1, cur_sum + nums[i])

        # skip
        dfs(sol, i + 1, cur_sum)
    

    dfs([], 0, 0)
    return res


tests = [
    (3, 7, [
        [1, 2, 4],
    ]),

    (3, 9, [
        [1, 2, 6],
        [1, 3, 5],
        [2, 3, 4],
    ]),

    (4, 1, []),

    (3, 15, [
        [1, 5, 9],
        [1, 6, 8],
        [2, 4, 9],
        [2, 5, 8],
        [2, 6, 7],
        [3, 4, 8],
        [3, 5, 7],
        [4, 5, 6],
    ]),

    (2, 17, [
        [8, 9],
    ]),

    (2, 3, [
        [1, 2],
    ]),

    (9, 45, [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]),

    (3, 2, []),
]


for k, n, expected in tests:
    result = combinationSum3(k, n)

    result_sorted = sorted(tuple(x) for x in result)
    expected_sorted = sorted(tuple(x) for x in expected)

    print(f"k={k}, n={n}")
    print("result:", result)
    print("correct:", result_sorted == expected_sorted)
    print("expected:", expected)
    print()