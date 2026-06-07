def x(nums):

    start = nums[0]
    i = 1

    while i < len(nums):
        if start + nums[i] < nums[i]:
            break
        start += nums[i]
        i += 1
    
    mx = start

    if i < len(nums):
        mx_end = nums[i]
        end = nums[i]
        i += 1
        while i < len(nums):
            end = max(end + nums[i], nums[i])
            mx_end = max(mx_end, end)
            i += 1

        mx = max(start, mx_end, start + end)

    return mx


print(x([1, -2, 3, -2]))          # 3
print(x([5, -3, 5]))              # 10
print(x([-3, -2, -3]))            # -2
print(x([3, -1, 2, -1]))          # 4
print(x([3, -2, 2, -3]))          # 3
print(x([10, -12, 11]))           # 21
print(x([8, -1, -3, 8]))          # 16
print(x([1, 2, 3, 4]))            # 10
print(x([-2]))                    # -2
print(x([0, 5, -3, 5]))           # 10