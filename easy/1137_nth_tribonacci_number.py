def tribonacci(n):

    memo = {0: 0, 1: 1, 2: 1}

    def trib(n):
        if n in memo:
            return memo[n]

        val = trib(n - 1) + trib(n - 2) + trib(n - 3)
        memo[n] = val
        return val

    return trib(n)

# def tribonacci(n):

#     p1 = 1
#     p2 = 1
#     p3 = 0

#     if n == 0:
#         return p3

#     for i in range(3, n + 1):
#         cur = p1 + p2 + p3
#         p3 = p2
#         p2 = p1
#         p1 = cur

#     return p1

    

    

tests = [
    (0, 0),
    (1, 1),
    (2, 1),

    (3, 2),
    (4, 4),
    (5, 7),
    (6, 13),

    (10, 149),
    (15, 3136),
    (20, 66012),

    (25, 1389537),

    (30, 29249425),
    (37, 2082876103),
]


for n, expected in tests:
    result = tribonacci(n)

    print(f"n={n}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()