def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > stack[-1][0]:
            days = i - stack[-1][1]
            answer[stack[-1][1]] = days
            stack.pop()

        stack.append([temperatures[i], i])

    return answer


tests = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([30, 40, 50, 60], [1, 1, 1, 0]),
    ([30, 60, 90], [1, 1, 0]),

    ([70], [0]),
    ([70, 70], [0, 0]),
    ([80, 70, 60], [0, 0, 0]),

    ([60, 70], [1, 0]),
    ([70, 60, 80], [2, 1, 0]),

    ([70, 71, 70, 72], [1, 2, 1, 0]),

    ([90, 80, 70, 60, 100], [4, 3, 2, 1, 0]),

    ([50, 40, 40, 60], [3, 2, 1, 0]),

    ([73, 72, 71, 70, 74], [4, 3, 2, 1, 0]),
]


for temperatures, expected in tests:
    result = dailyTemperatures(temperatures)

    print(f"temperatures={temperatures}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()