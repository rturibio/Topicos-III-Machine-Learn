import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly as py
import plotly.graph_objs as go
from sklearn.cluster import KMeans
import warnings
import os
warnings.filterwarnings("ignore")
py.offline.init_notebook_mode(connected = True)

low_memory=False

vg = pd.read_csv('vgsales.csv')

print(vg)

print(vg.info())


print(vg.iloc[3704])

gname =  vg.Publisher.unique()
print(gname)


pid = vg.Platform.unique()
print(pid)


print(vg.Name.value_counts()[:15])
print(vg.Platform.value_counts()[:15])
print(vg.Genre.value_counts()[:15])


vg_use = vg.pivot_table ('Global_Sales',
                            index = 'Platform',
                             aggfunc='mean')
print(vg_use)
vg_use.plot(kind = 'bar')
plt.xlabel('Plataformas')
plt.ylabel('Vendas Globais')
plt.show()

vg_use = vg.pivot_table ('NA_Sales',
                            index = 'Platform',
                             aggfunc='mean')
print(vg_use)
vg_use.plot(kind = 'bar')
plt.xlabel('Plataformas')
plt.ylabel('Vendas North America')
plt.show()

vg_use = vg.pivot_table ('EU_Sales',
                            index = 'Platform',
                             aggfunc='mean')
print(vg_use)
vg_use.plot(kind = 'bar')
plt.xlabel('Plataformas')
plt.ylabel('Vendas Europa')
plt.show()

vg_use = vg.pivot_table ('JP_Sales',
                            index = 'Platform',
                             aggfunc='mean')
print(vg_use)
vg_use.plot(kind = 'bar')
plt.xlabel('Plataformas')
plt.ylabel('Vendas Japao')
plt.show()

'''
info = 0
while (info != 'sair'):
    print("Digite a informacao abaixo: e para sair digite sair.. ")
    info = input()
    name_search = vg.loc[vg['Name'] == info]
    df = pd.DataFrame(name_search)
    df = df.drop(columns="Rank")
    df = df.drop(columns="Year")
    print(df)
    df.plot(kind='bar')
    plt.xlabel('Jogo Selecionado')
    plt.ylabel('Vendas')
    plt.show()
'''

newvg = vg

del newvg["Rank"]
del newvg["Year"]
del newvg["EU_Sales"]
del newvg["JP_Sales"]
del newvg["Other_Sales"]


newvg = newvg[newvg['Name'].notna()]
newvg = newvg[newvg['Platform'].notna()]
newvg = newvg[newvg['Genre'].notna()]
newvg = newvg[newvg['Publisher'].notna()]
newvg = newvg[newvg['NA_Sales'].notna()]
newvg = newvg[newvg['Global_Sales'].notna()]

print(newvg)

print(newvg.head())

print(newvg.shape)

print(newvg.describe())

print(newvg.dtypes)

print(newvg.isnull().sum())

plt.style.use('fivethirtyeight')

plt.figure(1 , figsize = (15 , 6))
n = 0 
for x in ['NA_Sales' , 'Global_Sales']:
    n += 1
    plt.subplot(1 , 2 , n)
    plt.subplots_adjust(hspace =0.5 , wspace = 0.5)
    sns.distplot(newvg[x] , bins = 2)
    plt.title('{} '.format(x))
plt.show()


plt.figure(1 , figsize = (15 , 5))
sns.countplot(y = 'Platform' , data = newvg)
plt.show()

plt.figure(1 , figsize = (15 , 6))
for gender in ['X360' , 'PS3','NES','Wii','PS2']:
    plt.scatter(x = 'Genre' , y = 'Global_Sales' , data = newvg[newvg['Platform'] == gender] ,
                 alpha = 0.7 , label = gender)
plt.xlabel('Genre'), plt.ylabel('Global_Sales') 
plt.title('Sales Game Consoles')
plt.legend()
plt.show()


X2 = newvg[['NA_Sales' , 'Global_Sales' ]].iloc[: , :].values
inertia = []
for n in range(1 , 11):
    algorithm = (KMeans(n_clusters = n))
    algorithm.fit(X2)
    inertia.append(algorithm.inertia_)
    plt.figure(1 , figsize = (15 ,6))
plt.plot(np.arange(1 , 11) , inertia , 'o')
plt.plot(np.arange(1 , 11) , inertia , '-' , alpha = 0.5)
plt.title('The Elbow Method')
plt.xlabel('Número de Clusters') , plt.ylabel('Soma das Distâncias Q intra Clusters')
plt.show()

algorithm = (KMeans(n_clusters = 5))
algorithm.fit(X2)


KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
       n_clusters=5, n_init=10, tol=0.0001, verbose=0)

labels2 = algorithm.labels_
centroids2 = algorithm.cluster_centers_

h = 0.02
x_min, x_max = X2[:, 0].min() - 1, X2[:, 0].max() + 1
y_min, y_max = X2[:, 1].min() - 1, X2[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = algorithm.predict(np.c_[xx.ravel(), yy.ravel()]) 

plt.figure(1 , figsize = (15 , 7) )
plt.clf()
Z2 = Z.reshape(xx.shape)
plt.imshow(Z2 , interpolation='nearest', extent=(xx.min(), xx.max(), yy.min(), yy.max()), cmap = plt.cm.Pastel2, aspect = 'auto', origin='lower')
plt.scatter( x = 'NA_Sales' ,y = 'Global_Sales' , data = newvg , c = labels2 , s = 200 )
plt.scatter(x = centroids2[: , 0] , y =  centroids2[: , 1] , s = 300 , c = 'red' , alpha = 0.5)
plt.ylabel('Global Sales') , plt.xlabel('Vendas North America')
plt.show()

print(algorithm.cluster_centers_)
print(algorithm.inertia_)
print(algorithm.labels_)

X=vg[["NA_Sales","Global_Sales"]]

#Scatterplot of the input data
plt.figure(figsize=(10,6))
plt.scatter( x = 'NA_Sales' ,y = 'Global_Sales' , data = newvg , c = labels2 , s = 200 )
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)') 
plt.title('Spending Score (1-100) vs Annual Income (k$)')
plt.show()

wcss=[]
for i in range(1,11):
    km=KMeans(n_clusters=i)
    km.fit(X)
    wcss.append(km.inertia_)
#The elbow curve
plt.figure(figsize=(12,6))
plt.plot(range(1,11),wcss)
plt.plot(range(1,11),wcss, linewidth=2, color="red", marker ="8")
plt.xlabel("K Value")
plt.xticks(np.arange(1,11,1))
plt.ylabel("WCSS")
plt.show()

#Scatterplot of the clusters
plt.figure(figsize=(10,6))
sns.scatterplot(x = 'NA_Sales',y = 'Global_Sales',  
                 palette=['green','orange','brown','dodgerblue','red'], legend='full',data = vg  ,s = 200 )
plt.xlabel('NA_Sales')
plt.ylabel('Global_Sales') 
plt.show()

#Silhouette Coefficient
from sklearn import metrics
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, max_iter=200).fit(X)
    label = kmeans.labels_
    sil_coeff = metrics.silhouette_score(X, label, metric='euclidean')
    print("Para n_clusters={}, o coeficiente de  Silhouette {}".format(k, sil_coeff))