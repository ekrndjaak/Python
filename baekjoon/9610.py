T = int(input())
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
AXIS = 0
for i in range(T):
    num1 , num2 = map(int,input().split())
    if num1 == 0 or num2 == 0:
        AXIS += 1
    elif num1 > 0 and num2 > 0:
        cnt1 += 1
    elif num1 < 0 and num2 > 0:
        cnt2 += 1
    elif num1 < 0 and num2 < 0:
        cnt3 += 1
    elif num1 > 0 and num2 < 0:
        cnt4 += 1    

print("Q1:", cnt1)
print("Q2:", cnt2)
print("Q3:", cnt3)
print("Q4:", cnt4)
print("AXIS:", AXIS)
