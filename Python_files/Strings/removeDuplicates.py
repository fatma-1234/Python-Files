text = input()
result, seen_characters = "", ""

for char in text:
    if char not in seen_characters:
        result += char
        seen_characters += char

print(result)
