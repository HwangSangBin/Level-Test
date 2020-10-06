Alpabet = input()
second = 0

for i in range(len(Alpabet)):
    if ord(Alpabet[i]) < 68:
        second += 3
    
    elif ord(Alpabet[i]) < 71:
        second += 4

    elif ord(Alpabet[i]) < 74:
        second += 5

    elif ord(Alpabet[i]) < 77:
        second += 6

    elif ord(Alpabet[i]) < 80:
        second += 7

    elif ord(Alpabet[i]) < 84:
        second += 8

    elif ord(Alpabet[i]) < 87:
        second += 9

    elif ord(Alpabet[i]) < 91:
        second += 10

print(second)