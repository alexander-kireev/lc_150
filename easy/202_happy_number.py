
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """

    seen = set()

    while True:
        if n == 1:
            return True
        
        if n in seen:
            return False
        
        seen.add(n)
        
        n_str = str(n)
        n = 0
        for c in n_str:
            n += (int(c) * int(c)) 

        
    