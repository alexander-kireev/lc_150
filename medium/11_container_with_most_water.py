def maxArea(height) -> int:

    front = 0
    back = len(height) - 1
    max_area = 0

    while front < back:
        range = back - front
        current_area = range * min(height[front], height[back])

        if current_area > max_area:
            max_area = current_area

        if height[front] <= height[back]:
            front += 1
        else:
            back -= 1

    return max_area






height = [1,8,6,2,5,4,8,3,7]


print(maxArea(height))