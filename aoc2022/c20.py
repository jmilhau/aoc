#!/usr/bin/env python3
import functools

with open("inputs/i20test.txt") as file:
    lines = file.read().splitlines()

theList = []
theID = {}

i = 0
for l in lines:
    u = []
    u.append(int(l))
    theID[i]=id(u)
    theList.append(u)
    i+=1

#print(theList)
#print(theID)

def findID(i,l):
    for u in range(len(l)):
        if id(l[u]) == i:
            #print("Found you!",u,l[u])
            return u
    print("Not found!",i)
    return None

def popID(i,l):
    for u in range(len(l)):
        if id(l[u]) == i:
            return l.pop(u)
    print("Not found!",i)
    return None

zero = 0
for k, v in sorted(theID.items()):
    index = findID(v,theList)
    if theList[index] == [0]:
        zero = v
        continue
    item = popID(v,theList)
    where = (index+item[0]) % (len(theList))
    if where == 0:
        theList.append(item)
    else:
        theList.insert(where,item)

zi = findID(zero,theList)
one = theList[1+(1000 - zi)%len(theList)][0]
two = theList[1+(2000 - zi)%len(theList)][0]
three = theList[1+(3000 - zi)%len(theList)][0]
#print(theList)
print((one,two,three))
print(sum((one,two,three)))
