def insertion(list, num):
    for j in range(1, num):
        key = num_list[j]       # 얘를 조사해야돼

        h = j - 1               # 인덱스값이 작은 값부터 비교해야지

        while ((h != -1) and (list[h] > key)):
            list[h + 1] = list[h]       # key에 값을 저장해둬서 h + 1에 전에 있던 값을 고려하지 않아도 된다. 
            h -= 1
        
        list[h + 1] = key               # while문을 처리할 때 값이 구해져도 h -= 1을 수행한 상태여서 +1을 해줘야해

N = int(input())

num_list = []

for i in range(N):
    num = int(input())
    num_list.append(num)

insertion(num_list, N)

for k in range(N):
    print(num_list[k])