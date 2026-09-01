def generateParenthesis(n):
    res = []

    def dfs(opened, closed, sol):
        if opened > n or closed > n:
            return

        if opened == n and closed == n:
            res.append(sol)
            return
        
        if closed > opened:
            return

        dfs(opened + 1, closed, sol + "(")
        
        dfs(opened, closed + 1, sol + ")")


    dfs(0, 0, "")
    return res

tests = [
    (1, [
        "()"
    ]),

    (2, [
        "(())",
        "()()"
    ]),

    (3, [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]),

    (4, None),   # expected count: 14
    (5, None),   # expected count: 42
]


for n, expected in tests:
    result = generateParenthesis(n)

    print(f"n={n}")
    print("result:", result)

    if expected is not None:
        print("correct:", sorted(result) == sorted(expected))
    else:
        expected_count = 14 if n == 4 else 42
        print("number of combinations:", len(result), f"(expected {expected_count})")

    print()