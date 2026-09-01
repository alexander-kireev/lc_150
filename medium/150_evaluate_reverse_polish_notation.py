def evalRPN(tokens):
    stack = []

    def is_number(x):
        try:
            x = int(x)
            return True
        except:
            return False

    for t in tokens:

        if is_number(t):
            stack.append(int(t))

        else:

            prev = stack.pop()
            prev_prev = stack.pop()

            if t == "+":
                stack.append(prev + prev_prev)
            elif t == "-":
                stack.append(prev_prev - prev)
            elif t == "*":
                stack.append(prev * prev_prev)
            else:
                stack.append(int(prev_prev / prev))

    return stack.pop()



tests = [
    # (["2", "1", "+", "3", "*"], 9),
    # (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),

    (["5"], 5),

    (["3", "4", "+"], 7),
    (["8", "3", "-"], 5),
    (["6", "7", "*"], 42),

    (["7", "2", "/"], 3),
    (["-7", "2", "/"], -3),
    (["7", "-2", "/"], -3),

    (["2", "3", "4", "*", "+"], 14),
    (["5", "1", "2", "+", "4", "*", "+", "3", "-"], 14),

    (["4", "2", "+", "3", "-"], 3),
    (["15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1", "+", "+", "-"], 5),
]


for tokens, expected in tests:
    result = evalRPN(tokens)

    print(f"tokens={tokens}")
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()