# 재귀함수
def factorial(num):

    if num == 0:
        return 1

    else:
        return num * factorial(num - 1)

number = int(input())

print(factorial(number))

# 반복문

number = int(input())

count = 0
total = 1

while count < number:
    count += 1
    total *= count

print(total)