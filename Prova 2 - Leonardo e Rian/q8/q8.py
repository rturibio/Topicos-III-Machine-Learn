from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()

print(cancer.data.shape)

print(cancer.feature_names)

print(cancer.target_names)

#split dataset em sets de treinamento e sets de teste
X_train, X_test, Y_train, Y_test = train_test_split(cancer.data,cancer.target, random_state=42)
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)

KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')
print("")
print("Acuracia Treino: ")
print(knn.score(X_train, Y_train))
print("")
print("Acuracia Teste: ")
print(knn.score(X_test, Y_test))