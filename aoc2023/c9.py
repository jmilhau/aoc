#!/usr/bin/env python3

with open("inputs/i9a.txt") as file:
    lines = file.readlines()

inputs = []

for l in lines:
    s = [int(i) for i in l.rstrip().split(" ")]
    inputs.append(s)

output = []
for inp in inputs:
    t = []
    t.append(inp)
    while any(t[-1]):
        q = []
        for i in range(len(t[-1])-1):
            q.append(t[-1][i+1]-t[-1][i])
        t.append(q)
    output.append(t)

for o in output:
    for i in range(len(o)-1,0,-1):
        a = o[i][-1]+o[i-1][-1]
        o[i-1].append(a)

answer = [ output[i][0][-1] for i in range(len(output))]
print(sum(answer))

for o in output:
    for i in range(len(o)-1,0,-1):
        a = o[i-1][0]-o[i][0]
        o[i-1].insert(0,a)

print(output[-1])
answer = [ output[i][0][0] for i in range(len(output))]
print(answer)
print(sum(answer))