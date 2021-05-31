const, change, price= map(int, input().split())

if(change >= price):
    print(-1)
else:
    print(const // (price - change) + 1)