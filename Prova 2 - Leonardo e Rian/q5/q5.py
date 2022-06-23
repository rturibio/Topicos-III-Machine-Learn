import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

col_names = ['ta_native', 'course_instr', 'course', 'summer_regular', 'class_size', 'label']
ds = pd.read_csv("tae.csv", header=None, names=col_names)

labelencoder = preprocessing.LabelEncoder()

ta_native = labelencoder.fit_transform(ds.ta_native)
course = labelencoder.fit_transform(ds.course)
course_instr = labelencoder.fit_transform(ds.course_instr)
class_size = labelencoder.fit_transform(ds.class_size)
summer_regular = labelencoder.fit_transform(ds.summer_regular)

label = labelencoder.fit_transform(ds.label)
res = list(zip(ta_native, course_instr, course, summer_regular, class_size))
test = GaussianNB()
test.fit(res,label)

predicted= test.predict([[2, 25, 1, 2, 38]])
print("Predição 1:", predicted)

predicted= test.predict([[2,10,3,1,42]])
print("Predição 2:", predicted)

X_train, X_test, y_train, y_test = train_test_split(res, label, test_size=0.3)
testmod = GaussianNB()
testmod.fit(X_train, y_train)
y_pred = testmod.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))