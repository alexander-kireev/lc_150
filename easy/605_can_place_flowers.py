def canPlaceFlowers(flowerbed, n):
    pots = len(flowerbed)

    for i in range(pots):
        if n == 0:
            break

        if flowerbed[i] == 1:
            continue

        if i == 0:
            if pots == 1:
                flowerbed[i] = 1
                n -= 1
            elif flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        elif i == pots - 1:
            if flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
        else:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

    return n == 0




tests = [
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),

    ([0], 0, True),
    ([0], 1, True),
    ([1], 1, False),

    ([0, 0], 1, True),
    ([0, 0], 2, False),

    ([0, 0, 0], 2, True),
    ([0, 0, 0], 3, False),

    ([1, 0, 0, 0, 0, 1], 2, False),
    ([1, 0, 0, 0, 0, 0, 1], 2, True),

    ([0, 0, 1, 0, 0], 2, True),
    ([0, 1, 0], 1, False),

    ([0, 0, 0, 0, 0], 3, True),

    ([1, 0, 1, 0, 1], 1, False),
]


for flowerbed, n, expected in tests:
    result = canPlaceFlowers(flowerbed.copy(), n)

    print(f"flowerbed={flowerbed}, n={n}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()