import os
import random
import verborganizer
import sys
if len(sys.argv) == 1:
    listdata = verborganizer.build("C:\\Users\\vadog\\Work\\Spanish")
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
i = random.randrange((len(listdata)))
j = random.randrange(2,4)
k = random.randrange(0,4)
points= 0
for a in range(10):
    word = listdata[i][j][k]
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
        form = "el/ella/usted"
    if k == 3:
        form = "nosotros"
    if k == 4:
        form = "ellos/ellas/ustedes"
    
    guess = input("What is the spanish word for "+listdata[i][1][0]+"? ")

    if guess == listdata[i][0][0]:
        guess2 = input("What is the "+tense+" tense of "+listdata[i][0][0]+" in the "+form+"? ")
        if guess2 == word:
            points+=1
            i = random.randrange((len(listdata)))
            j = random.randrange(2,4)
            k = random.randrange(0,4)
            print("You got a point.")
        else:
            print("You got that question wrong.")
        
    else:
        print("You got that question wrong.")
        

print("You got", points, "/ 10 right.")

