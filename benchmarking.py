from sklearn.linear_model import SGDRegressor, SGDClassifier, Lasso, ElasticNet, Ridge
from sklearn.ensemble import RandomForestRegressor as RandForReg
from sklearn.model_selection import train_test_split
from benchmarker import benchmark, benchmark_print, criterionA
import csv

def rfregressorBmer(xtrain, ytrain, ytest):

	rfr = RandForReg(n_estimators = 100)
	rfr.fit(xtrain, ytrain)
	ypred=rfr.predict(xtest)
	return benchmark(ytest,ypred, [criterionA])

X = [] # Contient tous les vecteurs [annee,semaine,jour,heure,weather]
Y = [] # Contient toutes les affluences (representees par un entier, somme des departs et arrivees)
with open('csv/519dataframe.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader,None)
    for line in reader: 
        temp=[]
        a=line[0].replace("[","").replace("]","").replace(".0","").split(",")
        for elem in a:
            temp.append(int(elem))
        X.append(temp)
        Y.append(int(line[1]))

trainsize=0.7
xtrain, xtest, ytrain, ytest = train_test_split(X, Y, train_size=trainsize)

print('Training and Testing sets made')

benchmark_print(rfregressorBmer(xtrain, ytrain, ytest))
