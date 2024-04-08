T = int(input())

for _ in range(T):
    N = int(input())

    max_school = ""
    max_amount = -1

    for _ in range(N):
        school, amount = input().split()
        amount = int(amount) # 정수로 전환

        if amount > max_amount:
            max_amount = amount
            max_school = school
        
    print(max_school)