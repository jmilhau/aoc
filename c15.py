#!/usr/bin/env python3
import multiprocessing
import functools

with open("inputs/i15a.txt") as file:
    lines = file.read().splitlines()

sensor = {}
beacon = []

@functools.cache
def mdist(x,y,u,v):
    return abs(x-u)+abs(y-v)

@functools.cache
def inrange(x,y):
    ss = sensor
    for s in ss.items():
        if s[1] >= mdist(x,y,s[0][0],s[0][1]):
            return s
    return False

for l in lines:
    l = l.replace("Sensor at ","").replace(" closest beacon is at ","")
    l = l.replace(" ","").replace("x=","").replace("y=","").replace(":",",").split(",")
    x,y,u,v = int(l[0]),int(l[1]),int(l[2]),int(l[3])
    sensor[(x,y)]=mdist(x,y,u,v)
    beacon.append((u,v))

b1 = [ k[0]-v for k,v in sensor.items() ]
b2 = [ k[0]+v for k,v in sensor.items() ]
xmin,xmax = min(b1),max(b2)

y = 2000000
counter = 0
closes = {}

for s in sensor.items():
    if mdist(s[0][0],y,s[0][0],s[0][1]) <= s[1]:
        closes[(s[0][0],s[0][1])]=s[1]
s=sensor
sensor = closes
for x in range(xmin-10,xmax+10):
    if inrange(x,y) and (x,y) not in beacon:
        counter +=1

print("Part 1",counter)
sensor = s

def run(start):
    print("Processing from ",start)
    for y in range(start,start+100000):
        x = 0
        if y%10000 == 0:
            print(y)
        while(x<4000001):
            if inrange(x,y):
                s = inrange(x,y)
                x += s[1]-mdist(x,y,s[0][0],s[0][1])
            elif (not (inrange(x,y))) and (x,y) not in beacon:
                print("Part 2",x,y,(x*4000000+y))
                exit()
            x+=1

run(3200000)
#Found after bruteforce that
#Part 2 3340224 3249595 13360899249595
#Trying to optimize now
