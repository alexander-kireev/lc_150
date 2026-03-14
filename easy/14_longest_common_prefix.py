def longestCommonPrefix(strs) -> str:
    i = 0
    for i in range(len(strs[0])):

        for word in strs:
            if i >= len(word) or word[i] != strs[0][i]:
                return strs[0][0:i]

    return strs[0][0:i]
         
                 

strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))