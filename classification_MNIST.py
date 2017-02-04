import pandas as pd
#import numpy as np
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier


train = pd.read_csv('train.csv')
features = train.columns[1:]
labels = train.columns[0]
X = train[features]
y = train[labels]
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X/225.,y,test_size=0.1,random_state=0)
print("preprocessing complete")

def randomforest():
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    pred_rf = rf.predict(X_test)
    acc_rf = accuracy_score(y_test, pred_rf)
    print("Random forest accuracy :", acc_rf)
    '''Random forest accuracy : 0.93880952381'''
    
    
def SVM():
    svm = LinearSVC()
    svm.fit(X_train, y_train)
    svm_predicted = svm.predict(X_test)
    acc_svm = accuracy_score(y_test, svm_predicted)
    
    print("SVM Accuracy :", acc_svm)
    '''SVM Accuracy : 0.907619047619'''    
    

def KNN():
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    pred_knn = knn.predict(X_test)
    acc_knn = accuracy_score(y_test, pred_knn)
    
    print("KNN Accuracy :" , acc_knn)
    '''KNN Accuracy : 0.964523809524'''
    
