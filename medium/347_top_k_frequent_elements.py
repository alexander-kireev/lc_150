def top_k_frequent_element(nums, k):
    # output list
    output = []

    # empty num:count map
    num_map = {}

    # iterate over nums, count occurences of each number
    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1

    # make list of lists of length nums
    buckets = [[] for _ in range(len(nums) + 1)]

    # place each num in buckets of its count
    for num in num_map:
        buckets[num_map[num]].append(num)

    # start from largest possible index
    index = len(nums)

    # fill output list
    while len(output) < k and index > 0:
        for num in buckets[index]:
            output.append(num)
            if len(output) == k:
                return output
        index -= 1

    return output




nums = [1,1,1,2,2,3]
k = 2

print(top_k_frequent_element(nums, k))
