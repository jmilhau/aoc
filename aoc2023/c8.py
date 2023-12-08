#!/usr/bin/env python3

import itertools
import math

with open("inputs/i8a.txt") as file:
    lines = file.readlines()

graph = {}

p = [ 1 if i == "R" else 0 for i in lines[0].rstrip() ] 

for l in lines[2:]:
    graph[l[0:3]]=(l[7:10],l[12:15])

def find_path(start="AAA",stop="ZZZ",maxcycle=10000000,pp=p):
    pattern = itertools.cycle(pp)
    current = start
    steps = 0
    for n in pattern:
        if current == stop:
            return steps
        elif steps > maxcycle:
            return None
        steps +=1
        current = graph[current][n]

print(find_path())

starts = [ i for i in graph.keys() if i[-1]=="A"] 
stops = [ i for i in graph.keys() if i[-1]=="Z"] 

found = []

for a in starts:
    for b in stops:
        n = find_path(start=a,stop=b)
        if not n is None:
            found.append(n)

print(math.lcm(*found))