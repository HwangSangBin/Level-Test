a = int(input())
b = list(map(int, input().split()))
d = 0
for i in range(len(b)):
    c = b[i] / max(b) * 100
    d += c
print(d / len(b))