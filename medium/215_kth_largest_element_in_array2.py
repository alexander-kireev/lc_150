import heapq

def findKthLargest(nums, k):
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    return heap[0]

tests = [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),

    ([1], 1, 1),
    ([2, 1], 1, 2),
    ([2, 1], 2, 1),

    ([5, 5, 5, 5], 2, 5),

    ([-1, -2, -3, -4], 1, -1),
    ([-1, -2, -3, -4], 4, -4),

    ([7, 10, 4, 3, 20, 15], 3, 10),

    ([1, 2, 3, 4, 5], 5, 1),

    ([9, 3, 2, 11, 7, 6, 8], 4, 7),
]


for nums, k, expected in tests:
    result = findKthLargest(nums, k)

    print(f"nums={nums}, k={k}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()