n = int(input())
for i in range(1, n + 1):
    for r in range(n-1):    
        print("", end=" ")
    print("*"*i)
    n -=1