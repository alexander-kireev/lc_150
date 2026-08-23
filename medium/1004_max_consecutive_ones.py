









def longestOnes(nums, k):
    zeros = 0
    left = 0
    best = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        best = max(best, (right - left) + 1)

    return best









tests = [
    ([1,1,1,0,0,0,1,1,1,1,0], 2),                    # 6
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3),    # 10
    ([1,1,1,1], 0),                                    # 4
    ([0,0,0,0], 2),                                    # 2
    ([0,0,0,0], 4),                                    # 4
    ([1,0,1,0,1,0,1], 1),                              # 3
    ([1,0,1,1,0,1,1,1], 1),                            # 6
    ([1,0,1,1,0,0,1,1,1,1], 2),                        # 7
    ([0,1,1,1,0,1,1,0,1], 2),                          # 8
    ([1], 0),                                            # 1
    ([0], 0),                                            # 0
    ([0], 1),                                            # 1
]

for nums, k in tests:
    result = longestOnes(nums, k)
    print(f"nums={nums}, k={k} -> {result}")