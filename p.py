# t1
nums = [4, 8, 15, 16]

for i, num in enumerate(nums):
    print(i, num)



# t2
nums = [4, 8, 15, 16]
def find_index(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
        
    return -1

# t3
nums = [3, 6, 8, 11, 14]
for i, num in enumerate(nums):
    if num % 2 == 0:
        print(i)


# t4
names = ["Alex", "Ivan", "Maria"]
for i, name in enumerate(names, start=1):
    print(str(i) + ". " + name)