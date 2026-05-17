# nums = [[0,0], [0,1], [0,2]]

# directions = [[-1,0], [0,1], [1,0], [0,-1]]

# for x1, y1 in nums:
#     for x2,y2 in directions:
#         new_node = [x1 + x2, y1 + y2]
#         print(new_node)


image = [
  [1,2,1],
  [1,0,1]
]
node = [0, 1]
x = node[2]
y = node[1]
print(image[x][y])