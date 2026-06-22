


# def jump_game_ii(nums):
#     last_index = len(nums) - 1
#     if last_index == 0:
#         return 0

#     max_reach = 0
#     position = 0
#     jumps = 0

    
#     while True:
#         # jump
#         jumps += 1

#         # get length of jump from current position
#         jump_range = nums[position]

#         # check if jumping from here is enough
#         if position + jump_range >= last_index:
#             return jumps

#         # set best values for round
#         best_jump = 0
#         best_position = 0

#         # get copy of position
#         this_position = position

#         # while we can jump
#         while jump_range > 0:

#             # get index of item
#             this_position = this_position + 1

#             # check we are not out of bounds
#             if this_position > last_index:
#                 break

#             # perform jump
#             this_jump = nums[this_position]

#             # decrement jump remaining
#             jump_range = jump_range - 1

#             # check if this is best jump in round
#             if this_jump + this_position >= best_jump + best_position:
#                 best_jump = this_jump
#                 best_position = this_position
#                 position_can_reach_from_here = this_position + this_jump
#                 max_reach = max(position_can_reach_from_here, max_reach)
#                 if max_reach >= last_index:
#                     return jumps + 1

#         position = best_position


def jump_game_ii(nums):
    max_reach = 0
    cur_reach = 0
    jumps = 0

    for i in range(len(nums) - 1):
        
        max_reach = max(max_reach, i + nums[i])

        if max_reach >= len(nums) - 1:
            jumps += 1
            break

        if cur_reach == i:
            jumps += 1
            cur_reach = max_reach

    return jumps


print(jump_game_ii([1, 1, 1, 1, 1]))      # 4
print(jump_game_ii([2, 3, 1, 1, 4]))      # 2
print(jump_game_ii([2, 3, 0, 1, 4]))      # 2
print(jump_game_ii([0]))                  # 0
print(jump_game_ii([1, 2]))               # 1
print(jump_game_ii([1, 1, 1, 1]))         # 3
print(jump_game_ii([4, 1, 1, 1, 1]))      # 1
print(jump_game_ii([2, 1, 1, 1, 1]))      # 3
print(jump_game_ii([3, 2, 1, 1, 4]))      # 2
print(jump_game_ii([1, 2, 3]))            # 2
print(jump_game_ii([2, 3, 1]))            # 1
print(jump_game_ii([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))  # 3