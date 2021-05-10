num_total = int(input())

for j in range(num_total):
    num, num_list = input().split()
    for i in range(len(num_list)):
        print(num_list[i] * int(num), end ="")
    print("")