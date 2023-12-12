li = [int(x) for x in input().split()]
for i in range(len(li)):
    for j in range(i, len(li)):            # here loop starts from i instead of 0 because
        if i != j and li[i] == li[j]:      # it will print same duplicate two times
            print(li[i])
            break
