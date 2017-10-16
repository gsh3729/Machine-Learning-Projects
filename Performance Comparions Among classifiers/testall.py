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

iris = load_iris()

names = ["Decision Tree","Perceptron","Neural Net","Deep learning","SVM","Naive Bayes","Logistic Regression","K-NN","Bagging","Random Forest","AdaBoost","Gradient Boosting"]

classifiers = [
	tree.DecisionTreeClassifier(),
	Perceptron(n_iter=100, random_state=16),
	MLPClassifier(solver='lbfgs',alpha=1,hidden_layer_sizes=(5,2),random_state=1,learning_rate_init=0.1),
	MLPClassifier(solver='lbfgs',alpha=1,hidden_layer_sizes=(6,5,4,3,2),random_state=1,learning_rate_init=0.1),
	SVC(),
	GaussianNB(),
	LogisticRegression(multi_class="multinomial",solver="sag",C=1,max_iter = 100),
	KNeighborsClassifier(n_neighbors=13),
	BaggingClassifier(KNeighborsClassifier(), max_samples=0.5, max_features=3),
	RandomForestClassifier(n_estimators=20, max_features = 4),
	AdaBoostClassifier(n_estimators=50,learning_rate=1),
	GradientBoostingClassifier(learning_rate=0.1,n_estimators=50,max_depth=4)
]
print ""
print "Testing all classifiers together with best parameters:"
n = range(0,12)
for i in n:
	clf = classifiers[i].fit(iris.data,iris.target)
	print names[i] + " accuracy: " + str(cross_val_score(clf,iris.data,iris.target,cv=10,scoring = "accuracy").mean())
	print names[i] + " precision: " + str(cross_val_score(clf,iris.data,iris.target,cv=10,scoring = "precision_macro").mean())
	print ""

		
