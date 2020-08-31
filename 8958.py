num = int(input())

total = 0
count = 0
for j in range(num):
    answer = input()
    for i in range(len(answer)):
        if answer[i] == "O":
            total += 1
            count += 1
            if i <= len(answer) - 2:
                for h in range(count):
                    if answer[i + 1] == "O":
                        total += 1
        elif answer[i] == "X":
            total += 0
            count = 0
    print(total)
    total = 0
    count = 0