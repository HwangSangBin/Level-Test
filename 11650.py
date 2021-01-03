import sys

num = int(sys.stdin.readline())
part_total = []

for i in range(num):        # part = list(map(int, sys.stdin.readline().split()))
    part_total.append(list(map(int, sys.stdin.readline().split())))

for i in range(num):
    for j in range(i + 1, num):
        if part_total[i][0] > part_total[j][0]:
            temp = part_total[i]
            part_total[i] = part_total[j]
            part_total[j] = temp

        elif part_total[i][0] == part_total[j][0]:
            if part_total[i][1] > part_total[j][1]:
                temp = part_total[i]
                part_total[i] = part_total[j]
                part_total[j] = temp

for i in range(num):
    print("{0} {1}".format(part_total[i][0], (part_total[i][1])))