#!/usr/bin/env python3

import functools

with open("inputs/i5a.txt") as file:
    lines = file.readlines()

f0,f1,f2,f3,f4,f5,f6 = [],[],[],[],[],[],[]
dico = {"sts":f0,"stf":f1,"ftw":f2,"wtl":f3,"ltt":f4,"tth":f5,"htl":f6}

current = ""
for l in lines:
    if l.startswith("\n"):
        current = ""
    elif l.startswith("seed-to-soil map:"):
        current = "sts"
    elif l.startswith("soil-to-fertilizer map:"):
        current = "stf"
    elif l.startswith("fertilizer-to-water map:"):
        current = "ftw"
    elif l.startswith("water-to-light map:"):
        current = "wtl"
    elif l.startswith("light-to-temperature map:"):
        current = "ltt"
    elif l.startswith("temperature-to-humidity map:"):
        current = "tth"
    elif l.startswith("humidity-to-location map:"):
        current = "htl"
    elif l.startswith("seeds: "):
        temp = l.rstrip().replace("seeds: ","")
        seeds = [int(i) for i in temp.split(" ")]
    else:
        temp = l.rstrip()
        f = [int(i) for i in temp.split(" ")]
        dico[current].append(f)

def applyone(f,i):
    for g in f:
        if g[1] <= i < g[1]+g[2]:
            return i-g[1]+g[0]
    return i

@functools.cache
def applyall(i):
    j = i
    for f in [f0,f1,f2,f3,f4,f5,f6]:
        j = applyone(f,j)
    return j

def applyonereverse(f,i):
    for g in f:
        if g[0] <= i < g[0]+g[2]:
            return i-g[0]+g[1]
    return i

@functools.cache
def applyallreverse(i):
    j = i
    for f in [f6,f5,f4,f3,f2,f1,f0]:
        j = applyonereverse(f,j)
    return j

s = [ applyall(s) for s in seeds ]
print(min(s))

stemp = iter(seeds)
seeds2 = []
for a,b in zip(stemp,stemp):
    seeds2.append(range(a,a+b))

i = -1
stop = False
while not stop:
    i+=1
    for u in seeds2:
        if applyallreverse(i) in u:
            stop = True
            continue
    
print("Found seed {} in minimal location {}".format(applyallreverse(i),i))