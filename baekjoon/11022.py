a = int(input())

case = []

for _ in range(a):
    A, B = map(int, input().split())
    case.append((A, B))

for i, (A, B) in enumerate(case, start=1):
    print("Case #{}: {} + {} = {}".format(i, A, B, A + B))