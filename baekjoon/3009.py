x1, y1 = map(int, input().split()) #A
x2, y2 = map(int, input().split()) #B
x3, y3 = map(int, input().split()) #C
a = [x1, x2, x3]
b = [y1, y2, y3]
c = sorted(a)
d = sorted(b)
if c[0] == c[1]:
    a4 = c[2]
else:
    a4 = c[0]
if d[0] == d[1]:
        b4 = d[2]
else:
        b4 = d[0]
print(a4, b4, end= ' ')