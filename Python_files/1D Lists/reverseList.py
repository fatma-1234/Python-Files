li = [int(x) for x in input().split()]
print(li[::-1])


# li = [int(x) for x in input().split()]
# revli = li.copy()                       #revli=li is not done because both will change
# for i in range(len(revli)//2):
#     temp = revli[i]                     # a = a + b     can also be done
#     revli[i] = revli[-i-1]              # b = a - b
#     revli[-i-1] = temp                  # a = a - b
# print(revli)                            # a, b = b, a   can also be done
