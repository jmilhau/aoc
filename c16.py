#!/usr/bin/env python3
import multiprocessing
import functools

with open("inputs/i16a.txt") as file:
    lines = file.read().splitlines()

values = {}
edges = {}
neigh = {}

@functools.cache
def name(v,n):
    return min(v,n)+max(v,n)

# dijkstra helper #1
def addToGraph(v,flow,next):
    values[v] = flow
    neigh[v] = next
    for n in next:
        edges[name(v,n)]=1

# dijkstra helper #1
def findmin(q,heat):
    m = 10000
    r = None
    for s in q:
        if heat[s] < m:
            m = heat[s]
            r = s
    return r

# dijkstra main function
def dijkstra(edg,neigh,start,store):
    heat = {k:1000 for k in neigh.keys()}
    heat[start] = 0
    q = list(neigh.keys())
    while len(q)!= 0:
        s1 = findmin(q,heat)
        #print(s1,q)
        q.remove(s1)
        for s2 in neigh[s1]:
            if heat[s2] > heat[s1] + 1:
                heat[s2] = heat[s1] + 1
    for k,v in heat.items():
        store[name(k,start)] = v

for l in lines:
    #Valve SW has flow rate=0; tunnels lead to valves LX, LD
    l = l.replace("Valve","").replace(" has flow rate=",",")
    l = l.replace(" tunnel leads to valve ","")
    l = l.replace(" tunnels lead to valves ","").replace(" ","").replace(";",",")
    l = l.split(",")
    v,flow,next = l[0],int(l[1]),l[2:]
    addToGraph(v,flow,next)

short = {}
for start in neigh.keys():
    dijkstra(edges,neigh,start,short)

v2 = {k:v for (k,v) in values.items() if v >0}
valves = v2.keys()
nbvalves = len(v2)

@functools.cache
def explore(start,time,done2,currentscore):
    #print("Explore",start,time,done,currentscore)
    done = [done2[i:i+2] for i in range(0, len(done2), 2)]
    if time <= 0:
        return currentscore,done
    r = []
    for e in valves:
        if e not in done:
            if time-short[name(start,e)]-1 <= 0:
                continue
            d = "".join(done)+e
            r.append((e,time-short[name(start,e)]-1,d,currentscore + (time-short[name(start,e)]-2)*v2[e]))
    if len(r)==0:
        return currentscore,done
    m = 0
    for arg in r:
        n = explore(*arg)
        if n[0]>m:
            m = n[0]
            d = n[1]
    return m,d

@functools.cache
def split2(done2):
    return sorted([done2[i:i+2] for i in range(0, len(done2), 2)])

@functools.cache
def maxremain(vs,t):
    vs = split2(vs)
    a = 0
    for v in [w for w in valves if w not in vs]:
        a+=v2[v]
    return a*(t-1)

@functools.cache
def explore2(s1,s2,t1,t2,done2,currentscore):
    global maxscore
    if t1<t2:
        return explore2(s2,s1,t2,t1,done2,currentscore)
    if currentscore+maxremain(done2,t1) < maxscore:
        return 0,""
    done = split2(done2)
    if len(done) == nbvalves:
        return currentscore,done2
    r = []
    u = "".join(done)
    for e in [f for f in valves if (f not in done) and (t1-1>short[name(s1,f)])]:
        d = u+e
        r.append((e,s2,t1-short[name(s1,e)]-1,t2,d,currentscore + (t1-short[name(s1,e)]-2)*v2[e]))
        if t2-short[name(s2,e)]-1 <= 0:
            continue
        r.append((s1,e,t1,t2-short[name(s2,e)]-1,d,currentscore + (t2-short[name(s2,e)]-2)*v2[e]))
    if len(r)==0:
        return currentscore,done2
    m = 0
    for arg in r:
        n = explore2(*arg)
        if n[0]>m:
            m = n[0]
            d = n[1]
        if m > maxscore:
            maxscore = m
            print("🎉 Better score found",m,[d[i:i+2] for i in range(0, len(d), 2)])
    return m,d

a,b = explore("AA",31,"",0)
print("Part 1",a,b)

maxscore = a
a,b = explore2("AA","AA",27,27,"",0)
print("Part 2",a,[b[i:i+2] for i in range(0, len(b), 2)])
