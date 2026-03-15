def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]




x = -121
# x = 121
# x = 10
# x = 1

print(isPalindrome(x))