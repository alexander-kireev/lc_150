def numDecodings(s):
    pass


tests = [
    ("12", 2),
    ("226", 3),
    ("06", 0),

    ("1", 1),
    ("9", 1),
    ("0", 0),

    ("10", 1),
    ("20", 1),
    ("30", 0),

    ("101", 1),
    ("110", 1),
    ("100", 0),

    ("27", 1),
    ("26", 2),

    ("111", 3),
    ("1111", 5),

    ("2101", 1),
    ("1201234", 3),
    ("2611055971756562", 4),
]


for s, expected in tests:
    result = numDecodings(s)

    print(f"s={s!r}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()