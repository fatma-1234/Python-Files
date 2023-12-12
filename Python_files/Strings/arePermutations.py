string1 = input()
string2 = input()
if len(string1) != len(string2):
    print("Not")
else:
    # Initialize an array to store character frequencies
    char_frequency = [0] * 256
    # Increment frequencies for characters in the first string
    for char in string1:
        char_code = ord(char)
        char_frequency[char_code] += 1
    # Decrement frequencies for characters in the second string
    for char in string2:
        char_code = ord(char)
        char_frequency[char_code] -= 1
    # Check if all character frequencies are zero
    for count in char_frequency:
        if count != 0:
            print("Not")
            break
    else:
        print("Yes")
