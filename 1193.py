num = int(input())

line = 1        # 사선

# 층수 정하기
while num > line:
    num -= line
    line += 1 

# 짝수일 때는 분자는 line값부터 감소, 분모는 1부터 증가
if line % 2 == 0:
    mom = num
    son = line - num + 1

# 홀수일 때는 분자는 1부터 증가, 분모는 line값부터 감소
else:
    mom = line - num + 1
    son = num

print(mom, '/', son, sep="")