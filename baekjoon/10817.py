a, b, c = map(int, input().split())

tmp = [0]

while(True):
    if a>=b and a>=c:
        if b>=c:
            print(b)
            break
        if c>=b:
            print(c)
            break
        if c>=a:
            print(a)
            break
    if b>=a and b>=c:
        if a>=c:
            print(a)
            break
        if c>=a:
            print(c)
            break
        if c>=b:
            print(b)
            break
    if c>=a and c>=b:
        if a>=b:
            print(a)
            break
        if b>=a:
            print(b)
            break
        if(b>=a):
            print(c)
            break