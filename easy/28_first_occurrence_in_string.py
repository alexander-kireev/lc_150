def strStr(haystack: str, needle: str) -> int:
    

    len_needle = len(needle)

    for i in range(len(haystack) - len_needle + 1):
        match = 0
        print(i)

        for j in range(len_needle):
            if haystack[i + j] == needle[j]:
                match += 1
            else:
                break
        
        if match == len_needle:
            return i
        
    return -1


haystack = "sadbutsad"
needle = "sad"
haystack = "leetcode"
needle = "leeto"

print(strStr(haystack, needle))