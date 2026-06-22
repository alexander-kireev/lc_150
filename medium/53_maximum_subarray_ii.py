def max_subarray(nums):
    best = nums[0]
    cur_total = nums[0]

    for num in nums[1:]:
        cur_total = max(cur_total + num, num)
        best = max(best, cur_total)

    return best

assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert max_subarray([1]) == 1
assert max_subarray([5,4,-1,7,8]) == 23
assert max_subarray([-1]) == -1
assert max_subarray([-2,-1]) == -1
assert max_subarray([-5,-4,-3,-2,-1]) == -1
assert max_subarray([0]) == 0
assert max_subarray([0,0,0]) == 0
assert max_subarray([-1,0,-2]) == 0
assert max_subarray([2,-1,2,3,4,-5]) == 10
assert max_subarray([8,-19,5,-4,20]) == 21
assert max_subarray([-2,3,-1,2]) == 4