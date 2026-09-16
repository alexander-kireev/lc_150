from math import ceil

def minEatingSpeed(piles, h):
    max_bananas = max(piles)

    if len(piles) == h:
        return max_bananas

    left = 1
    right = max_bananas
    min_bananas = max_bananas

    while left <= right:

        mid = (left + right) // 2
        available = h

        for p in piles:

            available -= ceil(p/mid)

            if available < 0:
                break

        if available >= 0:
            min_bananas = min(min_bananas, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_bananas


tests = [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30),
    ([30, 11, 23, 4, 20], 6, 23),

    ([1], 1, 1),
    ([10], 10, 1),
    ([10], 1, 10),

    ([1, 1, 1, 1], 4, 1),
    ([4, 4, 4, 4], 4, 4),
    ([4, 4, 4, 4], 8, 2),

    ([5, 10, 15], 6, 5),
    ([5, 10, 15], 3, 15),

    ([9, 9, 9], 6, 5),

    ([100, 200, 300], 6, 100),

    ([312884470], 312884469, 2),

    ([805306368, 805306368, 805306368], 1000000000, 3),
]


for piles, h, expected in tests:
    result = minEatingSpeed(piles, h)

    print(f"piles={piles}, h={h}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()