def lengthOfLastWord(s: str) -> int:
    words = s.split()[-1]
    return len(words[-1])





s = "   fly me   to   the moon  "


print(lengthOfLastWord(s))