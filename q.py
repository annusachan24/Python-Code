import csv
import numpy as np
tf=open('tf.csv','r')
lines=[]
for line in tf.readlines():
    data1 = [float(x) for x in line.strip().split(',') if x != '']
    indata1 =  tuple(data[:14])
    lines=indata1
    print lines
    #print indata
