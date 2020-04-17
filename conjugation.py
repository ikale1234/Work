import os
import random
import verborganizer
import sys
points= 0

def getlist():
    if len(sys.argv) == 1:
        alldata = verborganizer.build("C:\\Users\\vadog\\Work\\Work\\SpanishWords")
        listdata = alldata[0]
    elif len(sys.argv) == 2:
        try:
            listdata = verborganizer.build(sys.argv[1])
        except FileNotFoundError:
            print("That is an invalid directory.")
            quit()
    else:
        print("That is an invalid directory.")
        quit()
    return listdata

listdata = getlist()

def getgamevalues():
    r = []
    a = -1
    for b in range (6):
        if b == 0:
            i = random.randrange((len(listdata)))
        j = random.randrange(2,5)
        if b > a:
            k = random.randrange(0,5)
        word = listdata[i][j][k]
        if b == 0:
                x, y, z = i, j, k
                if listdata[i][2][k] == listdata[i][3][k] or listdata[i][3][k] == listdata[i][4][k]:
                    a = 1
                else:
                    a = 2
        # checks repeating
        for c in range(len(r)):
            while word == r[c]:
                j = random.randrange(2,5)
                if b > a:
                    k = random.randrange(0,5)
                word = listdata[i][j][k]
                c = 0
        r.append(word)
    right = r[0]
    random.shuffle(r)
    
    return x, y, z, r, right

def getquestionvals():
    if j == 2:
        tense = "present"
    if j == 3:
        tense = "preterite"
    if j == 4:
        tense = "imperfect"
    if k == 0:
        form = "yo"
    if k == 1:
        form = "tu"
    if k == 2:
        form = random.choice(["el", "ella", "usted"])
    if k == 3:
        form = "nosotros"
    if k == 4:
        form = random.choice(["ellos","ellas","ustedes"])
    return tense, form

def getinput():
    guess = input("What is the "+tense+" tense of "+listdata[i][0][0]+" in the "+form+"? \nA: "+r[0]+"\nB: "+r[1]+ "\nC: "+ r[2]+ "\nD: "+ r[3]+ "\nE: "+ r[4]+"\nF: "+ r[5]+"\n")
    if right == r[0]:
        let = "A"
    if right == r[1]:
        let = "B"
    if right == r[2]:
        let = "C"
    if right == r[3]:
        let = "D"
    if right == r[4]:
        let = "E"
    if right == r[5]:
        let = "F"
    return guess, let

def checkifright():
    global points
    if guess == let or guess == let.lower():
        points+=1
        print("You got a point.")
    else:

        print("You got that question wrong.")

for a in range(10):
 
    i, j, k, r, right = getgamevalues()
    
    tense, form = getquestionvals()
    
    guess, let = getinput()
    
    checkifright()
            

print("You got", points, "/ 10 right.")

