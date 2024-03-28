h, m, s = map(int,input().split())
ai = int(input())
s = ai + s

while(s >= 60):
    if(s >= 60):
        s -= 60
        m += 1
    if s <= 59:
        break

while(m >= 60):
    if m >= 60:
        m -= 60
        h += 1
    if m <= 59:
        break
while(h>=24):
    if h >= 24:
        h -= 24
    if h <=23:
        break
    
print(h, m ,s)
