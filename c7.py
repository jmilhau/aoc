#!/usr/bin/env python3

with open("inputs/i7a.txt") as file:
    lines = file.readlines()

current = []
allfiles = {}
alldir = {}
alldir["/"] = -1

#Parsing the commands, directories and files
for l in lines:
    match l[:4]:
        case "$ cd":
            match l[5:7]:
                case "/\n":
                    current = []
                case "..":
                    current.pop()
                case _:
                    current.append(l[5:-1])
        case "$ ls":
            continue
        case "dir ":
            name = l[4:-1]
            path = "/".join(current)+"/"+name+"/"
            if path[0] != "/":
                path = "/"+path
            alldir[path]=-1
        case _:
            f = l.split()
            size = int(f[0])
            name = f[1][:-1]
            path = "/".join(current)+"/"+name
            if path[0] != "/":
                path = "/"+path
            allfiles[path] = size

#Computing size per folder
for folder in alldir.keys():
    size = 0
    for (k,v) in allfiles.items():
        if k.startswith(folder):
            size += v
    alldir[folder] = size

#Selecting folders with size <=100000
smallDir = { k:v for (k,v) in alldir.items() if v<=100000}
print("Part 1 ",sum(smallDir.values()))

#Selecting candidate for deletion
okDir = { k:v for (k,v) in alldir.items() if v>=30000000-(70000000-alldir["/"])}
print("Part 2 ",min(okDir.values()))
