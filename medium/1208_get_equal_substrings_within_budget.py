def equalSubstring(s, t, maxCost):

    differences = [0] * len(s)

    for i in range(len(s)):
        differences[i] = abs(ord(s[i]) - ord(t[i]))

    left = 0
    longest = 0
    cur_cost = 0

    for right in range(len(differences)):

        cur_cost += differences[right]

        while cur_cost > maxCost:
            cur_cost -= differences[left]
            left += 1

        longest = max(longest, (right - left) + 1)

    return longest

tests = [
    ("abcd", "bcdf", 3, 3),
    ("abcd", "cdef", 3, 1),
    ("abcd", "acde", 0, 1),

    ("a", "a", 0, 1),
    ("a", "z", 0, 0),
    ("a", "z", 25, 1),

    ("abcd", "abcd", 0, 4),
    ("abcd", "abcd", 10, 4),

    ("abcd", "bcde", 4, 4),
    ("abcd", "bcde", 2, 2),

    ("aaaa", "zzzz", 24, 0),
    ("aaaa", "zzzz", 25, 1),
    ("aaaa", "zzzz", 50, 2),

    ("krrgw", "zjxss", 19, 2),

    ("pxezla", "loewbi", 25, 4),

    ("abcdxyz", "bcdfxyz", 3, 5),
]


for s, t, maxCost, expected in tests:
    result = equalSubstring(s, t, maxCost)

    print(f"s={s!r}, t={t!r}, maxCost={maxCost}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()