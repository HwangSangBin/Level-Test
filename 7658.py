people = int(input())
weight_all = []
height_all = []

for i in range(people):
    weight, height = map(int, input().split())

    weight_all.append(weight)
    height_all.append(height)

for j in range(people):
    rank = 1

    for h in range(people):
        if (weight_all[j] < weight_all[h]) and (height_all[j] < height_all[h]):
            rank += 1
    
    print(rank, end = " ")