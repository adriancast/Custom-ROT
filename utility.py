import sys #to get parameters
print "Parameters: ",sys.argv

def getRot():#default rot is 13
    if len(sys.argv)>3:
        return int(sys.argv[3])
    return 13

def getDataFile():
    if len(sys.argv)>1:
        f = open(sys.argv[1],"r")
        data = f.read()
        f.close()
        return data
    return ""

def pushDataFile(data):
    if len(sys.argv)>2:
        fo = open(sys.argv[2], "w")
        fo.write(data);
        fo.close()
