num1, num2 = input().split()

num1 = num1[::-1]
num2 = num2[::-1]

print(max(int(num1), int(num2)))