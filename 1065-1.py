num = int(input())

def hansu(num):
    count = 0
    for i in range(1, num + 1):
        num_list = []
        d = []
        for h in str(i):
            num_list.append(int(h))
            length = len(num_list)
        if length == 1:
            count += 1
        for k in range(length):
            if k == length - 1:
                break
            else:
                d.append(num_list[k] - num_list[k + 1])
        if len(set(d)) != 1:
            count += 0
        else:
            count += 1
    return count

print(hansu(num))