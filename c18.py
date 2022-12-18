#!/usr/bin/env python3
import functools

import sys

#Don't try this at home ;)
sys.setrecursionlimit(2048)

cubes = {}
with open("inputs/i18a.txt") as file:
    lines = file.read().splitlines()
for l in lines:
    l = l.split(",")
    cubes[(int(l[0]),int(l[1]),int(l[2]))] = 6

def calc_adj(cc):
    for c in cc.keys():
        x,y,z = c
        cc[c] = 6
        if (x+1,y,z) in cc.keys():
            cc[c] -= 1
        if (x-1,y,z) in cc.keys():
            cc[c] -= 1
        if (x,y+1,z) in cc.keys():
            cc[c] -= 1
        if (x,y-1,z) in cc.keys():
            cc[c] -= 1
        if (x,y,z+1) in cc.keys():
            cc[c] -= 1
        if (x,y,z-1) in cc.keys():
            cc[c] -= 1

calc_adj(cubes)
print("Part 1",sum(cubes.values()))

minx,maxx = min([x for x,y,z in cubes.keys()]), max([x for x,y,z in cubes.keys()])
miny,maxy = min([y for x,y,z in cubes.keys()]), max([y for x,y,z in cubes.keys()])
minz,maxz = min([z for x,y,z in cubes.keys()]), max([z for x,y,z in cubes.keys()])

outside = set()
visited = set()

@functools.cache
def is_outside(f):
    global outside
    global visited
    if f in outside:
        return True
    if f[0]<minx or f[0]>maxx or f[1]<miny or f[1]>maxy or f[2]<minz or f[2]>maxz:
         outside.add(f)
         return True
    x,y,z = f
    neigh = {(x-1,y,z),(x,y-1,z),(x,y,z-1),(x+1,y,z),(x,y+1,z),(x,y,z+1)}
    neigh = neigh
    neigh =  neigh - set(cubes.keys())
    if x+1 > maxx:
        neigh = neigh - {(x+1,y,z)}
    if x-1 < minx:
        neigh = neigh - {(x-1,y,z)}

    if y+1 > maxy:
        neigh = neigh - {(x,y+1,z)}
    if y-1 < miny:
        neigh = neigh - {(x,y-1,z)}

    if z+1 > maxz:
        neigh = neigh - {(x,y,z+1)}
    if z-1 < minz:
        neigh = neigh - {(x,y,z-1)}

    r = False
    if len(neigh)==0:
        return r
    for n in neigh:
        if n in outside:
            r = True
        elif n not in visited:
            visited.add(n)
            r = is_outside(n)
        if r:
            outside.add(f)
            return r

def add_neigh(p):
    if p not in cubes.keys():
        cubes[p]=0
        x,y,z = p
        neigh = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]
        neigh = [n for n in neigh if n not in cubes.keys()]
        #If I add a cube as lava, hence the neighbours should also be lava
        for n in neigh:
            add_neigh(n)


#Pre fill of outside cubes to speed up is_outside function
x,y,z = minx-1,miny-1,minz-1
outside.add((x,y,z))
neigh = {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}
neigh = {n for n in neigh if n not in cubes.keys()}
todo = neigh
while(todo):
    x,y,z = todo.pop()
    outside.add((x,y,z))
    neigh = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]
    neigh = [n for n in neigh if n not in cubes.keys()]
    neigh = {n for n in neigh if n not in outside}
    if x+1 > maxx+1:
        neigh = neigh - {(x+1,y,z)}
    if x-1 < minx-1:
        neigh = neigh - {(x-1,y,z)}

    if y+1 > maxy+1:
        neigh = neigh - {(x,y+1,z)}
    if y-1 < miny-1:
        neigh = neigh - {(x,y-1,z)}

    if z+1 > maxz+1:
        neigh = neigh - {(x,y,z+1)}
    if z-1 < minz-1:
        neigh = neigh - {(x,y,z-1)}
    todo = todo.union(neigh)

#Computing the cubes that are inside, and adding them as lava cubes
for x in range(minx,maxx+1,1):
    for y in range(miny,maxy+1,1):
        for z in range(minz,maxz+1,1):
            if (x,y,z) not in cubes.keys() and not is_outside((x,y,z)) :
                #print("FOUND one",(x,y,z))
                add_neigh((x,y,z))


calc_adj(cubes)
print("Part 2",sum(cubes.values()))
