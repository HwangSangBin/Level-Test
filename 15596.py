def solve(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum

n = int(input())
num_list = []

for i in range(0, n):
    num_list.append(int(input()))

print(solve(num_list))