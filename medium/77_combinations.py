def combine(n, k):
    res, sol = [], []
    nums = list(range(1, n + 1))
    calls = 0

    def dfs(i):
        nonlocal calls
        calls += 1
        if len(sol) == k:
            res.append(sol.copy())
            return

        if i >= len(nums):
            return

        max_len = len(sol) + (n - i)
        if max_len < k:
            return

        # take
        sol.append(nums[i])
        dfs(i + 1)
        sol.pop()

        # skip
        dfs(i + 1)

    dfs(0)
    print(calls)
    return res


tests = [
    (4, 2, [
        [1, 2], [1, 3], [1, 4],
        [2, 3], [2, 4],
        [3, 4]
    ]),

    (1, 1, [
        [1]
    ]),

    (5, 3, [
        [1, 2, 3], [1, 2, 4], [1, 2, 5],
        [1, 3, 4], [1, 3, 5], [1, 4, 5],
        [2, 3, 4], [2, 3, 5], [2, 4, 5],
        [3, 4, 5]
    ]),

    (5, 1, [
        [1], [2], [3], [4], [5]
    ]),

    (5, 5, [
        [1, 2, 3, 4, 5]
    ]),

    (6, 2, None),   # expected number of combinations: 15
]


for n, k, expected in tests:
    result = combine(n, k)

    print(f"n={n}, k={k}")
    print("result:", result)

    if expected is not None:
        result_sorted = sorted([tuple(x) for x in result])
        expected_sorted = sorted([tuple(x) for x in expected])

        print("correct:", result_sorted == expected_sorted)
    else:
        print("number of combinations:", len(result), "(expected 15)")

    print()