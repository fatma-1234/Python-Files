user_input = input("Enter a piece of text: ")
vowels = 0
consonants = 0
digits = 0
special_chars = 0
for char in user_input:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1
# for char in user_input:
#     if 'A' <= char.upper() <= 'Z' and char.upper() in 'AEIOU':
#         vowels += 1
#     elif 'A' <= char.upper() <= 'Z':
#         consonants += 1
#     elif '0' <= char <= '9':
#         digits += 1
#     else:
#         special_chars += 1
print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Digits: ", digits)
print("Special Characters: ", special_chars)
