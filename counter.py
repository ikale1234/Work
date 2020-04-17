what = input("Please enter the name of a txt file and directory if not in Work:")
thefile = open(what, "r")
string = thefile.read()
thefile.close()
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
wcount = 0
lcount = 1
aword = False
for i in range(len(string)):
    if string[i] in (letters) and aword == False:
        aword = True
    if aword:
        if string[i] not in (letters):
            aword = False
            wcount +=1
    if i == len(string)-1 and string[i] in (letters):
        wcount +=1
    if string[i] == "\n":
        lcount+=1
print ("In the file " +what+", there are", wcount,"words and",lcount,"lines.")
