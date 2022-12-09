#!/usr/bin/env python3

def moveHead(x,y,d):
    a,b=0,0
    match d:
        case "U":
            b = 1
        case "D":
            b = -1
        case "L":
            a = -1
        case "R":
            a = 1
    return (x+a,y+b)

def moveTail(hx,hy,tx,ty):
    if (abs(hx-tx) <= 1) and (abs(hy-ty) <= 1):
        #No need to change
        return (tx,ty)
    elif (hx-tx == 0):
        # Same x -> move 1 towards hy
        return (tx, (ty + (1 *((hy-ty>0)-(hy-ty<0)))))
    elif (hy-ty == 0):
        # Same y -> move 1 towards hx
        return ((tx + (1 *((hx-tx>0)-(hx-tx<0))),ty))
    else:
        # Need to move in diagonal
        return (tx + (1 *((hx-tx>0)-(hx-tx<0))),ty + (1 *((hy-ty>0)-(hy-ty<0))))

with open("inputs/i9a.txt") as file:
    lines = file.read().splitlines()

m = [{},{},{},{},{},{},{},{},{},{}]
knots = [(0,0)]*10
for i in range(0,10):
    m[i][knots[i]]=1

for l in lines:
    dir, nbr = l.split()
    nbr = int(nbr)
    for i in range(nbr):
        # move H in the direction dir
        knots[0] = moveHead(knots[0][0],knots[0][1],dir)
        for j in range(1,10):
            # call the tail catch-up for knot j
            knots[j] = moveTail(knots[j-1][0],knots[j-1][1],knots[j][0],knots[j][1])
            # Update the visited matrix
            m[j][knots[j]]=1

print("Part 1",len(m[1].keys()))
print("Part 2",len(m[9].keys()))
