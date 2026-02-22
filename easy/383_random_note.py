
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    
    letters = {}

    for c in ransomNote:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    
    for c in magazine:
        if c in letters:
            letters[c] -= 1

            if letters[c] == 0:
                letters.pop(c)
            
            if not letters:
                return True
    
    return False