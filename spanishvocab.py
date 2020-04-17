import os
import random
import verborganizer
import sys
if len(sys.argv) == 1:
    listdata = verborganizer.build("C:\\Users\\vadog\\Work\\SpanishWords")
elif len(sys.argv) == 2:
    print ()
    try:
        listdata = verborganizer.build(sys.argv[1])
    except FileNotFoundError:
        print("That is an invalid directory.")
        quit()
elif len(sys.argv) == 3:
    try:
        listdata = verborganizer.build(sys.argv[1]) + verborganizer.build(sys.argv[2])
    except FileNotFoundError:
        print("That is an invalid directory.")
        quit()
game = True
vocablist = []
for a in range(len(listdata[0])):
    vocablist.append(listdata[0][a][0][0])
for a in range(len(listdata[1])):
    vocablist.append(listdata[1][a][0][0])
points= 0
for e in range(10):
 
    r = random.sample(vocablist, 5)
    word = random.choice(r)
    for i in range(len(listdata[0])):
        if word == listdata[0][i][0][0]:
            eng = listdata[0][i][1][0]
    for i in range(len(listdata[1])):
        if word == listdata[1][i][0][0]:
            eng = listdata[1][i][1][0]

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

    if guess == let or guess == let.lower():
        points+=1
        print("You got a point.")
    else:
        print("You got that question wrong.")
        

print("You got", points, "/ 10 right.")

