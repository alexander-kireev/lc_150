def findAnagrams(s, p):
    output = []
    if len(p) > len(s):
        return []

    # turn p into dict char:count
    p_dict = {}
    for c in p:
        if c in p_dict:
            p_dict[c] += 1
        else:
            p_dict[c] = 1

    left = 0
    right = 0
    window = {}

    # get first window
    while right < len(p):
        if s[right] in window:
            window[s[right]] += 1
        else:
            window[s[right]] = 1

        right += 1

    # real slide
    while right <= len(s):

        # check if window is match
        if window == p_dict:
            output.append(left)

        # remove leftmost from window
        window[s[left]] -= 1
        if window[s[left]] == 0:
            window.pop(s[left])

        # if not out of bounds, add rightmost to window
        if right < len(s):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

        left += 1
        right += 1

    return output


tests = [
    ("cbaebabacd", "abc"),   # [0, 6]
    ("abab", "ab"),          # [0, 1, 2]
    ("abcdefg", "xyz"),      # []
    ("abc", "abc"),          # [0]
    ("aaaaa", "aa"),         # [0, 1, 2, 3]
    ("baa", "aa"),           # [1]
    ("abababab", "aab"),     # []
    ("abcba", "abc"),        # [0, 2]
    ("a", "a"),              # [0]
    ("a", "b"),              # []
    ("ab", "abc"),           # []
]

for s, p in tests:
    result = findAnagrams(s, p)
    print(f"s={s!r}, p={p!r} -> {result}")