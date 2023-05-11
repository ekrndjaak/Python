#create list
animals = ["사자", "호랑이","고양이","강아지"]

#data print
name = animals[3]

#data insert
animals.append("하마")
animals.append(1)


#data delate
del animals[-1] #last data delate

#list slicing
slicing = animals[1:3]

#list length
length = len(animals)

#list sort
animals.sort(reverse=True) #reverse=true -->> 오름차순

print(animals)
print(slicing)
print(length)