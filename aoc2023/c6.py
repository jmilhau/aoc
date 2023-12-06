#!/usr/bin/env python3

import math

with open("inputs/i6a.txt") as file:
    lines = file.readlines()

ins = []

for l in lines:
    s = l.rstrip().split(" ")
    ins.append([ int(i) for i in s[1:] if i!=''])
time,distance = ins[0], ins[1]

answer = [0,0,0,0]
x = 0
for a,b in zip(time,distance):
    for i in range(a+1):
        if (a-i)*i > b:
            answer[x] += 1
    x+=1
print(math.prod(answer))

time = int(lines[0].rstrip().replace("Time:","").replace(" ",""))
distance = int(lines[1].rstrip().replace("Distance:","").replace(" ",""))

answer = 0
a,b = time,distance
for i in range(a+1):
    if (a-i)*i > b:
        answer += 1
print(answer)
