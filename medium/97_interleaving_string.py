def isInterleave(s1, s2, s3):
    pass

tests = [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True),

    ("a", "", "a", True),
    ("", "b", "b", True),
    ("a", "b", "ab", True),
    ("a", "b", "ba", True),
    ("a", "b", "aa", False),

    ("abc", "def", "adbcef", True),
    ("abc", "def", "abdecf", True),
    ("abc", "def", "abcdef", True),
    ("abc", "def", "abdfec", False),

    ("aa", "ab", "aaba", True),
    ("aa", "ab", "abaa", True),

    ("abc", "abc", "aabbcc", True),

    ("abc", "def", "abcd", False),

    ("bbbb", "bbbb", "bbbbbbbb", True),

    ("db", "b", "cbb", False),
]


for s1, s2, s3, expected in tests:
    result = isInterleave(s1, s2, s3)

    print(f"s1={s1!r}, s2={s2!r}, s3={s3!r}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()