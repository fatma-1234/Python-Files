text = input("Enter sentence : ")
char = input("Enter the character to remove : ")
new_text = ""
for ele in text:
    if ele != char:
        new_text += ele
print("New sentence is : ", new_text)
