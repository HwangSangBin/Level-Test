def findnonselfnumber(n):
    num = n
    while n != 0:
        num += n % 10
        n //= 10
    return num


nonself = [0] * 10001
count = 1

for a in range(1, 10001):
    nonself[a] = findnonselfnumber(a)


for i in range(1, 10001):
    count = 0
    for j in range(1, i):
        if i == nonself[j]:
            count += 1
    if count == 0:
        print(i) 