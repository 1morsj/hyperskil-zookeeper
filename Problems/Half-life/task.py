N = int(input())
R = int(input())
a = N
T = 0
while a > R:
    a = (a / 2)
    T = T + 1

print(T * 12)
