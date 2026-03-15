def plusOne(digits):

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    
    digits.insert(0, 1)
    return digits



digits = [4,3,2,1]

print(plusOne(digits))