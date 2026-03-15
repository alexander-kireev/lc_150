def reverseBits(n: int):
    bin_rep = bin(n)[2:]
    bits = [0] * (32 - len(bin_rep))
    bits = bits + list(bin_rep)
    total = 0

    for i in range(len(bits)):
        total += int(bits[i]) * pow(2, i)

    return total



n = 2147483644
n = 43261596
print(reverseBits(n))


