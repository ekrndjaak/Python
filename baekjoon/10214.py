T = int(input())
for _ in range(T): 
    sum_Y = 0 
    sum_K = 0 
    
    for _ in range(9):
        Y, K = map(int, input().split())
        sum_Y += Y
        sum_K += K

    if sum_Y > sum_K:
        print("Yonsei")
    elif sum_Y < sum_K:
        print("Korea")
    else:
        print("Draw")
