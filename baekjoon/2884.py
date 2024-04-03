H, M = map(int,input().split())
if M-45 >= 0:
    M -= 45
    print(H, M)
elif M-45 < 0:
    if H != 0:
        H -= 1
        M += 15
        print(H, M)
    elif H == 0:
        H = 23
        M += 15
        print(H, M)