class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(self.min_stack[-1], value))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



tests = [
    (
        [
            ("push", -2),
            ("push", 0),
            ("push", -3),
            ("getMin", None),
            ("pop", None),
            ("top", None),
            ("getMin", None),
        ],
        [-3, 0, -2]
    ),

    (
        [
            ("push", 5),
            ("getMin", None),
            ("top", None),
        ],
        [5, 5]
    ),

    (
        [
            ("push", 3),
            ("push", 2),
            ("push", 1),
            ("getMin", None),
            ("pop", None),
            ("getMin", None),
            ("pop", None),
            ("getMin", None),
        ],
        [1, 2, 3]
    ),

    (
        [
            ("push", 2),
            ("push", 2),
            ("push", 1),
            ("push", 1),
            ("getMin", None),
            ("pop", None),
            ("getMin", None),
            ("pop", None),
            ("getMin", None),
        ],
        [1, 1, 2]
    ),

    (
        [
            ("push", -1),
            ("push", -5),
            ("push", -3),
            ("getMin", None),
            ("top", None),
            ("pop", None),
            ("top", None),
            ("getMin", None),
        ],
        [-5, -3, -5, -5]
    ),
]


for operations, expected in tests:
    stack = MinStack()
    results = []

    for operation, value in operations:
        if operation == "push":
            stack.push(value)

        elif operation == "pop":
            stack.pop()

        elif operation == "top":
            results.append(stack.top())

        elif operation == "getMin":
            results.append(stack.getMin())

    print("operations:", operations)
    print("result:", results)
    print("expected:", expected)
    print("correct:", results == expected)
    print()