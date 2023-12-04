#!/usr/bin/env python3
with open("inputs/i12a.txt") as file:
    lines = file.read().splitlines()

map = []
heat = []
backlog = {}
backlog2 = {}

start = 0,0
end = 0,0

m = []
h = []

y = 0
for l in lines:
    x = 0
    for i in l:
        if i == "E":
            end = x,y
            m.append("z")
            h.append(1000000)
        elif i == "a":
            m.append(i)
            h.append(1000000)
            backlog2[(x,y)]=0
        elif i == "S":
            start = x,y
            m.append("a")
            h.append(0)
        else:
            m.append(i)
            h.append(1000000)
        x+=1
    map.append(m)
    heat.append(h)
    m = []
    h = []
    y+=1

def isValid(x,y,a,b,score):
    if (x+a) < 0 or (y+b) < 0 or (x+a)>= len(heat[0]) or (y+b)>=len(heat):
        return False
    if score+1 >= heat[y+b][x+a]:
        return False
    if ord(map[y+b][x+a]) - ord(map[y][x]) > 1:
        return False
    else:
        return True

backlog[start]=0
s = sorted(backlog.items(), key=lambda kv: kv[1])
while(s):
    current = s[0]
    if len(s)==1 and current==end:
        break
    backlog.pop(current[0])
    score = current[1]
    x = current[0][0]
    y = current[0][1]
    for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
        if isValid(x,y,a,b,score):
            backlog[(x+a,y+b)]=score+1
            heat[y+b][x+a]=score+1
    s = sorted(backlog.items(), key=lambda kv: kv[1])
print("Part 1",heat[end[1]][end[0]])

scores = {}
scores[start] = heat[end[1]][end[0]]

for start in backlog2.keys():
    backlog = {}
    backlog[start]=0
    for j in range(0,len(heat)):
        for i in range(0,len(heat[j])):
            heat[j][i]=1000000

    s = sorted(backlog.items(), key=lambda kv: kv[1])
    while(s):
        current = s[0]
        if len(s)==1 and current==end:
            break
        backlog.pop(current[0])
        score = current[1]
        x = current[0][0]
        y = current[0][1]
        for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
            if isValid(x,y,a,b,score):
                backlog[(x+a,y+b)]=score+1
                heat[y+b][x+a]=score+1
        s = sorted(backlog.items(), key=lambda kv: kv[1])
    scores[start] = heat[end[1]][end[0]]

s = sorted(scores.items(), key=lambda kv: kv[1])
print("Part 2",s[0][1])
