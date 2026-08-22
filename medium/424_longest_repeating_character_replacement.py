def characterReplacement(s, k):

    best = 0
    counts = {}
    max_freq = 0
    left = 0 
    right = 0

    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1
        max_freq = max(max_freq, counts[s[right]])

        while ((right - left) + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


tests = [
    ("ABAB", 2),          # 4
    ("AABABBA", 1),       # 4
    ("AAAA", 2),          # 4
    ("ABCDE", 1),         # 2
    ("BAAA", 0),          # 3
    ("ABBB", 2),          # 4
    ("ABAA", 0),          # 2
    ("AABA", 1),          # 4
    ("ABABBA", 1),        # 4
    ("ABCDEFF", 2),       # 3
    ("AAABBC", 2),        # 5
    ("A", 0),             # 1
    ("A", 1),             # 1
]

for s, k in tests:
    result = characterReplacement(s, k)
    print(f"s={s!r}, k={k} -> {result}")