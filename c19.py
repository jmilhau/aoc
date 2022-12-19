#!/usr/bin/env python3
import functools

with open("inputs/i19a.txt") as file:
    lines = file.read().splitlines()

blueprints = []
for l in lines:
    out = []
    l = l.split(":")
    l = l[1].split(".")
    l.pop()
    for i in l:
        a,b,c = 0,0,0
        j = i.split("costs ")
        j = j[1].split(" and ")
        for k in j:
            m = k.split(" ")
            if k[-1] == "n":
                a = int(m[0])
            elif k[-1] == "y":
                b = int(m[0])
            elif k[-1] == "e":
                c = int(m[0])

        out.append((0,a,b,c))
    o = tuple(out)
    blueprints.append(o)


def cmp(a):
    return tuple([a[0][i]+a[1][i] for i in range(0,4)])

def mapprod(blueprint):
    r = [(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)]
    bp = [ (blueprint[i],r[i]) for i in range(len(l))]
    # Adding do nothing to the list of things we can do for  blueprint
    bp.append(((0,0,0,0),(0,0,0,0)))
    return bp

def canbedone(r,c):
    return all([r[i]>=c[i] for i in range(0,4)])

def bestgeodes(blueprint, t):
    robots = (0,0,0,0)
    ressources = (0,0,0,1)
    todo = [(robots,ressources)]
    for time in range(0,t):
        todonext = []
        for ressources, robots in todo:
            for cost, production in blueprint:
                if canbedone(ressources,cost):
                    nressources = tuple([ressources[i]+robots[i]-cost[i] for i in range(0,4)])
                    nrobots = tuple([robots[i]+production[i] for i in range(0,4)])
                    todonext.append((nressources,nrobots))
        todonext.sort(key=cmp,reverse=True)
        # Destroying the todo that are unlikely to help us (low cmp(todo[i]) value)
        todo = todonext[0:10000]
    return max(todo,key=cmp)[0][0]

q1 = 0
for i in range(0,len(blueprints)):
    b = mapprod(blueprints[i])
    q1 += bestgeodes(b,24) * (i+1)

print("Part 1",q1)

q2 = 1
for i in range(0,3):
    b = mapprod(blueprints[i])
    q2 *= bestgeodes(b,32)
print("Part 2",q2)
