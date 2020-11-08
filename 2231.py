num = int(input())
fake_num = num

setting = []
last_num = []
sum_num = 0

while (True):
    fake_num -= 1
    str_num = str(fake_num)

    for i in range(len(str_num)):
        setting_num = str_num[i]
        setting.append(int(setting_num))

    for j in range(len(setting)):
        sum_num += setting[j]
    sum_num += fake_num

    if sum_num == num:
        last_num.append(fake_num)

    setting = []
    sum_num = 0

    if fake_num < num - (9 * len(str(num))):
        if last_num == []:
            last_num.append(0)

        break



print(min(last_num))