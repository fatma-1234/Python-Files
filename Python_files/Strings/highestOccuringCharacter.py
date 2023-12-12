text = "Hello brother how are you doing brooother"
charCount = [0]*256
for ele in text:
    charCount[ord(ele)] += 1
for i in range(256):
    if max(charCount) == charCount[i]:
        print(chr(i))
        break
