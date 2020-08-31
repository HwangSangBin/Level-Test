a = int(input())
x = a
i = 0
while True:
    ten = a // 10
    one = a % 10
    b = ten + one
    a = one * 10 + b % 10
    i += 1
    if a == x:
        print(i)
        break