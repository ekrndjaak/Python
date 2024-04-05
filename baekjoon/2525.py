h, m = map(int, input().split())
wh = int(input())

mh = m + wh
while(mh >= 60):
    if(mh >= 120):
        mh = mh - 60
        h += 1
    if(mh >= 60):
        mh = mh - 60
        h += 1
    if(mh <60):
        break
    

if(h >= 24):
    h = h-24

print(h, mh)