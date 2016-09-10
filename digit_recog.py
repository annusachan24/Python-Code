
Skip to content
This repository

    Pull requests
    Issues
    Gist

    @annusachan24

Introducing a new repository design
Hey there! We're rolling out a faster, more streamlined repository experience and would love to give you early access.

1
1

    1

annusachan24/Digit-Recognizer

Digit-Recognizer/digitrecognizer4.0.py
7f0bc51 on 18 Mar
@amit-iiitm amit-iiitm adding files
1 contributor
83 lines (66 sloc) 2.18 KB
#read the traning data from csv file
import csv
import numpy as np
import sklearn
from sklearn.externals import joblib
from sklearn import svm, datasets, cross_validation
"""scikit-learn classifiers and cross validation utils
 from sklearn.ensemble import RandomForestClassifier (A random forest is a meta estimator
 that fits a number of decision tree classifiers on various sub-samples of the dataset and use
 averaging to improve the predictive accuracy and control over-fitting.)"""
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV #for cross validation



#loading the training data
X=[] #traning data
Y=[] #classes

with open('train.csv','r') as traindatafile:
    traindatareader=csv.reader(traindatafile,delimiter=',')
    for line in traindatareader:
        #line=line.strip('\n')
        X.append(line[1:])
        Y.append(line[0])


X=X[1:42000] #remove the label in first row
Y=Y[1:42000]
#print X
#print
#print
#print Y

X_train=np.array(X)
Y_train=np.array(Y)
X_train=X_train.astype(np.float)/255.0
Y_train=Y_train.astype(np.float)
#print X[0:10]
#print Y[0:10]
print "please give me the mistake"
clf=svm.SVC(gamma=0.01,C=100)
clf.fit(X_train,Y_train)
print "or run correctly"

#why whole definition of svc is not shown in interpreter
test_data=[]
with open('test.csv','r') as testdatafile:
    testdatareader=csv.reader(testdatafile,delimiter=',')
    for row in testdatareader:
        test_data.append(row)



test_data=test_data[1:]
test=np.array(test_data)
test=test.astype(np.float)/255.0
prediction=clf.predict(test)

print prediction

#writing the ouput to the csv file
with open('output7.0.csv','w') as outfile:
   writer=csv.writer(outfile,delimiter=",")
   i=1
   for value in prediction:
       
        #writer.writerow(str(int(value)))   using this wrote an extra blank line in between the values of prediction
        if i==1:
            outfile.write("ImageId")
            outfile.write(",")
            outfile.write("Label")
            outfile.write("\n")
        else:
            outfile.write(str(int(i-1)))
            outfile.write(",")
            outfile.write(str(int(value)))
            outfile.write("\n")
        i+=1

    
joblib.dump(clf,'train_pickle.pkl')

    Status API Training Shop Blog About Pricing 

    © 2015 GitHub, Inc. Terms Privacy Security Contact Help 

