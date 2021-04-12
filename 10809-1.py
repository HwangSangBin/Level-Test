Alpabet = input()

for i in range(ord("a"), ord("a") + (ord("z") - ord("a")) + 1):
    print(Alpabet.find(chr(i)), end = " ")