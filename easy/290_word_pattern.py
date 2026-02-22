def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    words = s.split()

    d = {}
    seen_words = {}

    if len(words) != len(pattern):
        return False

    for i in range(len(pattern)):
        letter = pattern[i]
        word = words[i]

        if letter in d:
            if d[letter] != word:
                return False
        
        else:
            if word in seen_words:
                return False
            else:
                d[letter] = word
                seen_words[word] = True

    return True
