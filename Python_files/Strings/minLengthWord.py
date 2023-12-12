string = "This is a string with some words written in this string"
wordList = string.split()
minLength = float('inf')
for word in wordList:
    if len(word) < minLength:  # This will print the first minLength word, for last do <=
        minLength = len(word)
        ans = word
print(ans)
