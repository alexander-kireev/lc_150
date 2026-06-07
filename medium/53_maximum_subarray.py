def m(nums):
    mx = nums[0]
    cur = nums[0]

    for n in nums[1:]:
        cur = max(n, cur + n)
        mx = max(mx, cur)

    return mx






nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
print(m(nums))