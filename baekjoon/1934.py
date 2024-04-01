T = int(input())

results = [] 

for _ in range(T):
    a, b = map(int, input().split())
    results.append((a, b))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for i, (a, b) in enumerate(results, start=1):
    print(lcm(a, b))
