# 하노이의 탑 규칙
# 맨 밑에 있는 거를 옮길라믄 위에 있는 거 전부 다 다른 곳에 있어야됑

def hanoi(num, start, to, other):
    if num == 1:
        print("{0} {1}".format(start, other))
    
    else:
        hanoi(num - 1, start, other, to)
        print("{0} {1}".format(start, other))
        hanoi(num - 1, to, start, other)
        

floor = int(input())

print((2 ** floor) - 1)
hanoi(floor, 1, 2, 3)