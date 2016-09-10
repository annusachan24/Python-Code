import pybrain,csv,accuracy
from pybrain.datasets import SupervisedDataSet
#from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.optimization.populationbased.ga import GA
import time

start_time=time.time()

ds = SupervisedDataSet(14,50)
tf=open('tf.csv','r')

X=[]
Y=[]
YY=[]
x=1;
y=302;
with open('d_set_all_50_centerofmass.csv', 'rb') as f:
    mycsv = csv.reader(f)
    for row in mycsv:
        if(x<=300):
            X.append(row[16:30])
        else:
            break
        x=x+1
    for row in mycsv:
        if(y<=601):
            YY.append(row[16:66])
        else:
                break
        y=y+1
'''for line in tf.readlines():
    data = [float(x) for x in line.strip().split(',') if x != '']
    indata =  tuple(data[:14])
    outdata = tuple(data[14:])
    ds.addSample(indata,outdata)'''
indata=X
outdata=YY
print ds.indim
print ds.outdim

n = buildNetwork(ds.indim,14,19,ds.outdim,recurrent=True)
print "-------------traning------------------"
print
ga = GA(ds.evaluateModuleMSE, n, minimize=True)
for i in range(10):
    n = ga.learn(0)[0]
print "-------------traning done----------------"
print

test_file=open('tf.csv','r')
i=1
for line in test_file.readlines():
	data1=[float(x) for x in line.strip().split(',') if x!='']
	indata1=tuple(data1[:14])
	print "Output for test case ",i," is"
	print n.activate(indata1)
	i=i+1


#print  n.activate([0.5957446809,0.5957446809,0.3549117248,0.5681818182,0.5681818182,0.3228305785,0.5277777778,0.5348837209,0.7804878049,0.7484662577,0.7484662577,0.5602017389,0.9692631128,1])
end_time=time.time()

print "time taken is ",end_time-start_time," seconds"
