def summaryRanges(nums):

    ranges = []
    i = 0
    while i < len(nums):
        j = 1

        while i + j < len(nums) and nums[i + j - 1] + 1 == nums[i + j]:
            j += 1

        if j == 1:
            ranges.append(f"{nums[i]}")
        else:
            ranges.append(f"{nums[i]}->{nums[i + j - 1]}")

        i += j

    return ranges






nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
nums = [0,2,3,4,6,8,9]

print(summaryRanges(nums))