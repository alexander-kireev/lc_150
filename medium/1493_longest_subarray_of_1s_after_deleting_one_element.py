def longestSubarray(nums):

    longest = 0
    left = 0
    zeros = 0

    for right in range(len(nums)):

        if nums[right] == 0:
            zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

        longest = max(longest, (right - left) + 1 - zeros)


    if longest == len(nums):
        longest -= 1
    return longest




tests = [
    ([1, 1, 0, 1], 3),
    ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
    ([1, 1, 1], 2),
    ([1], 0),
    ([0], 0),
    ([0, 0, 0], 0),
    ([1, 0, 1], 2),
    ([1, 1, 0, 1, 1], 4),
    ([1, 0, 1, 1, 1, 0, 1], 4),
    ([0, 1, 1, 1, 1], 4),
    ([1, 1, 1, 1, 0], 4),
    ([1, 1, 0, 0, 1, 1], 2),
    ([1, 1, 1, 0, 1, 1, 1], 6),
]

for nums, expected in tests:
    result = longestSubarray(nums)

    print(
        f"nums={nums} -> {result} "
        f"(expected {expected})"
    )