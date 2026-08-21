def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_dict = {}

    for char in s1:
        if char in s1_dict:
            s1_dict[char] += 1
        else:
            s1_dict[char] = 1

    last_possible_left = len(s2) - len(s1)
    window = {}
    left = 0 
    right = 0 

    for _ in range(len(s1)):
        if s2[right] in window:
            window[s2[right]] += 1
        else:
            window[s2[right]] = 1

        right += 1

    while left <= last_possible_left:
        if s1_dict == window:
            return True

        window[s2[left]] -= 1
        if window[s2[left]] == 0:
            window.pop(s2[left])

        if right < len(s2):
            if s2[right] in window:
                window[s2[right]] += 1
            else:
                window[s2[right]] = 1

        right += 1
        left += 1

    return False



tests = [
    ("ab", "eidbaooo"),      # True
    ("ab", "eidboaoo"),      # False
    ("adc", "dcda"),         # True
    ("a", "a"),              # True
    ("a", "b"),              # False
    ("abc", "bbbca"),        # True
    ("abc", "ccccbbbbaaaa"), # False
    ("hello", "ooolleoooleh"), # False
    ("aa", "eidbaaooo"),     # True
    ("aa", "eidabaooo"),     # False
    ("abcd", "abc"),         # False
    ("xyz", "afdgzyxksldfm"), # True
]

for s1, s2 in tests:
    result = checkInclusion(s1, s2)
    print(f"s1={s1!r}, s2={s2!r} -> {result}")