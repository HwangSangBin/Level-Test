# 방의 개수가 한 층 당 6의 배수로 증가된다.
# ex) 1층 = 1, 2층 = 6, 3층 = 12 ....

room = int(input())     # 방의 개수

floor = 1       # 층 수 
count = 1       # 방의 개수 합계

# 지속적으로 누적해줘야함. 1 7 19 37 ...

while room > count:
    count += 6 * floor
    floor += 1

print(floor)