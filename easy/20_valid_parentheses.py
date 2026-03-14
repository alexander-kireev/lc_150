def isValid(s: str) -> bool:
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for c in s:
        if c in pairs.values():
            stack.append(c)
        else:
            if not stack or stack.pop() != pairs[c]:
                return False



    return len(stack) == 0

s = "()"
s = '()[]{}'



print(isValid(s))