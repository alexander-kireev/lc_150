def validPalindrome(s):

    left = 0
    right = len(s) - 1
    lives = 1

    while left <= right:

        if s[left] != s[right]:

            if lives == 0:
                return False

            # try move left
            og_left = left
            og_right = right

            left += 1
            while left <= right:
                if s[left] != s[right]:
                    break
                else:
                    left += 1
                    right -= 1

            if left > right:
                return True

            # try move right
            left = og_left
            right = og_right
            right -= 1

            while left <= right:
                if s[left] != s[right]:
                    break
                else:
                    left += 1
                    right -= 1

            return left > right

        left += 1
        right -= 1

    return True


tests = [
    # ("aba", True),
    # ("abca", True),
    # ("abc", False),

    # ("a", True),
    # ("aa", True),
    # ("ab", True),

    # ("deeee", True),
    # ("cbbcc", True),

    # ("raceacar", True),
    # ("raceabcar", False),


    ("axbcbaba", False),
    ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True),

    ("abcdefedcba", True),
    ("abcdefgfedcba", True),

    ("abcddcba", True),
    ("abcdecba", True),
    ("abecbea", False),
]


for s, expected in tests:
    result = validPalindrome(s)

    print(f"s={s!r}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()