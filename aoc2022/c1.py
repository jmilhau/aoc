#!/usr/bin/env python3

with open("inputs/i1a.txt") as file:
    lines = file.readlines()

c = 0
elves = []
for l in lines:
    if l == "\n":
        elves.append(c)
        c = 0
    else:
        c += int(l[:-1])

print(max(elves))


with open("inputs/i1b.txt") as file:
    lines = file.readlines()

c = 0
elves = []
for l in lines:
    if l == "\n":
        elves.append(c)
        c = 0
    else:
        c += int(l[:-1])

elves.sort(reverse=True)
print(sum(elves[0:3]))
