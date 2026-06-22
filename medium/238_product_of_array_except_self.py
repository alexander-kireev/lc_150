def product_of_array_except_self(nums):
    length = len(nums)
    output = [1] * length
    total_prefix = 1
    total_suffix = 1

    for i in range(1, length):
        total_prefix = total_prefix * nums[i - 1]
        output[i] = output[i] * total_prefix

    for i in range(length - 2, -1, -1):
        total_suffix = total_suffix * nums[i + 1]
        output[i] = output[i] * total_suffix

    return output

nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
print(product_of_array_except_self(nums))