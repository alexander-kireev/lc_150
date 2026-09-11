def findMaxLength(nums):
    counts = []

    for _ in range(len(nums)):
        counts.append([0, 0])

    if nums[0] == 0:
        counts[0] = [1, 0]
    else:
        counts[0] = [0, 1]

    best = 0
    
    for i in range(1, len(nums)):
        counts[i][0] = counts[i - 1][0]
        counts[i][1] = counts[i - 1][1]

        if nums[i] == 0:
            counts[i][0] += 1
        else:
            counts[i][1] += 1


        if counts[i][0] == counts[i][1]:
            best = max(best, counts[i][0] * 2)
        else:
            for j in range(i):
                zeros = counts[i][0] - counts[j][0]
                ones = counts[i][1] - counts[j][1]

                if zeros == ones:
                    best = max(best, zeros * 2)
                    break

                if (min(zeros, ones) * 2) <= best:
                    break

    return best




tests = [
    ([0, 1], 2),
    ([0, 1, 0], 2),
    ([0, 1, 1, 1, 1, 1, 0, 0, 0], 6),

    ([0], 0),
    ([1], 0),

    ([0, 0, 1, 1], 4),
    ([1, 1, 0, 0], 4),

    ([0, 0, 0, 1, 1, 1], 6),

    ([1, 0, 1, 0, 1, 0], 6),

    ([1, 1, 1, 0, 0], 4),

    ([0, 0, 1, 0, 1, 1, 0], 6),

    ([1, 0, 0, 1, 0, 1, 1, 1], 6),

    ([0, 1, 1, 0, 1, 1, 1, 0], 4),
]


for nums, expected in tests:
    result = findMaxLength(nums)

    print(f"nums={nums}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()