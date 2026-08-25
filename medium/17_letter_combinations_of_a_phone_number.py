def letterCombinations(digits):
    res = []
    n = len(digits)

    mappings = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }


    def dfs(sol, digit):

        if len(sol) == n:
            res.append(sol)
            return
        
        for char in mappings[digits[digit]]:
            dfs(sol + char, digit + 1)


    dfs("", 0)
    return res


tests = [
    ("23", [
        "ad", "ae", "af",
        "bd", "be", "bf",
        "cd", "ce", "cf",
    ]),

    ("2", [
        "a", "b", "c",
    ]),

    ("7", [
        "p", "q", "r", "s",
    ]),

    ("9", [
        "w", "x", "y", "z",
    ]),

    ("27", [
        "ap", "aq", "ar", "as",
        "bp", "bq", "br", "bs",
        "cp", "cq", "cr", "cs",
    ]),

    ("79", None),   # expected count: 16
    ("234", None),  # expected count: 27
]


for digits, expected in tests:
    result = letterCombinations(digits)

    print(f"digits={digits!r}")
    print("result:", result)

    if expected is not None:
        print("correct:", sorted(result) == sorted(expected))
    else:
        expected_count = 16 if digits == "79" else 27
        print("number of combinations:", len(result), f"(expected {expected_count})")

    print()