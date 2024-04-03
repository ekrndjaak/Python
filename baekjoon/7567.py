stacks = input().strip()

height = 10 

for i in range(1, len(stacks)):
    if stacks[i] == stacks[i - 1]:
        height += 5
    else:
        height += 10

print(height)