def longestCommonSubsequence(text1, text2):
    grid = []

    for _ in range(len(text1)):
        grid.append([0] * len(text2))


    for i in range(len(text1)):

        for j in range(len(text2)):

            if text1[i] == text2[j]:

                if i == 0 and j == 0:
                    grid[i][j] = 1
                elif i == 0:
                    grid[i][j] = 1
                elif j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i - 1][j - 1] + 1


            else:

                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    grid[i][j] = grid[i][j - 1]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j]
                else:
                    grid[i][j] = max(grid[i][j - 1], grid[i - 1][j])
                

    return grid[-1][-1]

tests = [
    # ("abcde", "ace", 3),
    # ("abc", "abc", 3),
    # ("abc", "def", 0),

    # ("a", "a", 1),
    # ("a", "b", 0),

    # ("abc", "ac", 2),
    # ("abc", "bac", 2),

    ("aaaa", "aa", 2),

    ("abcba", "abcbcba", 5),

    ("bl", "yby", 1),

    ("abcbdab", "bdcaba", 4),

    ("AGGTAB", "GXTXAYB", 4),

    ("ezupkr", "ubmrapg", 2),

    ("oxcpqrsvwf", "shmtulqrypy", 2),
]


for text1, text2, expected in tests:
    result = longestCommonSubsequence(text1, text2)

    print(f"text1={text1!r}, text2={text2!r}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()