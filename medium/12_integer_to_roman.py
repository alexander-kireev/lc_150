def int_to_roman(num):
    roman = []

    values = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    while num > 0:
        string_form = str(num)

        if string_form.startswith(("4", "9")):
            if num >= 900:
                num -= 900
                roman.append(values[100])
                roman.append(values[1000])
            elif num >= 400:
                num -= 400
                roman.append(values[100])
                roman.append(values[500])
            elif num >= 90:
                num -= 90
                roman.append(values[10])
                roman.append(values[100])
            elif num >= 40:
                num -= 40
                roman.append(values[10])
                roman.append(values[50])
            elif num >= 9:
                num -= 9
                roman.append(values[1])
                roman.append(values[10])
            elif num >= 4:
                num -= 4
                roman.append(values[1])
                roman.append(values[5])
        else:
            if num >= 1000:
                num -= 1000
                roman.append(values[1000])
            elif num >= 500:
                num -= 500
                roman.append(values[500])
            elif num >= 100:
                num -= 100
                roman.append(values[100])
            elif num >= 50:
                num -= 50
                roman.append(values[50])
            elif num >= 10:
                num -= 10
                roman.append(values[10])
            elif num >= 5:
                num -= 5
                roman.append(values[5])
            elif num >= 1:
                num -= 1
                roman.append(values[1])

    return "".join(roman)



x = 1994
print(int_to_roman(x))