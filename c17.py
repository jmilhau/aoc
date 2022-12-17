#!/usr/bin/env python3
import functools

with open("inputs/i17a.txt") as file:
    lines = file.read().splitlines()
wind = []
for l in lines:
    wind += l

shapes = []
#|..X@@@.|
shape = {}
shape["n"] = "-"
shape["s"] = [(0,0),(1,0),(2,0),(3,0)]
shape["<"] = [(-1,0)]
shape[">"] = [(4,0)]
shape["d"] = [(0,-1),(1,-1),(2,-1),(3,-1)]
shapes.append(shape)

#|...@...|
#|..@@@..|
#|..x@...|
shape = {}
shape["n"] = "+"
shape["s"] = [(1,0),(0,1),(1,1),(2,1),(1,2)]
shape["<"] = [(0,0),(-1,1),(0,2)]
shape[">"] = [(2,0),(3,1),(2,2)]
shape["d"] = [(1,-1),(0,0),(2,0)]
shapes.append(shape)

#|....@..|
#|....@..|
#|..X@@..|
shape = {}
shape["n"] = "L"
shape["s"] = [(0,0),(1,0),(2,0),(2,1),(2,2)]
shape["<"] = [(-1,0),(1,1),(1,2)]
shape[">"] = [(3,0),(3,1),(3,2)]
shape["d"] = [(0,-1),(1,-1),(2,-1)]
shapes.append(shape)

#|..@....|
#|..@....|
#|..@....|
#|..X....|
shape = {}
shape["n"] = "|"
shape["s"] = [(0,0),(0,1),(0,2),(0,3)]
shape["<"] = [(-1,0),(-1,1),(-1,2),(-1,3)]
shape[">"] = [(1,0),(1,1),(1,2),(1,3)]
shape["d"] = [(0,-1)]
shapes.append(shape)

#|..@@...|
#|..X@...|
shape = {}
shape["n"] = "o"
shape["s"] = [(0,0),(0,1),(1,0),(1,1)]
shape["<"] = [(-1,0),(-1,1)]
shape[">"] = [(2,0),(2,1)]
shape["d"] = [(0,-1),(1,-1)]
shapes.append(shape)

board = {(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),(6,-1)}

def maxy(board):
    return max([y for x,y in board])

def colision(center,s,direction):
    for x,y in s[direction]:
        if (x+center[0],y+center[1]) in board:
            return True
        elif x+center[0]<0 or x+center[0]>6 or y+center[1]<0:
            return True
    return False

def move(c,direction):
    if direction == "<":
        return (c[0]-1,c[1])
    elif direction == ">":
        return (c[0]+1,c[1])
    elif direction == "d":
        return (c[0],c[1]-1)

def printb(board,points=[],center=(0,0)):
    for y in range(maxy(board)+7,-1,-1):
        print("|",end="")
        p = []
        for point in points:
            p.append((point[0]+center[0],point[1]+center[1]))
        for x in range(0,7):
            if (x,y) in p:
                print("@",end="")
            elif (x,y) in board:
                print("#",end="")
            else:
                print(" ",end="")
        print("|")
    print("|",end="")
    for x in range(0,7):
        print("#",end="")
    print("|")
    print("")

size = 0
delta = []

i = 0
while(True):
    s = shapes.pop(0)
    shapes.append(s)
    center = (2,4+maxy(board))
    tbc = True
    while(tbc):
        w = wind.pop(0)
        wind.append(w)
        if not colision(center,s,w):
            center = move(center,w)
        if not colision(center,s,"d"):
            center = move(center,"d")
        else:
            i+=1
            for point in s["s"]:
                board.add((center[0]+point[0],center[1]+point[1]))
                tbc = False
            delta.append(maxy(board)+1-size)
            size = maxy(board)+1
    if i>8000:
        break

print("Part 1",sum(delta[0:2022]))

found = False
# Looking for offset
for j in range(1,500,1):
    # Looking for cycle
    for i in range(1,2000,1):
        if len(delta[j:j+i]*4) == len(delta[j:j+4*i]):
            if delta[j:j+i]*4 == delta[j:j+4*i]:
                found = True
                cycle = i
                offset = j
                print(" offset",j,"cycle",i)
                break
    if found:
        break

print("  Height offset",sum(delta[0:offset]))
o = sum(delta[0:offset])
print("  Height cycle",sum(delta[offset:offset+cycle]))
c = sum(delta[offset:offset+cycle])

n = (1000000000000 - offset) // cycle
r = (1000000000000 - offset) % cycle
print("Part 2",(n*c)+sum(delta[0:offset+r]))
