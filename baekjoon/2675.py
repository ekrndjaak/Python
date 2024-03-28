import sys
read = sys.stdin.readline

t = int(read())

for i in range(t):
    r, s = map(str,read().split())
    
    s = list(s)

    for char in s:
        print(char * int(r), end="")
    print()