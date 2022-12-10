#!/usr/bin/env python3

with open("inputs/i10a.txt") as file:
    lines = file.read().splitlines()

actions = []
for l in lines:
    match l.split()[0]:
        case "noop":
            actions.append(0)
        case "addx":
            actions.append(0)
            actions.append(int(l.split()[1]))

#Part 1
x = 1
f = 0
clock = 0

for a in actions:
    clock += 1
    if clock in [20,60,100,140,180,220]:
        f += x*clock
    x += a

print("Part 1",f)

#Part 2
x = 1
f = 0
clock = 0
sprite = range(0,3)
crt_draws = -1
screen = []
line = []

for a in actions:
    clock += 1
    crt_draws += 1
    if crt_draws in sprite:
        line.append("█")
    else:
        line.append(" ")
    if len(line) == 40:
        screen.append(line)
        line = []
        crt_draws = -1
    x += a
    sprite = range(x-1,x+2)

print("Part 2")
for l in screen:
    print("".join(l))
