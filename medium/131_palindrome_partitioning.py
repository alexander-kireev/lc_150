def partition(s):
    pass


tests = [
    ("aab", [
        ["a", "a", "b"],
        ["aa", "b"],
    ]),

    ("a", [
        ["a"],
    ]),

    ("aa", [
        ["a", "a"],
        ["aa"],
    ]),

    ("aba", [
        ["a", "b", "a"],
        ["aba"],
    ]),

    ("abba", [
        ["a", "b", "b", "a"],
        ["a", "bb", "a"],
        ["abba"],
    ]),

    ("aaa", [
        ["a", "a", "a"],
        ["a", "aa"],
        ["aa", "a"],
        ["aaa"],
    ]),

    ("abc", [
        ["a", "b", "c"],
    ]),

    ("aabaa", None),  # multiple valid partitions; just inspect/count
]


for s, expected in tests:
    result = partition(s)
    print(result)

    print(f"s={s!r}")
    print("result:", result)

    if expected is not None:
        result_sorted = sorted(tuple(x) for x in result)
        expected_sorted = sorted(tuple(x) for x in expected)
        print("correct:", result_sorted == expected_sorted)
    else:
        print("number of partitions:", len(result))

    print()