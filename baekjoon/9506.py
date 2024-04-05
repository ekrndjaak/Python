n=0
while True:
    a=[]
    b=0
    n=int(input())
    if n == -1:
        break
    
    for x in range(1,n):
        if n%x==0:
            a.append(int(x))
    for i in a:
        b+=i
    if b==n:
        print("%d = " % b, end='')
        print(*a, sep=" + ")
    else:
        print('%d is NOT perfect.'%n)