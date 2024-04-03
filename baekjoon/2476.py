T = int(input())
game = []
total = 0
for i in range(T):
    a, b, c = map(int,input().split())
    if a == b == c:
        total = 10000 + (a * 1000)
    elif a == b or a == c or b == c:
        if a == b == c:
            total = 10000 + (a * 1000)
        else:
            num = a if a == b or a == c else b
            total = 1000 + (num * 100)
    else:
        max_num = max(a, b, c)
        total = max_num * 100
    game.append(total)
    total = 0 # total 초기화

for _ in range(T):
    game.sort(reverse=True)

print(game[0])