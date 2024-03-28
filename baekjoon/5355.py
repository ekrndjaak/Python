T = int(input())

for _ in range(T):
    tmp = input().split()

    result = float(tmp[0])
    for i in range(1, len(tmp)):
        if tmp[i] == '@':
            result *= 3
        elif tmp[i] == '%':
            result += 5
        elif tmp[i] == '#':
            result -= 7
    