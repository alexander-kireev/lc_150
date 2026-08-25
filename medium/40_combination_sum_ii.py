def combinationSum2(candidates, target):
    res, sol = [], []
    n = len(candidates)
    candidates = sorted(candidates)

    def dfs(cur_sum, sol, i):
        if cur_sum == target:
            res.append(sol.copy())
            return

        if cur_sum > target or i >= n:
            return
    
        # take
        sol.append(candidates[i])
        dfs(cur_sum + candidates[i], sol, i + 1)
        sol.pop()

        # skip
        while i + 1 < n and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(cur_sum, sol, i + 1)


    dfs(0, sol, 0)
    return res

tests = [
    (
        [10, 1, 2, 7, 6, 1, 5],
        8,
        [
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6],
        ],
    ),

    (
        [2, 5, 2, 1, 2],
        5,
        [
            [1, 2, 2],
            [5],
        ],
    ),

    (
        [1, 1, 1, 2],
        3,
        [
            [1, 1, 1],
            [1, 2],
        ],
    ),

    (
        [1, 2, 3, 4, 5],
        5,
        [
            [1, 4],
            [2, 3],
            [5],
        ],
    ),

    (
        [2, 2, 2, 2],
        4,
        [
            [2, 2],
        ],
    ),

    (
        [3, 1, 3, 5, 1, 1],
        8,
        [
            [1, 1, 1, 5],
            [1, 1, 3, 3],
            [3, 5],
        ],
    ),

    (
        [4, 5, 6],
        3,
        [],
    ),

    (
        [1],
        1,
        [
            [1],
        ],
    ),

    (
        [1, 1],
        1,
        [
            [1],
        ],
    ),

    (
        [1, 1, 2, 2, 3],
        4,
        [
            [1, 1, 2],
            [1, 3],
            [2, 2],
        ],
    ),
]


for candidates, target, expected in tests:
    result = combinationSum2(candidates, target)

    result_sorted = sorted(tuple(sorted(x)) for x in result)
    expected_sorted = sorted(tuple(sorted(x)) for x in expected)

    print(f"candidates={candidates}, target={target}")
    print("result:", result)
    print("correct:", result_sorted == expected_sorted)
    print("expected:", expected)
    print()