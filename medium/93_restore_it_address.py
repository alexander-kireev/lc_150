def restoreIpAddresses(s):
    res = []

    if len(s) < 4 or len(s) > 12:
        return res


    def dfs(new_s, i, dots):
        remainder_string = new_s[i:]
        remainder_int = int(new_s[i:])
        
        if dots == 3:
        
            if (
                1 <= len(remainder_string) <= 3 and 
                0 <= remainder_int <= 255 and
                (remainder_string[0] != "0" or remainder_string == "0")):
                res.append(new_s)
                return
            else:
                return
            
        for j in range(1, 4):
            front = new_s[:i + j]
            back = new_s[i + j:]
            part = new_s[i:i + j]
            
            if not back or not front:
                break

            if part[0] == "0" and len(part) > 1:
                continue

            if int(part) > 255:
                continue

            dfs(front + "." + back, i + j + 1, dots + 1)
        

    dfs(s, 0, 0)
    return res


tests = [
    ("0000", [
        "0.0.0.0",
    ]),

    ("25525511135", [
        "255.255.11.135",
        "255.255.111.35",
    ]),

    ("0000", [
        "0.0.0.0",
    ]),

    ("101023", [
        "1.0.10.23",
        "1.0.102.3",
        "10.1.0.23",
        "10.10.2.3",
        "101.0.2.3",
    ]),

    ("1111", [
        "1.1.1.1",
    ]),

    ("010010", [
        "0.10.0.10",
        "0.100.1.0",
    ]),

    ("255255255255", [
        "255.255.255.255",
    ]),

    ("256256256256", []),

    ("123", []),

    ("1234567890123", []),

    ("9999", [
        "9.9.9.9",
    ]),
]


for s, expected in tests:
    result = restoreIpAddresses(s)

    print(f"s={s!r}")
    print("result:", result)
    print("correct:", sorted(result) == sorted(expected))
    print("expected:", expected)
    print()