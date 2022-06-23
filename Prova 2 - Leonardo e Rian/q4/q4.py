import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['ta_native', 'course_instr', 'course', 'summer_regular', 'class_size', 'label']
ds = pd.read_csv("tae.csv", header=None, names=col_names)

labelencoder = preprocessing.LabelEncoder()

ta_native = labelencoder.fit_transform(ds.ta_native)
course_instr = labelencoder.fit_transform(ds.course_instr)
course = labelencoder.fit_transform(ds.course)
summer_regular = labelencoder.fit_transform(ds.summer_regular)
class_size = labelencoder.fit_transform(ds.class_size)

label = labelencoder.fit_transform(ds.label)

res = list(zip(ta_native, course_instr, course, summer_regular, class_size))

#5
modelo5 = KNeighborsClassifier(n_neighbors=5)

modelo5.fit(res,label)

predicted= modelo5.predict([[2, 25, 1, 2, 38]]) # 0
print("teste predição 5:", predicted)

X_train, X_test, y_train, y_test = train_test_split(res, label, test_size=0.3)

modelo5.fit(X_train, y_train)

y_pred = modelo5.predict(X_test)
print("Accuracy5:",metrics.accuracy_score(y_test, y_pred))

#7
modelo7 = KNeighborsClassifier(n_neighbors=7)

modelo7.fit(res,label)

predicted= modelo7.predict([[2, 25, 1, 2, 38]]) # 0
print("teste predição 7:", predicted)

X_train, X_test, y_train, y_test = train_test_split(res, label, test_size=0.3)

modelo7.fit(X_train, y_train)

y_pred = modelo7.predict(X_test)
print("Accuracy7:",metrics.accuracy_score(y_test, y_pred))