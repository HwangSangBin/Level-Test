num = int(input())
fake_num = num

setting = []
last_num = []
sum_num = 0

while (True):
    fake_num -= 1
    str_num = str(fake_num)

    for i in range(len(str_num)):                    # 숫자마다 자릿수 별 숫자 할당 
        setting_num = str_num[i]
        setting.append(int(setting_num))

    for j in range(len(setting)):                   # 자릿수 숫자들 + 그 숫자
        sum_num += setting[j]
    sum_num += fake_num

    if sum_num == num:
        last_num.append(fake_num)

    setting = []                                    # 초기화
    sum_num = 0

    if fake_num < num - (9 * len(str(num))):        # (9 * 자릿수) 이상 차이나는 수는 답이 될 수 없음 
        if last_num == []:
            last_num.append(0)                      # 값이 없을 때 0 넣음
        break

    elif fake_num == 0:                             # 일의 자리는 오류가 떠서 0일 때도 넣어줌
        if last_num == []:
            last_num.append(0)
        break


print(min(last_num))