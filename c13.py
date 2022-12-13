#!/usr/bin/env python3
import functools

with open("inputs/i13a.txt") as file:
    lines = file.read().splitlines()

sign = lambda x: int(x and (1, -1)[x<0])

def goodOrder(a,b):
    #Returns -1 if bad order, 1 if good order and 0 if inconclusive
    if isinstance(a,int) and isinstance(b,int):
        return sign(b-a)
    elif isinstance(a,list) and isinstance(b,list):
        for i in range(len(a)):
            r = 0
            if i < len(b):
                r = goodOrder(a[i],b[i])
            else:
                r = -1
                break
            if r != 0:
                return r
        if len(a)==len(b):
            return 0
        elif len(a)<len(b):
            return 1
        elif len(a)>len(b):
            return -1
    elif isinstance(a,int) and isinstance(b,list):
        return goodOrder([a],b)
    elif isinstance(a,list) and isinstance(b,int):
        return goodOrder(a,[b])
    else:
        print("Nooooooooo",a,b)
        return 0

score = []
for i in range(0,len(lines)//3):
    a = eval(lines[i*3])
    b = eval(lines[(i*3)+1])
    score.append((0,i+1)[goodOrder(a,b)==1])

print("Part 1",sum(score))

todo = [eval(l) for l in lines if l!=""]
todo.append([[6]])
todo.append([[2]])
todo.sort(reverse=True,key=functools.cmp_to_key(goodOrder))
print("Part 2",(todo.index([[2]])+1)*(todo.index([[6]])+1))
