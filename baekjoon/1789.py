S = int(input())
sum = 0
cnt = 0

for i in range(1, S+1):
    sum = sum + i
    cnt += 1
    if(sum>S):
        cnt -=1
        break
print(cnt)