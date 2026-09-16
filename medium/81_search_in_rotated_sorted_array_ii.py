def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True

        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
            continue

        # check if left is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


tests = [
    ([2, 5, 6, 0, 0, 1, 2], 0, True),
    ([2, 5, 6, 0, 0, 1, 2], 3, False),

    ([1], 1, True),
    ([1], 0, False),

    ([1, 1, 1, 1, 1], 1, True),
    ([1, 1, 1, 1, 1], 2, False),

    ([1, 0, 1, 1, 1], 0, True),
    ([1, 1, 1, 0, 1], 0, True),

    ([3, 1, 1], 3, True),
    ([3, 1, 1], 2, False),

    ([1, 3, 1, 1, 1], 3, True),

    ([4, 5, 6, 6, 7, 0, 1, 2, 4, 4], 7, True),
    ([4, 5, 6, 6, 7, 0, 1, 2, 4, 4], 3, False),

    ([2, 2, 2, 3, 4, 2], 4, True),
    ([2, 2, 2, 3, 4, 2], 1, False),
]


for nums, target, expected in tests:
    result = search(nums, target)

    print(f"nums={nums}, target={target}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()