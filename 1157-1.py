str_list = input().upper()

unique_list = list(set(str_list))
count_list = []

for i in unique_list:
    count_list.append(str_list.count(i))

if (count_list.count(max(count_list)) > 1):
    print("?")
else:
    print(unique_list[count_list.index(max(count_list))])