#!/usr/bin/env python3

# Very lazy, hardcoding puzzle inputs
stacks = {}
stacks[1] = ["J","H","G","M","Z","N","T","F"]
stacks[2] = ["V","W","J"]
stacks[3] = ["G","V","L","J","B","T","H"]
stacks[4] = ["B","P","J","N","C","D","V","L"]
stacks[5] = ["F","W","S","M","P","R","G"]
stacks[6] = ["G","H","C","F","B","N","V","M"]
stacks[7] = ["D","H","G","M","R"]
stacks[8] = ["H","N","M","V","Z","D"]
stacks[9] = ["G","N","F","H"]

# Input modified to only contain move lines
with open("inputs/i5a.txt") as file:
    lines = file.readlines()
for l in lines:
    word = l.split()
    move, fr, to = int(word[1]),int(word[3]),int(word[5])
    for i in range(move):
        stacks[to].append(stacks[fr].pop())
for i in range(1,10):
    print(stacks[i][-1],end="")
print("")

stacks = {}
stacks[1] = ["J","H","G","M","Z","N","T","F"]
stacks[2] = ["V","W","J"]
stacks[3] = ["G","V","L","J","B","T","H"]
stacks[4] = ["B","P","J","N","C","D","V","L"]
stacks[5] = ["F","W","S","M","P","R","G"]
stacks[6] = ["G","H","C","F","B","N","V","M"]
stacks[7] = ["D","H","G","M","R"]
stacks[8] = ["H","N","M","V","Z","D"]
stacks[9] = ["G","N","F","H"]

with open("inputs/i5a.txt") as file:
    lines = file.readlines()
for l in lines:
    word = l.split()
    move, fr, to = int(word[1]),int(word[3]),int(word[5])
    # Appending then poping from temp equals to moving crates in order
    temp = []
    for i in range(move):
        temp.append(stacks[fr].pop())
    for i in range(move):
        stacks[to].append(temp.pop())
for i in range(1,10):
    print(stacks[i][-1],end="")
print("")
