import sys

datasetnum=[]
n=-1

def calculatebillionare(n):
    global datasetnum
    scores={}
    billionares=[]
    if n==-1:
        return None
    else:
        for salesdata in datasetnum:
            if not salesdata[0] in billionares:
                if salesdata[0] in scores:
                    scores[salesdata[0]]=scores[salesdata[0]]+salesdata[1]*salesdata[2]
                else:
                    scores[salesdata[0]]=salesdata[1]*salesdata[2]
                if scores[salesdata[0]]>=1000000:
                    billionares.append(salesdata[0])
                    del(scores[salesdata[0]])
        if len(billionares)==0:
            print "NA"
        else:
            for people in billionares:
                print people
        datasetnum=[]
        return None
                    
for line in sys.stdin:
    line=line.strip()
    line=line.split(" ")
    lineelement=map(int,line)
    if len(lineelement)==1:
        calculatebillionare(n)
        if lineelement[0]==0:
            break
        else:
            n=lineelement[0]
    else:
        datasetnum.append(lineelement)

    