string = input()
map1 = []
map2 = []
for i in range(len(string)):
    map1.append((string[i]))

for i in range(len(string) -1, -1 ,-1):
    map2.append((string[i]))

palimdrome = True
for i in range(len(string)):
    if map1[i] != map2[i]:
        palimdrome = False
        break

if palimdrome:
    print("1")
else:
    print("0")