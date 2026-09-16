def nextGreaterElements(nums):
    output = [-1] * len(nums)
    stack = []
    i = 0
    count = len(nums) * 2

    while count > 0:

        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            output[index] = nums[i]

        if stack and i == stack[-1]:
            return output
        
        stack.append(i)

        i += 1
        count -= 1

        if i == len(nums):
            i = 0

    return output

tests = [
    ([1, 2, 1], [2, -1, 2]),
    ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),

    ([1], [-1]),
    ([2, 1], [-1, 2]),
    ([1, 2], [2, -1]),

    ([3, 3, 3], [-1, -1, -1]),

    ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),

    ([1, 5, 3, 6, 4], [5, 6, 6, -1, 5]),

    ([2, 1, 2, 4, 3], [4, 2, 4, -1, 4]),

    ([-2, -1, -3], [-1, -1, -2]),

    ([1, 3, 2, 4], [3, 4, 4, -1]),
]


for nums, expected in tests:
    result = nextGreaterElements(nums)

    print(f"nums={nums}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()