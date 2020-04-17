bigfile = open("C:\\Users\\vadog\\Work\\Work\\SpanishWords\\jehle_verb_database.csv.txt", "r")
thefile = bigfile.read()
thefile = thefile.split("\n")
thefile.pop(0)
data = []
csfile = []
for i in range(len(thefile)):
    csfile.append(thefile[i].split(","))
for i in range(len(thefile)):
    if i == 0:
        
