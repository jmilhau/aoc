#!/usr/bin/env python3

with open("inputs/i8a.txt") as file:
    lines = file.read().splitlines()

# Forest contains the parsed input
forest = []

# Map contains 0 if tree is not visible, 1 else
map = []

for l in lines:
    f = []
    m = []
    for i in l:
        f.append(int(i))
        m.append(0)
    forest.append(f)
    map.append(m)

# Fill map according to visbility status
for j in range(len(map)):
    top = -1
    for i in range(len(map[0])):
        if forest[j][i] > top:
            map[j][i] = 1
            top = forest[j][i]
    top = -1
    for i in range(len(map[0])-1,0,-1):
        if forest[j][i] > top:
            map[j][i] = 1
            top = forest[j][i]

for i in range(len(map[0])):
    top = -1
    for j in range(len(map)):
        if forest[j][i] > top:
            map[j][i] = 1
            top = forest[j][i]
    top = -1
    for j in range(len(map)-1,0,-1):
        if forest[j][i] > top:
            map[j][i] = 1
            top = forest[j][i]
# Sum map to know how many trees are visible (map contains 0 or 1)
print("Part 1",sum([sum(n) for n in map]))


# Reuse map to compute score for each tree
for j in range(len(map)):
    for i in range(len(map[0])):

        #Check to south
        south = 0
        top = -1
        for y in range(j+1,len(map)):
            south +=1
            if forest[y][i] >= forest[j][i]:
                break

        #Check to north
        north = 0
        for y in range(j-1,-1,-1):
            north +=1
            if forest[y][i] >= forest[j][i]:
                break

        #Check to east
        east = 0
        for x in range(i+1,len(map[0])):
            east +=1
            if forest[j][x] >= forest[j][i]:
                break

        #Check to west
        west = 0
        for x in range(i-1,-1,-1):
            west +=1
            if forest[j][x] >= forest[j][i]:
                break

        score = north * south * east * west
        map[j][i] = score

# Print max score
print("Part 2",max([max(n) for n in map]))
