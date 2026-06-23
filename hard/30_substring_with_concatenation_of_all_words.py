# def substring(s, words):
#     output = []
#     word_len = len(words[0])

#     # build map
#     needed = {}

#     for word in words:
#         needed[word] = needed.get(word, 0) + 1

#     i = 0
#     while i + word_len - 1 < len(s):

#         # get slice to see if potential start of perm
#         start = s[i:i + word_len]

#         # if valid start
#         if start in needed:

#             # set bounds of 1 word window
#             left = i
#             right = i + word_len

#             # save starting bounds
#             start_left = left
#             start_right = right

#             cur_needed = {}

#             # ensure in bounds of s
#             while right <= len(s):
                
#                 # get word
#                 word = s[left:right]

#                 # if word is valid, log it, move window
#                 if word in needed:

#                     cur_needed[word] = cur_needed.get(word, 0) + 1

#                     # if perm can be valid, but too many copies of valid word
#                     if cur_needed[word] > needed[word]:

#                         # move window, removing first word from perm, until window is valid
#                         while start_right < right and cur_needed[word] > needed[word]:
#                             first_word = s[start_left:start_right]
#                             cur_needed[first_word] -= 1
#                             start_left += word_len
#                             start_right += word_len
                        
#                 # if word is invalid, invalidate perm
#                 else:
#                     break
                
#                 # if needed empty, valid perm found
#                 if cur_needed == needed:
#                     output.append(start_left)
#                     break 
                
#                 # extend window to the right by 1 word
#                 left += word_len
#                 right += word_len

#             # update starting search index
#             i = start_left + 1

#         else:

#             # update starting search index
#             i += 1

#     return output







# s = "ababaab"
# words = ["ab","ba","ba"]
# print(sorted(substring(s, words))) 

# # print(sorted(substring("barfoothefoobarman", ["foo", "bar"])))  
# # # [0, 9]

# # print(sorted(substring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])))  
# # # []

# # print(sorted(substring("barfoofoobarthefoobarman", ["bar", "foo", "the"])))  
# # # [6, 9, 12]

# # print(sorted(substring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])))  
# # # [8]

# # print(sorted(substring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"])))  
# # # [13]

# # print(sorted(substring("aaaaaa", ["aa", "aa"])))  
# # # [0, 1, 2]

# # print(sorted(substring("aaaaaaaa", ["aa", "aa", "aa"])))  
# # # [0, 1, 2]

# # print(sorted(substring("foobarfoobar", ["foo", "bar"])))  
# # # [0, 3, 6]

# # print(sorted(substring("barfoofoobar", ["foo", "bar"])))  
# # # [0, 6]

# # print(sorted(substring("abcabc", ["abc"])))  
# # # [0, 3]

# # print(sorted(substring("abc", ["abcd"])))  
# # []


def substring(s, words):
    output = []
    word_len = len(words[0])

    # build map
    needed = {}
    for word in words:
        needed[word] =+ needed.get(word, 0) + 1

    i = 0
    while i + word_len - 1 < len(s):

        # get slice to see if potential start of perm
        start = s[i:i + word_len]

        # if valid start
        if start in needed:

            # copy map
            cur_needed = needed.copy()

            # set bounds of 1 word window
            start = i
            end = start + word_len

            # ensure in bounds of s
            while end <= len(s):
                
                # get word
                word = s[start:end]

                # if word is valid, log it, move window
                if word in cur_needed:
                    cur_needed[word] -= 1
                    if cur_needed[word] == 0:
                        cur_needed.pop(word)
                    start += word_len
                    end += word_len
                # if word is invalid, invalidate perm
                else:
                    break
                
                # if needed empty, valid perm found
                if not cur_needed:
                    output.append(i)
                    break

        i += 1

    return output