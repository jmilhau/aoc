#!/usr/bin/env python3

values = list(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))
size = len(values)

class Hand: 
    def __init__(self, hand, bet): 
        self.h = hand
        self.b = bet
        self.count = [0] * size
        for i in self.h:
            self.count[values.index(i)] += 1        

    def type(self):
        #print("Type of {} with {}".format(self.h,self.count))
        if 5 in self.count:
            return 6
        elif 4 in self.count:
            return 5
        elif 3 in self.count and 2 in self.count:
            return 4
        elif 3 in self.count:
            return 3
        elif self.count.count(2) == 2:
            return 2
        elif 2 in self.count:
            return 1
        else:
            return 0
        
    def __lt__(self, obj): 
        if self.type() < obj.type():
            return True
        elif self.type() > obj.type():
            return False
        else:
            for i,j in zip(self.h,obj.h):
                if values.index(i) < values.index(j):
                    return True
                if values.index(i) > values.index(j):
                    return False
            return False
        
    def __eq__(self, obj): 
        return (self.h == obj.h) 
  
    def __repr__(self): 
        return "{} ({})".format(self.h,self.b) 
  
allhands = []
with open("inputs/i7a.txt") as file:
    lines = file.readlines()
for l in lines:
    s = l.rstrip().split(" ")
    allhands.append(Hand(s[0],int(s[1])))
    
n =sorted(allhands)
scores = [ (i+1)*n[i].b for i in range(len(n)) ]
print(sum(scores))


values2 = list(reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))

class Hand2(Hand): 
    def __init__(self, hand, bet): 
        self.h = hand
        self.b = bet
        self.count = [0] * size
        for i in self.h:
            self.count[values2.index(i)] += 1   
        if self.count[0] > 0:
            for i in range(len(self.count)-1,-1,-1):
                if self.count[i] == max(self.count[1:]):
                    self.count[i]+= self.count[0]
                    self.count[0] = 0
                    break

    def __lt__(self, obj): 
        if self.type() < obj.type():
            return True
        elif self.type() > obj.type():
            return False
        else:
            for i,j in zip(self.h,obj.h):
                if values2.index(i) < values2.index(j):
                    return True
                if values2.index(i) > values2.index(j):
                    return False
            return False

allhands2 = []

for l in lines:
    s = l.rstrip().split(" ")
    allhands2.append(Hand2(s[0],int(s[1])))

n = sorted(allhands2)
scores = [ (i+1)*n[i].b for i in range(len(n)) ]
print(sum(scores))
