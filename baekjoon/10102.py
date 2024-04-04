T = int(input())
case = []
cnta = 0
cntb = 0
vote = input()
for i in range(len(vote)):
    case.append((vote[i]))
for i in range(len(vote)):
    if vote[i] == "A":
        cnta += 1
    elif vote[i] == "B":
        cntb += 1
if cnta > cntb:
    print("A")
if cnta < cntb:
    print("B")
if cnta == cntb:
    print("Tie")