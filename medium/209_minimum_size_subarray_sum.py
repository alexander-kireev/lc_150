from math import inf

def minSubArrayLen(target, nums):
    total = 0
    start_subarray = 0
    end_subarray = 0
    min_length = inf
    

    for i in range(len(nums)):
        total += nums[i]

        if total < target:
            continue
        
        if total >= target:
            end_subarray = i

            cur_length = end_subarray - start_subarray + 1

            if cur_length < min_length:
                min_length = cur_length
            
            while total - nums[start_subarray] >= target and start_subarray + 1 <= end_subarray:
                total -= nums[start_subarray]

                start_subarray += 1
                cur_length = end_subarray - start_subarray + 1

                if cur_length < min_length:
                    min_length = cur_length


    if min_length == inf:
        return 0
    return min_length







target = 7
nums = [2,3,1,2,4,3]

target = 11
nums = [1,1,1,1,1,1,1,1]

nums = [1,4,4]
target = 1

print(minSubArrayLen(target, nums))
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.


