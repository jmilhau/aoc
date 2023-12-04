#!/usr/bin/env python3

with open("inputs/i2a.txt") as file:
    lines = file.readlines()

s = []
dico = { "red":0, "green":0, "blue":0}
for l in lines:
    current = dico.copy()
    temp = l.rstrip()
    temp = temp.split(": ")
    temp = temp[1].split("; ")
    for t in temp:
        t = iter(t.split(", "))
        for u in t:
            u = iter(u.split(" "))
            for d0,d1 in zip(u,u):
                current[d1] = max(int(d0),current[d1])
                
    s.append(current)
nbr = 0
nbr2 = 0
for i in range(len(s)):
    if s[i]["red"] <= 12 and s[i]["green"] <= 13 and s[i]["blue"] <= 14:
        nbr+= i+1
    nbr2 += s[i]["red"] * s[i]["green"] * s[i]["blue"]
print(nbr)
print(nbr2)
