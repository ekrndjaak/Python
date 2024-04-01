num = []
cnt = 0

while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    elif num1>num2:
        num.append("Yes")
        cnt += 1
    elif num1<=num2:
        num.append("No")
        cnt += 1
for i in range(cnt):
    print(num[i])

