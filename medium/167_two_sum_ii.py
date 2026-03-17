def twoSum(nums, target):

    last = len(nums) - 1
    first = 0

    while True:
        front = nums[first]
        back = nums[last]

        total = front + back

        if total == target:
            return [first + 1, last + 1]
        
        if total > target:
            last -= 1

        if total < target:
            first += 1


    return






numbers = [2,7,11,15]
target = 9

numbers = [2,3,4]
target = 6

numbers = [5, 25, 75]
target = 100

print(twoSum(numbers, target))