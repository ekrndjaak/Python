T = int(input())
case = []

for _ in range(T):
    r, e, c = map(int,input().split())
    case.append((r,e,c))

for i in range(T):
    r, e, c = case[i]
    if r < e - c:
        print("advertise")
    elif r == e - c:
        print("does not matter")
    elif r > e - c:
        print("do not advertise")
