num = int(input())
str_list = []

for i in range(num):
    str_list.append(input())

str_list = set(str_list)
str_list = list(str_list)

num = len(str_list)

for i in range(num):
    for j in range(i + 1, num):
        if len(str_list[i]) > len(str_list[j]):
            temp = str_list[i]
            str_list[i] = str_list[j]
            str_list[j] = temp

        elif len(str_list[i]) == len(str_list[j]):
            for h in range(len(str_list[i])):
                if str_list[i][h] > str_list[j][h]:
                    temp = str_list[i]
                    str_list[i] = str_list[j]
                    str_list[j] = temp
for i in range(num):
    print(str_list[i])