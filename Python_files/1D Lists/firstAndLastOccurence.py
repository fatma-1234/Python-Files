li = [int(x) for x in input().split()]
num = int(input())
f = 0
l = len(li) - 1
first_occurrence = -1
while f <= l:
    m = (f + l) // 2
    if li[m] == num:
        first_occurrence = m
        l = m - 1   # Move left to find the first occurrence
    elif li[m] < num:
        f = m + 1
    else:
        l = m - 1
f = 0
l = len(li) - 1
last_occurrence = -1
while f <= l:
    m = (f + l) // 2
    if li[m] == num:
        last_occurrence = m
        f = m + 1   # Move right to find the last occurrence
    elif li[m] < num:
        f = m + 1
    else:
        l = m - 1
if first_occurrence != -1:
    print("First occurrence:", first_occurrence + 1)
    print("Last occurrence:", last_occurrence + 1)
else:
    print("Number not found in the list")
