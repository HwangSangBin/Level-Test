num_list = []

for  i in range(1, 10001):
    total = i
    while True:
        total += (i % 10)
        i = i // 10
        if i // 10 != 0:
            continue
        elif i // 10 == 0:
            break
    num_list.append(total)

for  i in range(1, 10001):
    if (i not in num_list):
        print(i)