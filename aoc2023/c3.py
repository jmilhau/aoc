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

def readnumber(i,savej):
    if not s[i][savej].isnumeric():
        return None
    j = savej
    while s[i][j].isnumeric():
        j+=1
    return int(s[i][savej:j])

def backtrack(i,j):
    if not s[i][j].isnumeric():
        return None
    y = j-1
    while s[i][y].isnumeric():
        y -= 1
    return (i,y+1)

def findnumbers(i,j):
    a = set()
    for x,y in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
        t =  backtrack(x,y)
        if t is not None:
            a.add(t)
    return list(a)


i,j,answer2 = 0,0,0
while i < len(s):
    while j < len(s[i]):
        if s[i][j]=="*":
            found = findnumbers(i,j)
            if len(found) == 2:
                t = readnumber(*found[0]) * readnumber(*found[1])
                answer2 += t
        j+=1
    j = 0
    i+=1
print(answer2)

