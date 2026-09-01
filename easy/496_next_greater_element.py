# def nextGreaterElement(nums1, nums2):

#     mapping = [[-1, -1]] * len(nums2)
#     output = []


#     for i in range(len(nums2) - 2, -1, -1):

#         j = i + 1

#         while -1 < j < len(nums2):
#             if nums2[j] > nums2[i]:
#                 mapping[i] = [nums2[j], j]
#                 break
#             else:
#                 j = mapping[j][1]

#     index_map = {}

#     for i in range(len(nums2)):
#         index_map[nums2[i]] = i

#     for i in range(len(nums1)):

#         index = index_map[nums1[i]]

#         output.append(mapping[index][0])

#     return output




def nextGreaterElement(nums1, nums2):

    stack = []
    mapping = {}

    for i in range(len(nums2)):
        while stack and nums2[i] > stack[-1]:
            mapping[stack[-1]] = nums2[i]
            stack.pop()

        stack.append(nums2[i])

    for num in stack:
        mapping[num] = -1

    output = []

    for num in nums1:
        output.append(mapping[num])

    return output

tests = [
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ([2, 4], [1, 2, 3, 4], [3, -1]),

    ([1], [1], [-1]),
    ([1], [1, 2], [2]),

    ([2, 1], [2, 1, 3], [3, 3]),

    ([3, 1], [1, 2, 3], [-1, 2]),

    ([5, 2, 4], [2, 1, 4, 3, 5], [-1, 4, 5]),

    ([1, 3, 5], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7]),

    ([8, 4, 6], [8, 7, 6, 5, 4, 9], [9, 9, 9]),

    ([2, 7], [2, 3, 1, 5, 4, 7, 6], [3, -1]),
]


for nums1, nums2, expected in tests:
    result = nextGreaterElement(nums1, nums2)

    print(f"nums1={nums1}")
    print(f"nums2={nums2}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()