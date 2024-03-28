tmp = input().split()

result = int(tmp[0])
for i in range(1, len(tmp), 2):
    if tmp[i] == '+':
        result += int(tmp[i+1])
    elif tmp[i] == '*':
        result *= int(tmp[i+1])

print(result)