#!/usr/bin/env python3

with open("inputs/i3a.txt") as file:
    lines = file.readlines()

m = 0
for l in lines:
    s1, s2 = l[:len(l)//2], l[len(l)//2:]
    y = [ c for c in s1 if c in s2 ][0]
    if ord(y)>=ord("a"):
        m += ord(y) - ord("a") + 1
    else:
        m += ord(y) - ord("A") + 27
print(m)

with open("inputs/i3b.txt") as file:
    lines = file.readlines()

m = 0
for i in range(0,len(lines)//3):
    s1, s2 , s3 = lines[3*i], lines[3*i+1], lines[3*i+2]
    y = [ c for c in s1 if c in s2 and c in s3 ][0]
    if ord(y)>=ord("a"):
        m += ord(y) - ord("a") + 1
    else:
        m += ord(y) - ord("A") + 27
print(m)
