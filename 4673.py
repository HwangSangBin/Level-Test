num_list = []
def 
    for  i in range(1, 10001):
        total = i
        while True:
            total += (i % 10)
            if i // 10 != 0:
                i = i // 10
                continue
            elif i // 10 == 0:
                i = i // 10
                break
        num_list.append(total)

for  i in range(1, 10001):
    if (i not in num_list):
        print(i)

# numbers = set(range(1,10001))
# remove_set = set() #생성자가 있는 숫자를 집합으로 묶음 -> 차집합을 사용하기 위해
# for num in numbers:
#    for i in str(num): #숫자를 자릿수대로 분류하려면 str
#      num += int(i) #생성자 있는 숫자 골라냄
#     remove_set.add(num) #골라낸 숫자를 생성자가 있는 숫자의 집합으로 이동 .add() -> 집합에 요소 추가

# self_number = numbers - remove_set #1~10000까지 숫자 중 생성자 있는 숫자 제거
# for i in sorted(self_number):
#    print (i)