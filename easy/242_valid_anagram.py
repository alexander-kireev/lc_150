def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    if len(s) != len(t):
        return False

    s_chars = {}
    t_chars = {}

    for c in s:
        if c in s_chars:
            s_chars[c] += 1
        else:
            s_chars[c] = 1
        
    for c in t:
        if c in t_chars:
            t_chars[c] += 1
        else:
            t_chars[c] = 1
    
    return s_chars == t_chars