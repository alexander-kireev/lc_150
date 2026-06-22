def h_index(citations):
    citations.sort()
    max_h = len(citations)

    for i in range(max_h):

        if citations[i] >= max_h - i:
            return max_h - i

    return 0



print(h_index([3, 0, 6, 1, 5]))      # 3
print(h_index([1, 3, 1]))            # 1
print(h_index([0]))                  # 0
print(h_index([1]))                  # 1
print(h_index([100]))                # 1
print(h_index([0, 0, 0]))            # 0
print(h_index([1, 1, 1]))            # 1
print(h_index([2, 2, 2]))            # 2
print(h_index([3, 3, 3]))            # 3
print(h_index([4, 4, 0, 0]))         # 2
print(h_index([10, 8, 5, 4, 3]))     # 4
print(h_index([25, 8, 5, 3, 3]))     # 3
print(h_index([6, 5, 3, 1, 0]))      # 3
print(h_index([100, 100, 100, 100])) # 4
print(h_index([0, 1, 4, 5, 6]))      # 3