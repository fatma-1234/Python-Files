n = int(input())
sequence = "1"

if n > 0:
    print(sequence)

for i in range(n-1):
    result = ""
    count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:
            result += str(count) + sequence[i - 1]
            count = 1

    result += str(count) + sequence[-1]
    print(result)
    sequence = result
