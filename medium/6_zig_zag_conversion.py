def zigzag(text, num_rows):
    if num_rows == 1:
        return text
    
    rows = []
    for _ in range(num_rows):
        rows.append([])


    row = 0
    down = True

    for c in text:
        rows[row].append(c)
        
        # if going down
        if down:

            # if just added to bottom row, reverse direction
            if row == num_rows - 1:
                down = False
                row -= 1
            # if continuing to go down, continue
            else:
                row += 1
        
        # if going up
        else:

            # if just added to top row, reverse direction
            if row == 0:
                down = True
                row += 1
            # if continuing to go up, continue
            else:
                row -= 1

    output = []

    for row in rows:
        for c in row:
            output.append(c)
    
    return "".join(output)



print(zigzag("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
print(zigzag("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
print(zigzag("A", 1))               # A
print(zigzag("AB", 1))              # AB
print(zigzag("AB", 2))              # AB
print(zigzag("ABC", 2))             # ACB
print(zigzag("ABCD", 2))            # ACBD
print(zigzag("ABCDE", 3))           # AEBDC
print(zigzag("ABCDEFG", 3))         # AEBDFCG
print(zigzag("ABCDEFG", 4))         # AGBFCED
print(zigzag("HELLOWORLD", 3))      # HOLELWRDLO
print(zigzag("THISISAZIGZAG", 4))   # TAGHSZASIIGIZ