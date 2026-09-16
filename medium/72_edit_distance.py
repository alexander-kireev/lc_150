def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)

    grid = []

    for _ in range(m + 1):
        grid.append([0] * (n + 1))

    for i in range(1, n + 1):
        grid[0][i] = i

    for j in range(1, m + 1):
        grid[j][0] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # match
            c1 = word1[i - 1]
            c2 = word2[j - 1]
            if c1 == c2:
                grid[i][j] = grid[i - 1][j - 1]
            else:
                grid[i][j] = min(grid[i - 1][j - 1], grid[i][j - 1], grid[i - 1][j]) + 1

    return grid[-1][-1]

tests = [
    ("horse", "ros", 3),
    ("intention", "execution", 5),

    ("", "", 0),
    ("a", "", 1),
    ("", "a", 1),

    ("a", "a", 0),
    ("a", "b", 1),

    ("abc", "abc", 0),
    ("abc", "", 3),
    ("", "abc", 3),

    ("abc", "ab", 1),
    ("ab", "abc", 1),

    ("abc", "adc", 1),
    ("abc", "axc", 1),

    ("kitten", "sitting", 3),
    ("flaw", "lawn", 2),

    ("abcdef", "azced", 3),

    ("aaaa", "bbbb", 4),

    ("abcd", "acbd", 2),

    ("distance", "editing", 5),
]


for word1, word2, expected in tests:
    result = minDistance(word1, word2)

    print(f"word1={word1!r}, word2={word2!r}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()