def han(n):
    h = 0
    if n < 100:
        h = n
    else:
        for i in range(100, n + 1):
            a = i // 100             # 백의 자리
            b = (i % 100) // 10      # 십의 자리
            c = i % 10       # 일의 자리
            for j in range(5):
                if a + j == b:
                    if b + j == c:
                        h += 1
                
                elif a - j == b:
                    if b - j == c:
                        h += 1
        h = 99 + h
    return h

n = int(input())

print(han(n))