import pybrain
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
import time

start_time=time.time()

#our data set has 4 input parameters and 3 classes
ds = SupervisedDataSet(4,3)

tf=open('IRIS.csv','r')
for line in tf.readlines():
    data = [float(x) for x in line.strip().split(',') if x != '']
    indata =  tuple(data[:4])
    outdata = tuple(data[4:])
    ds.addSample(indata,outdata)
print ds.indim
print ds.outdim
# pybrain.tools.shortcuts.buildNetwork(*layers, **options)
#Build arbitrarily deep networks.
#layers should be a list or tuple of integers, that indicate how many neurons the layers should have.
#change the hidden layer neurons to maximise the accuracy
n = buildNetwork(ds.indim,3,ds.outdim,recurrent=True)

#bpa
t = BackpropTrainer(n,learningrate=0.01,momentum=0.5,verbose=True)

t.trainOnDataset(ds,5)
t.testOnData(verbose=True)


end_time=time.time()

print "time taken is ",end_time-start_time," seconds"
