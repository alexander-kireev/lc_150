def findContentChildren(g, s):
    max_children = 0
    g.sort()
    s.sort()

    children = len(g)
    cookies = len(s)

    j = 0

    for i in range(children):

        while j < cookies and s[j] < g[i]:
            j += 1

        if j >= cookies:
            return max_children

        if s[j] >= g[i]:
            max_children += 1
            j += 1

    return max_children

tests = [
    ([1, 2, 3], [1, 1], 1),
    ([1, 2], [1, 2, 3], 2),

    ([1], [], 0),
    ([1], [1], 1),
    ([2], [1], 0),

    ([1, 1, 1], [1, 1], 2),
    ([2, 3, 4], [1, 2, 3], 2),

    ([1, 2, 3], [3], 1),
    ([1, 2, 3], [3, 3, 3], 3),

    ([5, 10, 15], [1, 2, 3, 20], 1),

    ([10, 9, 8, 7], [5, 6, 7, 8], 2),

    ([1, 2, 2, 3], [1, 2, 3, 3], 4),
]


for g, s, expected in tests:
    result = findContentChildren(g, s)

    print(f"g={g}, s={s}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()