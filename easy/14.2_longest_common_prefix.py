
def longest_common_prefix(strs):

        i = 0

        # iterate over first word in list
        while i < len(strs[0]):

            # get char at current index
            char = strs[0][i]

            # check if all words share prefix
            for word in strs:

                # if exceeds length or not prefix
                if i >= len(word) or char != word[i]:
                    return strs[0][:i]

            i += 1

        return strs[0][:i]

strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))