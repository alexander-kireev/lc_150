def mySqrt(x: int) -> int:
    if x < 2:
        return x
    
    left = 1
    right = x // 2
    
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        
        sq = mid * mid

        if sq == x:
            return mid
        
        if sq > x:
            right = mid - 1
        if sq < x:
            ans = mid
            left = mid + 1

    return ans





print(mySqrt(40))