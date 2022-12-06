#!/usr/bin/env python3

with open("inputs/i6a.txt") as file:
    lines = file.readlines()
l = lines[0]

for i in range(4,len(l)):
    if len(l[i-4:i]) == len(set(l[i-4:i])):
        print(i)
        break

for i in range(14,len(l)):
    if len(l[i-14:i]) == len(set(l[i-14:i])):
        print(i)
        break
