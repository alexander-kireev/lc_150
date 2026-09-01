def totalFruit(fruits):
    fruit_types = {}
    left = 0
    best = 0

    for right in range(len(fruits)):
        fruit_types[fruits[right]] = fruit_types.get(fruits[right], 0) + 1 

        while len(fruit_types) > 2:
            fruit_types[fruits[left]] -= 1

            if fruit_types[fruits[left]] == 0:
                fruit_types.pop(fruits[left])
            
            left += 1

        best = max(best, (right - left) + 1)

    return best

tests = [
    ([1, 2, 1], 3),
    ([0, 1, 2, 2], 3),
    ([1, 2, 3, 2, 2], 4),
    ([1, 1, 1, 1], 4),
    ([1, 2, 3, 4], 2),
    ([1, 2, 1, 2, 1, 2], 6),
    ([0, 1, 2, 2, 2, 1, 1], 6),
    ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 2, 3, 3, 3, 2, 2], 7),
    ([0, 0, 1, 1, 2, 2, 1, 1], 6),
]

for fruits, expected in tests:
    result = totalFruit(fruits)
    print(
        f"fruits={fruits} -> {result} "
        f"(expected {expected})"
    )