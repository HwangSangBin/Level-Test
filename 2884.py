H, M = input().split()
H = int(H)
M = int(M)
if M < 45:
    if H == 0:
        H = 23
    elif H != 0:
        H -= 1
    M = M + 15
    print(H, M)
elif M >= 45:
    M = M - 45
    print(H, M)