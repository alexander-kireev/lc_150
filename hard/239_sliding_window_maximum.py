from collections import deque
import heapq

def maxSlidingWindow(nums, k):

    output = []
    max_heap = []

    for i in range(k):
        heapq.heappush(max_heap, [-nums[i], i])
        
    output.append(-max_heap[0][0])

    for i in range(k, len(nums)):

        heapq.heappush(max_heap, [-nums[i], i])

        while (i - max_heap[0][1]) >= k:
            heapq.heappop(max_heap)

        output.append(-max_heap[0][0])

    return output
        


tests = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([1], 1, [1]),

    ([1, 2, 3, 4], 2, [2, 3, 4]),
    ([4, 3, 2, 1], 2, [4, 3, 2]),

    ([7, 7, 7, 7], 2, [7, 7, 7]),

    ([9, 1, 3, 7, 2, 6], 3, [9, 7, 7, 7]),

    ([1, -1], 1, [1, -1]),

    ([5, 3, 4], 3, [5]),

    ([2, 1, 5, 3, 4, 6], 2, [2, 5, 5, 4, 6]),

    ([10, 9, 8, 7, 6, 5], 3, [10, 9, 8, 7]),

    ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
]


for nums, k, expected in tests:
    result = maxSlidingWindow(nums, k)

    print(f"nums={nums}, k={k}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()