sentence = "Hello I am Alok"
words = []
current_word = ""
for char in sentence:
    if char != ' ':
        current_word += char
    else:
        words.append(current_word[::-1])
        current_word = ""
words.append(current_word[::-1])
reversed_sentence = ' '.join(words)
print(reversed_sentence)
