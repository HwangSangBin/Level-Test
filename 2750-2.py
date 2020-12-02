def bubble(list, num):
    j = num
    while j != -1:
        for h in range(j - 1):                      # 맨마지막 자리는 안해도 돼
            if num_list[h] > num_list[h + 1]:       # 앞에 거가 뒤에 거 보다 클 때
                num_replace = num_list[h]           
                num_list[h] = num_list[h + 1]       # 뒤에 거를 앞자리에 넣어
                num_list[h + 1] = num_replace       # 앞에 거를 뒷자리에 넣어
        j -= 1                                      # 뒤에서부터 채워오니까 하나씩 빼줘야지


N = int(input())

num_list = []

for i in range(N):
    num = int(input())
    num_list.append(num)

bubble(num_list, N)

for k in range(N):
    print(num_list[k])