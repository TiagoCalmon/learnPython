myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
#
aux=[]
#z=0
for z, i in enumerate(myList):
    if i == myList[-1]:
        break
    listaux = myList[:]
    w=z+1
    for j in listaux[z+1:]:
        if i == j:
            if w not in aux:
                aux.append(w)
        w += 1
    #z += 1

aux.sort()
aux = aux[::-1]
print(aux)
for i in aux:
    del myList[i]
    
print("The list with unique elements only:")
print(myList)
len