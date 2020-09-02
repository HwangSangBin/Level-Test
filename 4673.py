def findnonselfnumber(n):
    num = n
    while n != 0:
        num += n % 10
        n //= 10
    return num


nonself = [0]*10001
count = 1
# a를 생성자로 하는 다음의 수를 다 구해두자.
# nonself[1] = 2, ns[2] = 4, ns[3] = 6, ns[4] = 8
# ns[10] = 11, ns[11] = 13 , .... (ns는 nonself 축약임)
for a in range(1, 10001):
    nonself[a] = findnonselfnumber(a)

# 1~10000 사이의 수 중에 self넘버가 있는지 검사
# i와 nonself[j]가 같으면 i는 생성자가 있는 nonself넘버임.
# 같은게 없으면 생성자가 없는 self 넘버임.
for i in range(1, 10001):
    count = 0
    for j in range(1, i):
        if i == nonself[j]:
            count += 1
    if count == 0:
        print(i) 