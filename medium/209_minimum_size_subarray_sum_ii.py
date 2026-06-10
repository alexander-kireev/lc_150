from math import inf


def x(nums, target):
    # set current min len
    min_len = inf

    # set left and right subarray bounds
    left = 0
    right = 0

    # set starting sum as first element
    cur_sum = 0

    # while right bound is within list
    while right < len(nums):
        cur_sum += nums[right]
                 
        while cur_sum >= target:
            min_len = min(min_len, (right - left) + 1)
            cur_sum -= nums[left]
            left += 1

        right += 1

    return min_len if min_len != inf else 0







target = 7
nums = [2,3,1,2,4,3]
# Output: 2

# target = 4
# nums = [1,4,4]
# # Output: 1

# target = 7
# nums = [8]
print(x(nums, target))