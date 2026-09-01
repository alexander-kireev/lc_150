def combinationSum(candidates, target):
    nums = candidates
    res = []

    def dfs(sol, i, cur_sum):
        if cur_sum == target:
            res.append(sol.copy())
            return

        if i >= len(nums):
            return

        if cur_sum > target:
            return
        
        # take
        sol.append(nums[i])
        dfs(sol, i, cur_sum + nums[i])
        sol.pop()

        # skip
        dfs(sol, i + 1, cur_sum)
    

    dfs([], 0, 0)
    return res

tests = [
    ([2, 3, 6, 7], 7, [
        [2, 2, 3],
        [7],
    ]),

    ([2, 3, 5], 8, [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5],
    ]),

    ([2], 1, []),

    ([2], 8, [
        [2, 2, 2, 2],
    ]),

    ([3, 4, 5], 9, [
        [3, 3, 3],
        [4, 5],
    ]),

    ([2, 4, 6], 6, [
        [2, 2, 2],
        [2, 4],
        [6],
    ]),

    ([5, 10], 20, [
        [5, 5, 5, 5],
        [5, 5, 10],
        [10, 10],
    ]),

    ([7, 3, 2], 7, [
        [2, 2, 3],
        [7],
    ]),

    ([8, 9, 10], 7, []),

    ([2, 3, 7], 12, [
        [2, 2, 2, 2, 2, 2],
        [2, 2, 2, 3, 3],
        [2, 3, 7],
        [3, 3, 3, 3],
    ]),
]


for candidates, target, expected in tests:
    result = combinationSum(candidates, target)

    # Sort inner lists and then outer list so output order doesn't matter
    result_sorted = sorted(tuple(sorted(x)) for x in result)
    expected_sorted = sorted(tuple(sorted(x)) for x in expected)

    print(f"candidates={candidates}, target={target}")
    print("result:", result)
    print("correct:", result_sorted == expected_sorted)
    print("expected:", expected)
    print()