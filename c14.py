#!/usr/bin/env python3
import functools

with open("inputs/i14a.txt") as file:
    lines = file.read().splitlines()

cave = {}
rocks = []

for l in lines:
    for coord in l.split(" -> "):
        c=coord.split(",")
        x = c[0]
        y = c[1]
        rocks.append((x,y))
        if len(rocks)>1:
            u = int(rocks[-1][0])
            v = int(rocks[-2][0])
            m = int(rocks[-1][1])
            n = int(rocks[-2][1])
            if u == v:
                for y in range(min(m,n),(max(m,n)+1)):
                    cave[(u,y)] = "R"
            elif m == n:
                for x in range(min(u,v),(max(u,v)+1)):
                    cave[(x,m)] = "R"
    rocks = []

cave2 = cave.copy()

xx = [x for x,y in cave.keys()]
yy = [y for x,y in cave.keys()]
minx,maxx=min(xx),max(xx)
miny,maxy=0,max(yy)
sandx,sandy = 500,0

def canMove(tx,ty):
    return (tx,ty) not in cave.keys()

while (minx <= sandx <= maxx) and (miny <= sandy <=maxy) :
    if canMove(sandx,sandy+1):
        sandy+=1
    elif canMove(sandx-1,sandy+1):
        sandx-=1
        sandy+=1
    elif canMove(sandx+1,sandy+1):
        sandx+=1
        sandy+=1
    else:
        cave[(sandx,sandy)]="S"
        sandx,sandy = 500,0
print("Part 1",sum(1 for v in cave.values() if v == "S"))

#Reinitializing cave
cave = cave2

#Adding floor, not to infinity though
for x in range(minx-maxy-3,maxx+maxy+3):
    cave[(x,maxy+2)]="F"

while (minx-(maxy+3) <= sandx <= maxx+maxy+3) and (miny <= sandy <=maxy+3) :
    if canMove(sandx,sandy+1):
        sandy+=1
    elif canMove(sandx-1,sandy+1):
        sandx-=1
        sandy+=1
    elif canMove(sandx+1,sandy+1):
        sandx+=1
        sandy+=1
    else:
        cave[(sandx,sandy)]="S"
        # If we complete filling the cave, break the loop
        if sandx == 500 and sandy == 0:
            break
        sandx,sandy = 500,0

print("Part 2",sum(1 for v in cave.values() if v == "S"))
