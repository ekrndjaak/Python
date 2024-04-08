T = int(input())

ch = 100
sang = 100

for i in range(T):
    A, B = map(int, input().split())
    if A>B:
        sang -= A
    elif A<B:
        ch -= B
    else:
        A = 0
        B = 0

print(ch)
print(sang)
