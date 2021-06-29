room = int(input())

floor = 1
count = 1

# 층 마다 6의 배수의 만큼의 방을 갖고 있다.
# 6의 배수씩 더해줘서 층수 찾기
while room > count:
    count += 6 * floor
    floor += 1

print(floor)