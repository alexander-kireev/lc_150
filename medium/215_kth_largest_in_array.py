import heapq

def findKthLargest(nums, k):
    # empty heap
    heap = []

    for n in nums:

        # if heap isn't full
        if len(heap) < k:
            heapq.heappush(heap, n)
            
        # if heap is full, but n is larger than top
        elif n > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, n)

    return heap[0]




nums = [3,2,3,1,2,4,5,5,6]
k = 4
#Output: 4

print(findKthLargest(nums, k))