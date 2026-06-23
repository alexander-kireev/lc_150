def int_to_roman(num):
    roman = []

    values = [
        [1000, "M"],
        [900, "CM"],
        [500, "D"],
        [400, "CD"],
        [100, "C"],
        [90, "XC"],
        [50, "L"],
        [40, "XL"],
        [10, "X"],
        [9, "IX"],
        [5, "V"],
        [4, "IV"],
        [1, "I"],
    ]

    for v in values:
        while num >= v[0]:
            roman.append(v[1])
            num -= v[0]

    return "".join(roman)



x = 1994
print(int_to_roman(x))