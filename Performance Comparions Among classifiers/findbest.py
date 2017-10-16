import os, sys
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
from sklearn.model_selection import cross_val_predict
from sklearn import metrics
from sklearn.linear_model import Perceptron
from sklearn import tree
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier


#Codes below are used for finding best classifier parameters

iris = load_iris()
print ""
#DECISION TREE
dt = tree.DecisionTreeClassifier()
dt = dt.fit(iris.data, iris.target)
print "Decision Tree Accuracy: "
print cross_val_score(dt, iris.data, iris.target, cv=10, scoring  = 'accuracy').mean()
print ""

#Perceptron
pp = Perceptron(n_iter=100, random_state=16)
pp = pp.fit(iris.data, iris.target)
print "Perceptron Accuracy: "
print cross_val_score(pp, iris.data, iris.target, cv=10, scoring  = 'accuracy').mean()
print ""

#Neural Net
MLPC=MLPClassifier(solver='lbfgs',alpha=1,hidden_layer_sizes=(6,5,4),random_state=1,learning_rate_init=0.1)
MLPC.fit(iris.data,iris.target)
print "Neural Net Accuracy:"
print cross_val_score(MLPC, iris.data, iris.target ,cv=10,scoring = "accuracy").mean()
print " "

#Deep Learning(nerual net work with 5 hidden layers)
MLPC=MLPClassifier(solver='lbfgs',alpha=1,hidden_layer_sizes=(7,2,2,2,2),random_state=1,learning_rate_init=0.1)
MLPC.fit(iris.data, iris.target)
print "Deep Learning Accuracy:"
print cross_val_score(MLPC, iris.data, iris.target ,cv=10,scoring = "accuracy").mean()
print " "

#SVM
exp_number1 = range(1,11)
exp_accuracy1 = []
for i in exp_number1:
    svm = SVC()
    svm = svm.fit(iris.data, iris.target)
    each1 = cross_val_score(svm, iris.data, iris.target, cv=10, scoring  = 'accuracy')
    exp_accuracy1.append(each1.mean())
print "SVM Accuracy: "
print exp_accuracy1
print ""

#Navie Bayes
gnb = GaussianNB()
gnb = gnb.fit(iris.data, iris.target)
print "Navie Bayes Accuracy:"
print cross_val_score(gnb, iris.data, iris.target, cv=10,scoring = "accuracy").mean()
print " "

#Logistic Regression
LR = LogisticRegression(multi_class="multinomial",solver="lbfgs",C=100)
LR = LR.fit( iris.data, iris.target)
print "Logistic Regression Accuracy:"
print cross_val_score(LR, iris.data, iris.target, cv=10,scoring = "accuracy").mean()
print " "

#KNN
exp_number2 = range(1,21)
exp_accuracy2 = []
for i in exp_number2:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn = knn.fit(iris.data, iris.target) 
    each2 = cross_val_score(knn, iris.data, iris.target, cv=10, scoring  = 'accuracy')
    exp_accuracy2.append(each2.mean())
print "KNN Accuracy: "
print exp_accuracy2
print ""

#bagging
bagging = BaggingClassifier(KNeighborsClassifier(), max_samples=1.0, max_features=4)
bagging = bagging.fit(iris.data, iris.target)
print "Bagging Accuracy: "
print cross_val_score(bagging, iris.data, iris.target, cv=10, scoring  = 'accuracy').mean()
print ""

#Random Forests
exp_number3 = range(1,11)
exp_accuracy3 = []
for i in exp_number3:
	rf = RandomForestClassifier(n_estimators=10, max_features = 4)
	rf = rf.fit(iris.data, iris.target)
	each3 = cross_val_score(rf, iris.data, iris.target, cv=10, scoring  = 'accuracy')
	exp_accuracy3.append(each3.mean())
print "Random Forests Accuracy: "
print sum(exp_accuracy3)/float(len(exp_accuracy3))
print ""

#AdaBoost
ABC = AdaBoostClassifier(n_estimators=100,learning_rate=1)
ABC = ABC.fit(iris.data,iris.target)
print "AdaBoost Accuracy:"
print cross_val_score(ABC, iris.data, iris.target, cv=10,scoring = "accuracy").mean()
print " "

#GradientBoosting
GBC = GradientBoostingClassifier(learning_rate=0.1,n_estimators=200,max_depth=4)
GBC = GBC.fit(iris.data,iris.target)
print "GradientBoosting Accuracy:"
print cross_val_score(GBC, iris.data, iris.target, cv=10,scoring = "accuracy").mean()


















