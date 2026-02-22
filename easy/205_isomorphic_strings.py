def isIsomorphic(s, t):
    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]].append(i)
        else:
            s_dict[s[i]] = [i]
        
        if t[i] in t_dict:
            t_dict[t[i]].append(i)
        else:
            t_dict[t[i]] = [i]
        
        if s_dict[s[i]] != t_dict[t[i]]:
            return False
    
    return True


s = "bbbaaaba"
t = "aaabbbba"

print(isIsomorphic(s, t))