import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('tae.csv', names=['ta_native', 'course_instr', 'course', 'summer_regular', 'class_size', 'label'])
#print(data.head())

X=data[['ta_native', 'course_instr', 'course', 'summer_regular', 'class_size']]  
Y=data['label']  

#70%
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
rfc=RandomForestClassifier(n_estimators=1000)
rfc.fit(X_train,y_train)
y_pred=rfc.predict(X_test)
print("Acuracia:",metrics.accuracy_score(y_test, y_pred))

#nova entrada
rfc.predict([[2, 25, 1, 2, 38]])
rfc=RandomForestClassifier(n_estimators=1000)
rfc.fit(X_train,y_train)

RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=2,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)

teste = pd.Series(rfc.feature_importances_,index=['ta_native', 'course_instr', 'course', 'summer_regular', 'class_size']).sort_values(ascending=False)

sns.barplot(x=teste, y=teste.index)
plt.show()

#retirada menos importante e teste
X=data[['ta_native', 'course_instr', 'course', 'class_size']]  
Y=data['label']                                       

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.70, random_state=5)
rfc=RandomForestClassifier(n_estimators=1000)
rfc.fit(X_train,y_train)
y_pred=rfc.predict(X_test)
print("Acuracia:",metrics.accuracy_score(y_test, y_pred))