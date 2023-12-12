def fact(a):
    a_fact = 1
    for i in range(1, a + 1):
        a_fact = a_fact * i
    return a_fact


def ncr(b, c):
    n_fact = fact(b)
    r_fact = fact(c)
    n_min_r_fact = fact(b - c)
    ans = n_fact//(r_fact*n_min_r_fact)
    return ans


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
print(ncr(n, r))
