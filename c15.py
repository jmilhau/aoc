#!/usr/bin/env python3
import multiprocessing
import functools

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

sensor = {}
beacon = []

with open("inputs/i15a.txt") as file:
    lines = file.read().splitlines()

for l in lines:
    l = l.replace("Sensor at ","").replace(" closest beacon is at ","")
    l = l.replace(" ","").replace("x=","").replace("y=","").replace(":",",").split(",")
    x,y,u,v = int(l[0]),int(l[1]),int(l[2]),int(l[3])
    sensor[(x,y)]=mdist(x,y,u,v)
    beacon.append((u,v))

def scanrange(start):
    slice = 200000
    print("🆕 Processing",start,start+slice)
    for y in range(start,start+slice):
        x = 0
        while(x<4000001):
            if inrange(x,y):
                s = inrange(x,y)
                x += s[1]-mdist(x,y,s[0][0],s[0][1])
            elif (not (inrange(x,y))) and (x,y) not in beacon:
                return x,y,x*4000000+y
            x+=1
    print("✅ Completed",start,start+slice)
    return 0

if __name__ == "__main__":

    b1 = [ k[0]-v for k,v in sensor.items() ]
    b2 = [ k[0]+v for k,v in sensor.items() ]
    xmin,xmax = min(b1),max(b2)

    y = 2000000
    counter = 0

    for x in range(xmin-10,xmax+10):
        if inrange(x,y) and (x,y) not in beacon:
            counter +=1

    print("🎉 Part 1",counter)

    pool = multiprocessing.Pool(multiprocessing.cpu_count()-1)
    # Starting from 4M as I know that the result is closer ;)
    # But you could start from 0 and go incremental instead
    # Doing chuncks of 200k
    ans = pool.imap_unordered(scanrange, range(3800000, -1, -200000))
    # imap_unordered allows to get access to the answers as soon as available
    # but not in the initial order of jobs (we do not care of order here)
    for a in ans:
        if a!=0:
            print("🎉 Part 2",a[0],a[1],a[2])
            # Calling exit() to stop burning CPU on other tasks
            exit()
