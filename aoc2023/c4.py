#!/usr/bin/env python3

with open("inputs/i4a.txt") as file:
    lines = file.readlines()

count = [1] * len(lines)
nbr = 0
score = 0
i = 0 
for l in lines:
    nbr = 0
    l = l.replace("  "," ").rstrip()
    temp = l.split(": ")
    temp = temp[1].split(" | ")
    a = [int(i) for i in temp[0].split(" ")] 
    b = [int(i) for i in temp[1].split(" ")]
    nbr = sum([ 1 if a[i] in b else 0 for i in range(len(a))])
    if nbr > 0:
        score += pow(2, nbr-1)
        for j in range(nbr):
            count[i+j+1] += 1*count[i]
    nbr = 0
    i+=1
print(score)
print(sum(count))