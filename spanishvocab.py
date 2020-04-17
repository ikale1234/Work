# initialization
import os
import random
import verborganizer
import sys
vocablist = []
points= 0

# functions
def getlist():
    if len(sys.argv) == 1:
        listdata = verborganizer.build("C:\\Users\\vadog\\Work\\Work\\SpanishWords")
    elif len(sys.argv) == 2:
        print ()
        try:
            listdata = verborganizer.build(sys.argv[1])
        except FileNotFoundError:
            print("That is an invalid directory.")
            quit()
    return listdata

def convertlist(x, y):
    for a in range(len(y[0])):
        x.append(y[0][a][0][0])
    for a in range(len(y[1])):
        x.append(y[1][a][0][0])

def getgamevalues():
    r = random.sample(vocablist, 5)
    word = random.choice(r)
    for i in range(len(listdata[0])):
        if word == listdata[0][i][0][0]:
            eng = listdata[0][i][1][0]
    for i in range(len(listdata[1])):
        if word == listdata[1][i][0][0]:
            eng = listdata[1][i][1][0]
    return word, eng, r


def getuserguess():
    guess = input("What is the spanish word for "+eng+"? \nA: "+r[0]+"\nB: "+r[1]+ "\nC: "+ r[2]+ "\nD: "+ r[3]+ "\nE: "+ r[4]+"\n")
    if word == r[0]:
        let = "A"
    if word == r[1]:
        let = "B"
    if word == r[2]:
        let = "C"
    if word == r[3]:
        let = "D"
    if word == r[4]:
        let = "E"
    return let, guess

def checkifright():
    global points
    if guess == let or guess == let.lower():
        points+=1
        print("You got a point.")
    else:
        print("You got that question wrong.")

# game
listdata = getlist()
convertlist(vocablist, listdata)

for e in range(10):
    word, eng, r = getgamevalues()
    
    let, guess = getuserguess()

    checkifright()
  
print("You got", points, "/ 10 right.")

