num_3 = []

for i in range(int(input())):
    num_2 = list(map(int, input().split()))
    total = 0
    for j in range(len(num_2)):
        total += num_2[j]
    student_num = num_2[0]
    del num_2[0]
    total -= student_num
    average = total / student_num
    # 평균 구하기
    num_4 = 0
    for h in range(student_num):
        if num_2[h] > average:
            num_3.append(num_2[h])
            num_4 += 1
    print(str("%.3f" % round(num_4 / student_num * 100, 3)) + "%")
