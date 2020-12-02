def selction(list, num):
    # 최솟값을 옮기고 그 다음 인덱스부터 최솟값을 찾아야함.
    for j in range(num):
        # 여기서 최솟값을 찾고 인덱스를 옮겨야함.
        least = j
        for h in range(j, num):
            if list[h] < list[least]:
                least = h

        # least를 j번째로 옮겨줘야지
        a = list[j]
        list[j] = list[least]
        list[least] = a

N = int(input())

num_list = []

for i in range(N):
    num = int(input())
    num_list.append(num)

selction(num_list, N)

for k in range(N):
    print(num_list[k])