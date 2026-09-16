from math import inf
def mincostTickets(days, costs):

    calendar = [inf] * 25
    calendar[days[0]] = costs[0]
    TICKETS = [1, 7, 30]

    prev = 0

    for i in range(1, len(days)):

        
        for j in range(len(costs)):
            prev_day = max(day - TICKETS[i], 0)


            calendar[day] = min(calendar[day], calendar[prev_day] + costs[i])



    return calendar[days[-1]]



tests = [
    ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),

    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),

    ([1], [2, 7, 15], 2),

    ([1, 2], [2, 7, 15], 4),

    ([1, 8, 15, 22, 29], [2, 7, 15], 10),

    ([1, 2, 3, 4, 5, 6, 7], [2, 7, 15], 7),

    ([1, 7, 8], [2, 7, 15], 6),

    ([1, 30, 31, 60, 61, 90], [3, 8, 20], 18),

    ([100, 101, 102, 103, 104, 105, 106, 107], [5, 9, 30], 14),

    ([1, 365], [2, 7, 15], 4),

    ([1, 2, 3, 10, 11, 12, 20, 21, 22], [3, 8, 20], 20),
]


for days, costs, expected in tests:
    result = mincostTickets(days, costs)

    print(f"days={days}, costs={costs}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()