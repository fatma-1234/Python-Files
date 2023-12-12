string = "aaabbcccdeffgaafffg"
n = len(string)
compressed = ""
i = 1
count = 1
while i < n:
    if string[i] == string[i-1]:
        count = count+1
    else:
        if count > 1:
            compressed = compressed+string[i-1]+str(count)
        else:
            compressed = compressed+string[i-1]
        count = 1
    i = i+1
if count > 1:
    compressed = compressed+string[i-1]+str(count)
else:
    compressed = compressed+string[i-1]
print(compressed)
