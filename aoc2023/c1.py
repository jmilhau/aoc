#!/usr/bin/env python3

with open("inputs/i1a.txt") as file:
    lines = file.readlines()

s = []
for l in lines:
    n = [c for c in l if c.isdigit()]
    s.append(int(n[0]+n[-1]))
print(sum(s))


d = { "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

s = []
for l in lines:
    m = [[x if (x := "".join([v for k, v in d.items() if l[i:].startswith(k)])) else l[i] for i in range(len(l))] ]
    m = str(m)
    n = [c for c in m if c.isdigit()]
    s.append(int(n[0]+n[-1]))
print(sum(s))
