def permute(nums):
    res = []
    avail = set(nums)

    def dfs(avail, sol):
        if not avail:
            res.append(sol)
            return
        
        for num in avail:
            dfs(avail - {num}, sol + [num])
            
    dfs(avail, [])
    return res


tests = [
    ([1, 2, 3], [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]),

    ([0, 1], [
        [0, 1],
        [1, 0],
    ]),

    ([1], [
        [1],
    ]),

    ([1, 2], [
        [1, 2],
        [2, 1],
    ]),

    ([-1, 0, 2], [
        [-1, 0, 2],
        [-1, 2, 0],
        [0, -1, 2],
        [0, 2, -1],
        [2, -1, 0],
        [2, 0, -1],
    ]),

    ([1, 2, 3, 4], None),  # expected count: 24
]


for nums, expected in tests:
    result = permute(nums)

    print(f"nums={nums}")
    print("result:", result)

    if expected is not None:
        result_sorted = sorted(tuple(x) for x in result)
        expected_sorted = sorted(tuple(x) for x in expected)
        print("correct:", result_sorted == expected_sorted)
    else:
        print("number of permutations:", len(result), "(expected 24)")

    print()