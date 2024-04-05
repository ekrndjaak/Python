T = int(input())
arr = []
sum = 0
cnt = 0
for i in range(T):
    ox = input()
    arr.append(ox)

for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        if arr[i][j] == 'O':
            cnt+=1
            sum+=cnt
        elif arr[i][j] == "X":
            cnt = 0
    print(sum)
    cnt=0
    sum=0


