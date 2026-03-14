def addBinary(a: str, b: str) -> str:
    output = []
    position = 0
    prev = 0

    while position < min(len(a), len(b)):
        last_a = int(a[-1 - position])
        last_b = int(b[-1 - position])
        cur = (last_a + last_b + prev) % 2
        prev = (last_a + last_b + prev) // 2
        output.append(str(cur))
        position += 1
    
    if len(a) > len(b):
        while position < len(a):
            cur = (int(a[-1 - position]) + prev) % 2
            prev = (int(a[-1 - position]) + prev) // 2
            output.append(str(cur))
            position += 1

    elif len(b) > len(a):
        while position < len(b):
            cur = (int(b[-1 - position]) + prev) % 2
            prev = (int(b[-1 - position]) + prev) // 2
            output.append(str(cur))
            position += 1

    while prev > 0:
        output.append(str(1))
        prev -=1

    return ''.join(output[::-1])




a = "1"
b = "11"

print(addBinary(a, b))