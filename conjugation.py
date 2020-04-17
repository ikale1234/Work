import os
import random
import verborganizer
import sys
if len(sys.argv) == 1:
    alldata = verborganizer.build("C:\\Users\\vadog\\Work\\SpanishWords")
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
game = True

points= 0
for a in range(10):
    r = []
    for b in range (5):
        i = random.randrange((len(listdata)))
        j = random.randrange(2,4)
        k = random.randrange(0,4)
        word = listdata[i][j][k]
        for c in range(len(r)):
            while word == r[c]:
                i = random.randrange((len(listdata)))
                j = random.randrange(2,4)
                k = random.randrange(0,4)
                word = listdata[i][j][k]
        r.append(word)
    right = random.choice(r)
    for d in range(len(listdata)):
        for e in range(3):
            for f in range(5):
                if right == listdata[d][e+2][f]:
                    i = d
                    j = e+2
                    k = f
        

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
        form = "ellos/ellas/ustedes"
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

    

    
    guess = input("What is the "+tense+" tense of "+listdata[i][0][0]+" in the "+form+"? \nA: "+r[0]+"\nB: "+r[1]+ "\nC: "+ r[2]+ "\nD: "+ r[3]+ "\nE: "+ r[4]+"\n")
    if guess == let or guess == let.lower():
        points+=1
        print("You got a point.")
    else:

        print("You got that question wrong.")
            

print("You got", points, "/ 10 right.")

