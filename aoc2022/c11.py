#!/usr/bin/env python3

object = [
    [64, 89, 65, 95],
    [76, 66, 74, 87, 70, 56, 51, 66],
    [91, 60, 63],
    [92, 61, 79, 97, 79],
    [93, 54],
    [60, 79, 92, 69, 88, 82, 70],
    [64, 57, 73, 89, 55, 53],
    [62]
]

inspect = [
    lambda a : a * 7,
    lambda a : a + 5,
    lambda a : a * a,
    lambda a : a + 6,
    lambda a : a * 11,
    lambda a : a + 8,
    lambda a : a + 1,
    lambda a : a + 4
]

test = [
    lambda a : [1,4][a%3==0],
    lambda a : [3,7][a%13==0],
    lambda a : [5,6][a%2==0],
    lambda a : [6,2][a%11==0],
    lambda a : [7,1][a%5==0],
    lambda a : [0,4][a%17==0],
    lambda a : [5,0][a%19==0],
    lambda a : [2,3][a%7==0]
]

score = [0,0,0,0,0,0,0,0]
cooldown = lambda a: int(a/3)

#20 rounds
for r in range(0,20):
    # 8 monkeys
    for m in range(0,8):
        while(object[m]):
            i = object[m].pop(0)
            #print(" Round",r,"Monkey",m,"Item",i)
            score[m]+=1
            next = cooldown(inspect[m](i))
            object[test[m](next)].append(next)

score.sort(reverse=True)
print("Part 1",score[0]*score[1])

object = [
    [64, 89, 65, 95],
    [76, 66, 74, 87, 70, 56, 51, 66],
    [91, 60, 63],
    [92, 61, 79, 97, 79],
    [93, 54],
    [60, 79, 92, 69, 88, 82, 70],
    [64, 57, 73, 89, 55, 53],
    [62]
]

score = [0,0,0,0,0,0,0,0]
cooldown = lambda a: a%(3*13*2*11*5*17*19*7)

#10000 rounds
for r in range(0,10000):
    # 8 monkeys
    for m in range(0,8):
        while(object[m]):
            i = object[m].pop(0)
            print(" Round",r,"Monkey",m,"Item",i)
            score[m]+=1
            next = cooldown(inspect[m](i))
            object[test[m](next)].append(next)

score.sort(reverse=True)
print("Part 2",score[0]*score[1])
