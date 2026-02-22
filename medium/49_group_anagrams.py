def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    words = {}
    
    for s in strs:
        sorted_s = "".join(sorted(s))

        if sorted_s in words:
            words[sorted_s].append(s)
        else:
            words[sorted_s] = [s]
    
    output = []

    for anagram in words:
        output.append(words[anagram])
    
    return output