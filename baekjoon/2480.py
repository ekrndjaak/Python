a, b, c = map(int,input().split())
total = 0

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

print(total)