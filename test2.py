import csv
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
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
        

print len(X)
print len(YY)



for i in range(300):
    for j in range (50):
        if(YY[i][j]=='1'):
            Y.append(j+1)
    

print Y

print "traning"

clf=LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='liblinear', max_iter=100, multi_class='ovr', verbose=0, warm_start=False, n_jobs=1)


clf.fit(X,Y)

print "traning done"
test=np.array(X)
test=test.astype(np.float)
Y_test=np.array(Y)
Y_test=Y_test.astype(np.float)
#print test
print "testing"
prediction=clf.predict(test)

print"prediction"
print prediction
print "log probabilities"
print clf.predict_log_proba(test)
print "Accuracy"
print clf.score(test,Y_test)*7

    



