text = input("Enter sentence : ")
char_1 = input("Enter the character to replace : ")
char_2 = input("Enter the character to replace with : ")
new_text = ""
for ele in text:
    if ele == char_1:
        new_text += char_2
    else:
        new_text += ele
print("New sentence is : ", new_text)
