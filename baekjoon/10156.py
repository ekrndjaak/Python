K, N ,M = map(int,input().split())
sum = K * N
total_price = sum - M
if total_price<=0:
    print("0")
if total_price>0:
    print(total_price)