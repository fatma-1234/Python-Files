# Need to enter initial Fahrenheit Value, Final Fahrenheit value, and the difference in
# between as S, E and W respectively. Now the programme will find all the Fahrenheit values
# in between and display their converted Celsius value


def printTable(S, E, W):
    while S <= E:
        celsius = (S - 32) * 5/9
        print(S, int(celsius))
        S += W


s = int(input())
e = int(input())
w = int(input())
printTable(s, e, w)


# S = int(input())
# E = int(input())
# W = int(input())
# while S <= E:
#     celsius = (S - 32) * 5/9
#     print(S, int(celsius))
#     S += W
