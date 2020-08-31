num = []
for i in range(3):
    a = int(input())
    num.append(a)
gop = num[0] * num[1] * num[2]
gop = str(gop)
for i in range(10):
    print(gop.count(str(i)))