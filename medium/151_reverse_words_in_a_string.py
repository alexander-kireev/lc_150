def reverse_words_in_a_string(text):
    output = []

    split_text = text.split()

    for i in range(len(split_text) - 1, -1, -1):
        output.append(split_text[i])

    return " ".join(output)







print(reverse_words_in_a_string("the sky is blue"))          # "blue is sky the"
print(reverse_words_in_a_string("  hello world  "))          # "world hello"
print(reverse_words_in_a_string("a good   example"))         # "example good a"
print(reverse_words_in_a_string("  Bob    Loves  Alice   ")) # "Alice Loves Bob"
print(reverse_words_in_a_string("Alice does not even like bob")) # "bob like even not does Alice"
print(reverse_words_in_a_string("a"))                        # "a"
print(reverse_words_in_a_string("   single   "))             # "single"
print(reverse_words_in_a_string("one    two     three"))     # "three two one"
print(reverse_words_in_a_string("123 abc 456"))              # "456 abc 123"
print(reverse_words_in_a_string("  leetcode   is   fun  "))  # "fun is leetcode"