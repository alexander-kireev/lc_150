
def x(nums):
    longest = 0
    found = set(nums)

    for n in found:
        if longest >= (len(nums) // 2) + 1:
            return longest

        if n - 1 not in found:
            cur_len = 1
            while n + 1 in found:
                cur_len += 1
                n += 1
            longest = max(longest, cur_len)

    return longest







nums = [5, 100,4,200,1,3,2]
Output: 4
print(x(nums))