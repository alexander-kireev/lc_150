def lengthOfLongestSubstring(s) -> int:
    substring = set()
    longest = 0
    i = 0

    start = 0

    for i in range(len(s)):
        
        if s[i] not in substring:
            substring.add(s[i])

        else:

            while s[start] != s[i]:
                substring.remove(s[start])
                start += 1
            
            start += 1
        
        longest = max(len(substring), longest)
        

    return longest


s = "abcabcbb"
# s = "pwwkew"
# s = "bbbbb"
# s = "aab"
# s = "dvdf"
# s = "abaaacaaadaaae"

print(lengthOfLongestSubstring(s))