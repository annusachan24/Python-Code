import csv
import numpy as np
p1=[]
p2=[]
p=[]
x=0
with open('input50.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #print row
        if (x==4):
            break
        x=x+1
        p1.append(row)
y=0
with open('output50.csv', 'rb') as f1:
    reader1 = csv.reader(f1)
    for row in reader1:
        #print row
        if (y==4):
            break
        y=y+1
        p2.append(row)


pa1=np.asarray(p1)
pa2=np.asarray(p2)
p=np.hstack((pa1, pa2))   
ppl=[]
ppl=np.array(p).tolist()

#print p1
#print p2
print p
print ppl
f.close()
f1.close()

