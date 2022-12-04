#!/usr/bin/env python3

def inside(ra, rb, cont=True):
    return (int(ra[0]) >= int(rb[0]) and int(ra[1]) <= int(rb[1])
        ) or ( cont and inside(rb,ra,False) )

def over(ra, rb):
    return (int(rb[1]) - int(ra[0])) * (
        int(ra[1]) - int(rb[0]) ) >= 0

m = 0
with open("inputs/i4a.txt") as file:
    lines = file.readlines()
for l in lines:
    a,b = [ i.split("-") for i in l.strip("\n").split(",")]
    m+=[0,1][inside(a,b)]
print(m)


m = 0
with open("inputs/i4b.txt") as file:
    lines = file.readlines()
for l in lines:
    a,b = [ i.split("-") for i in l.strip("\n").split(",")]
    m+=[0,1][over(a,b)]
print(m)
