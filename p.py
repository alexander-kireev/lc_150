words = ["hello", "bye"]

for word in words:
    word = "".join(sorted(word))
    print(word)

print(words)