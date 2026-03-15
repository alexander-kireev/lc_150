def singleNumber(nums):
    seen = set()
    

    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)

    return list(seen)[0]

    

nums = [4,1,2,1,2]
print(singleNumber(nums))