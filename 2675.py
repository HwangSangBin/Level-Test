num = int(input())
j = 0
d = []

for i in range(num):
    a = list(map(str, input().split()))
    b = int(a[0])
    c = a[1]

    while j < len(c):
        d.append(c[j])
        if len(d) == b * (1 + j):
            j += 1
    for z in range(len(d)):
        if len(d) > 20:
            pass
        else:
            print(d[z], end = "")
    print("")