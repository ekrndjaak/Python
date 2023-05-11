for i in range(1,6): #1,2,3,4,5 순서열
    print("*" * i)

print("==========\n")
for i in range(1,6):
    print("*" * (6-i))
print("==========\n")
for i in range(1,6):
    print(" " * (5-i) + "*" * i)
print("==========\n")
for i in range(1,6):
    print(" " * (i-1) + "*" * (6-i))