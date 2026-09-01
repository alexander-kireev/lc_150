import heapq

def kClosest(points, k):

    max_heap = []

    for x, y in points:

        distance = x * x + y * y

        if len(max_heap) < k:
            heapq.heappush(max_heap, (-distance, [x, y]))
        elif -distance > max_heap[0][0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-distance, [x, y]))

    output = []

    for item in max_heap:
        output.append(item[1])

    return output

tests = [
    (
        [[1, 3], [-2, 2]],
        1,
        [[-2, 2]]
    ),

    (
        [[3, 3], [5, -1], [-2, 4]],
        2,
        [[3, 3], [-2, 4]]
    ),

    (
        [[1, 1]],
        1,
        [[1, 1]]
    ),

    (
        [[1, 0], [2, 0], [3, 0]],
        2,
        [[1, 0], [2, 0]]
    ),

    (
        [[-1, -1], [4, 4], [0, 2], [3, 0]],
        2,
        [[-1, -1], [0, 2]]
    ),

    (
        [[10, 10], [1, 1], [2, 2], [3, 3]],
        3,
        [[1, 1], [2, 2], [3, 3]]
    ),

    (
        [[0, 1], [1, 0], [5, 5]],
        2,
        [[0, 1], [1, 0]]
    ),

    (
        [[-5, 0], [0, -4], [3, 0], [0, 2], [1, 1]],
        3,
        [[0, 2], [1, 1], [3, 0]]
    ),
]


for points, k, expected in tests:
    result = kClosest(points, k)

    result_sorted = sorted(map(tuple, result))
    expected_sorted = sorted(map(tuple, expected))

    print(f"points={points}, k={k}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result_sorted == expected_sorted)
    print()