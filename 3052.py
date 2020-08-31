b = []
for i in range(10):
    a = int(input())
    b.append(a)
    
d = []
for i in range(10):
    c = b[i] % 42
    d.append(c)
d = set(d)
print(len(d))