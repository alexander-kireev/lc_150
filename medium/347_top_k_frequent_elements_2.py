import heapq

def topKFrequent(nums, k):

    num_map = {}

    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1

    max_heap = []

    for num in num_map:
        count = num_map[num]
        heapq.heappush(max_heap, (-count, num))

    output = []
    for _ in range(k):
        output.append(heapq.heappop(max_heap)[1])
    return output


tests = [
    # ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    # ([1], 1, [1]),
    # ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),

    # ([4, 4, 4, 4, 5, 5, 6], 1, [4]),

    ([5, 5, 6, 6, 6, 7, 7, 7, 7], 2, [7, 6]),

    # ([-1, -1, -1, 2, 2, 3], 2, [-1, 2]),

    ([10, 20, 10, 30, 20, 10], 2, [10, 20]),

    ([1, 2, 3, 4], 4, [1, 2, 3, 4]),

    ([9, 9, 8, 8, 8, 7, 7, 7, 7, 6], 2, [7, 8]),

    ([0, 0, 0, -1, -1, 2], 2, [0, -1]),
]


for nums, k, expected in tests:
    result = topKFrequent(nums, k)

    print(f"nums={nums}, k={k}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", set(result) == set(expected))
    print()