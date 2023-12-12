s = input()
left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("The string is not a palindrome.")
        break
    left += 1
    right -= 1
else:
    print("The string is a palindrome.")


# s = input()
# p = s[::-1]
# print("Palindrome" if s == p else "Not Palindrome")
