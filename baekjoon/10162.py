T = int(input())

times = [300, 60, 10]

count = [0, 0, 0]

for i in range(3):
    count[i] = T // times[i]
    T %= times[i]
if T != 0:
    print(-1)
else:
    print(count[0], count[1], count[2])