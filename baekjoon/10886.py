T = int(input())
case = []
cnt = 0

for _ in range(T):
    n = int(input())
    case.append(n)

for i in range(T):
    n = case[i]
    if n == 1:
        cnt += 1

if T//2 < cnt:    
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")