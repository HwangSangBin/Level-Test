kg = int(input())
count = []
number = 0

for i in range(kg // 3 + 1):
    for j in range(kg // 3 + 1):
        if (5 * i) + (3 * j) == kg:
            number = i + j
            count.append(number)

for h in range(len(count)):
    if count[h] < count[h - 1]:
        number = count[h]

if number == 0:
    number = -1

print(number)