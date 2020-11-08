num, max_num = input().split()
list_num = list((input().split()))
total_num = []

num = int(num)
max_num = int(max_num)

for i in range(num):
    for j in range(1, num):
        for k in range(2, num):
            if ((i == j) or (i == k) or (j == k)):
                pass

            else:
                plus_num = int(list_num[i]) + int(list_num[j]) + int(list_num[k])
                
                if plus_num > max_num:
                    pass

                else:
                    total_num.append(plus_num)

total_num = list(set(total_num))


print(max(total_num))