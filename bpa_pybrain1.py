import pybrain
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
import time

start_time=time.time()

#our data set has 14 input parameters and 50 classes
ds = SupervisedDataSet(14,50)
#tf.csv has been modifies such that the csv file has 64 values on each line separated by a comma. The first 14 values are input values and the rest 50 are outputs. 
tf=open('tf.csv','r')
for line in tf.readlines():
    data = [float(x) for x in line.strip().split(',') if x != '']
    indata =  tuple(data[:14])
    outdata = tuple(data[14:])
    ds.addSample(indata,outdata)
print ds.indim
print ds.outdim
# pybrain.tools.shortcuts.buildNetwork(*layers, **options)
#Build arbitrarily deep networks.
#layers should be a list or tuple of integers, that indicate how many neurons the layers should have.
#buiding the network sucg that is has 14 input neurons, 2 hidden layers of 14 neurons each and output layer of 50 neurons.
#change the hidden layer neurons to maximise the accuracy
n = buildNetwork(ds.indim,14,ds.outdim,recurrent=True)

#bpa
t = BackpropTrainer(n,learningrate=0.01,momentum=0.5,verbose=True)

t.trainOnDataset(ds,5)
t.testOnData(verbose=True)


end_time=time.time()

print "time taken is ",end_time-start_time," seconds"
