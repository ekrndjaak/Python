num = int(input())
c = 2

while num>1:
    if num %c == 0:
        print(c)
        num //= c
    else:
        c += 1