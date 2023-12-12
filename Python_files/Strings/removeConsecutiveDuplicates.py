text = input()
result = ""
prev_char = None
for char in text:
    if char != prev_char:
        result += char
        prev_char = char
print(result)

# text = input()
# result = text[0]
# n = len(text)
# for i in range(1, n):
#     if text[i] != text[i - 1]:
#         result += text[i]
# print(result)
