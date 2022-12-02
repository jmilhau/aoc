#!/usr/bin/env python3

s = {}
s['AX']=3+1
s['AY']=6+2
s['AZ']=0+3
s['BX']=0+1
s['BY']=3+2
s['BZ']=6+3
s['CX']=6+1
s['CY']=0+2
s['CZ']=3+3

with open("inputs/i2a.txt") as file:
    lines = file.readlines()

m = 0
for l in lines:
    i = l[:-1].split()
    m += s[i[0]+i[1]]
print(m)


s = {}
s['AX']=0+3
s['AY']=3+1
s['AZ']=6+2
s['BX']=0+1
s['BY']=3+2
s['BZ']=6+3
s['CX']=0+2
s['CY']=3+3
s['CZ']=6+1

with open("inputs/i2b.txt") as file:
    lines = file.readlines()

m = 0
for l in lines:
    i = l[:-1].split()
    m += s[i[0]+i[1]]
print(m)
