a = input()

for i in range(26):
    b = a.find(chr(97 + i))
    print(b, end = " ")