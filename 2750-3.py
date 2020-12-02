
def divided(list, left, right):
    low = left + 1
    high = right
    pivot = list[left]

    while (low < high):
        while (low <= right) and (list[low] < pivot):
            low += 1

        while (high >= left) and (list[high] > pivot):
            high -= 1
    
        if (low < high):
            temp = list[low]
            list[low] = list[high]
            list[high] = temp
        
        # 여기까지 한 사이클 당 하나씩 바뀐다.
        # 이해하니까 개신기하네 ㄹㅇ;
    
    temp = list[left]
    list[left] = list[high]
    list[high] = temp

    return high

def quick(list, left, right):
    if (left < right):
        cicle = divided(list, left, right)

        quick(list, left, cicle - 1)
        quick(list, cicle + 1, right)



N = int(input())

num_list = []

for i in range(N):
    number = int(input())
    num_list.append(number)

quick(num_list, 0, N - 1)

for k in range(N):
    print(num_list[k])