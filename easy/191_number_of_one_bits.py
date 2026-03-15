def hammingWeight(n: int) -> int:
    s = bin(n)[2:]
    counter = 0
    for c in s:
        if c == "1":
            counter += 1

    return counter




n = 128
print(hammingWeight(n))