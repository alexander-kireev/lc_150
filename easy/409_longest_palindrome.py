def longestPalindrome(s):
    counts = {}

    for c in s:
        counts[c] = counts.get(c, 0) + 1

    max_len = 0

    for c, i in counts.items():
        if i % 2 == 0:
            max_len += i
        else:
            if max_len % 2 == 0:
                max_len += i
            else:
                max_len += i - 1

    return max_len


tests = [
    ("bananas", 5),
    ("abccccdd", 7),
    ("a", 1),

    ("aa", 2),
    ("ab", 1),
    ("abc", 1),

    ("aabb", 4),
    ("aabbc", 5),

    ("aaaa", 4),
    ("aaaaa", 5),

    ("Aa", 1),
    ("AaAa", 4),

    ("abccccdd", 7),

    ("bananas", 5),

    ("aabbccddeeff", 12),
    ("aabbccddeeffg", 13),

    ("zzzzZZ", 6),
]


for s, expected in tests:
    result = longestPalindrome(s)

    print(f"s={s!r}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()