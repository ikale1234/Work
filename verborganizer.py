import os

def build(dir):
    verbbank = []
    nounbank = []
    wordbank = []
    verbs =  os.listdir(dir+"\\Verbs")
    nouns = os.listdir(dir+"\\Nouns")
    for i in range(len(verbs)):
        curfile = open(dir+"\\Verbs\\"+verbs[i], "r")
        templist = []


        for j in range(5):
            templist.append(curfile.readline()[:-1])
            templist[j] = templist[j].split(",")
        curfile.close()
        #check


        good = False
        if str(templist[1])[2] == "t" and str(templist[1])[3] == "o":           
            if len(templist[2]) == len(templist[3]) == len(templist[4]) == 5:
                good = True
        if good:
            verbbank.append(templist)
    for i in range(len(nouns)):
        curfile = open(dir+"\\Nouns\\"+nouns[i], "r")
        templist = []
        for j in range(2):
            templist.append(curfile.readline()[:-1])
            templist[j] = templist[j].split(",")
        curfile.close
        nounbank.append(templist)
    wordbank.append(verbbank)
    wordbank.append(nounbank)
    return wordbank



