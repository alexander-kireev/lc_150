def canFinish(numCourses, prerequisites):

    if not prerequisites:
        return True

    counts = {}

    for p in prerequisites:
        _to, _from = p[0], p[1]

        if _from in counts:
            counts[_from].append(_to)
        else:
            counts[_from] = [_to]

        if _to not in counts:
            counts[_to] = []

    state = [0] * numCourses

    def dfs(node):
        if state[node] == 1:
            return False

        if state[node] == 2:
            return True

        state[node] = 1

        for n in counts[node]:
            if not dfs(n):
                return False

        state[node] = 2
        return True

    return dfs(prerequisites[0][1])

tests = [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False),

    (1, [], True),
    (3, [], True),

    (3, [[1, 0], [2, 1]], True),
    (3, [[1, 0], [2, 1], [0, 2]], False),

    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),

    (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),

    (5, [[1, 0], [2, 0], [3, 1], [4, 3]], True),

    (5, [[1, 0], [2, 1], [3, 2], [4, 3], [1, 4]], False),

    (6, [[1, 0], [2, 1], [3, 2], [4, 2], [5, 4]], True),

    (6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [2, 5]], False),
]


for numCourses, prerequisites, expected in tests:
    result = canFinish(numCourses, prerequisites)

    print(f"numCourses={numCourses}")
    print("prerequisites:", prerequisites)
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()