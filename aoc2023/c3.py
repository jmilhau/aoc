#!/usr/bin/env python3

with open("inputs/i3a.txt") as file:
    lines = file.readlines()

s = []
for l in lines:
    l = l.replace("\n",".")
    s.append(l)
t = "." * len(s[0])
s.insert(0,t)
s.append(t)

def keepme(i,js,je):
    if s[i][js-1] != ".":
        return True
    if s[i][je] != ".":
        return True            
    rx = [i-1,i+1]
    ry = range(js-1,je+1)
    for x in rx:
        for y in ry:
            if s[x][y] != ".":
                return True
    return False
    

i,j,answer = 0,0,0
while i < len(s):
    while j < len(s[i]):
        if s[i][j].isnumeric():
            savej = j
            while s[i][j].isnumeric():
                j+=1
            if keepme(i,savej,j):
                answer += int(s[i][savej:j])
        j+=1
    j = 0
    i+=1
print(answer)

def findnumbers(i,j):
    
    return []

i,j,answer2 = 0,0,0
while i < len(s):
    while j < len(s[i]):
        if s[i][j]=="*":
            found = findnumbers(i,j)
            if found == []:
                print("WONT KEEP Line {} value {} ".format(i,j))
            else:
                answer2 += sum(found)
        j+=1
    j = 0
    i+=1
print(answer2)