import pandas as pd
import numpy as np
from math import sqrt
from sklearn.metrics.pairwise import cosine_similarity

#Questao A
#Criacao da matriz termoXdocumento randomica
termdoc = np.random.random((10, 15))
#print(termdoc)

docs = pd.Series([f'D{i+1}' for i in range(len(termdoc))], name='Documentos')
terms = pd.Series([f'T{i+1}' for i in range(len(termdoc[0]))], name='Termos')

dbtermdoc = pd.DataFrame(
    np.array(termdoc).transpose(),
    columns=docs,
    index=terms
)
dbtermdoc.apply(lambda x : x.apply(lambda y : '0' if y == 0 else y))

#B Matriz de similadridade pelo cosseno
cosinecalc = cosine_similarity(termdoc,termdoc)
dfcosinecalc = pd.DataFrame(cosinecalc, index=docs, columns=docs)
#print(dfcosinecalc.round(2).apply(lambda x : x.apply(lambda y : '0' if y == 0 else y)))
dfcosinecalc.round(2).apply(lambda x : x.apply(lambda y : '0' if y == 0 else y))


#C Matriz userXdoc
userdoc = [[False, False, True, False, True, False, True,  True, False,  False],
       [ True,  True, False,  True, False,  True, False,  True,  True, False],
       [ True,  True,  True, False,  True,  True,  True,  False, False,  True],
       [False,  True, False,  True, False,  True,  True, False, True, False],
       [ False,  True, True,  True,  True,  True, False, False, False,  True],
       [False, False, False,  True, True, False, False,  True, False, False],
       [False,  True,  True,  True, False,  True, False, False,  True, False],
       [ True,  True,  False,  False,  True,  False,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
       [False, True, True,  True, False, True, False, False, True, False]]

usuarios = pd.Series([f'U{i+1}' for i in range(len(userdoc))], name='Usuários')

dataframe_userdoc = pd.DataFrame(np.array(userdoc).transpose(), columns=usuarios, index=docs)
#print(dataframe_userdoc)

#D Matrix de similaridade
convert = lambda u1, u2 : [d_u1 and d_u2 for d_u1, d_u2 in zip(u1, u2)].count(True)
sim = lambda u1, u2 : convert(u1, u2) / len(docs)

user = [[sim(u1,u2) for u2 in userdoc] for u1 in userdoc]
df_user = pd.DataFrame(user, index=usuarios, columns=usuarios)
#print(df_user.round(2).apply(lambda y: y.apply(lambda x : '0' if x == 0. else '1' if x == 1. else x)))
df_user.round(2).apply(lambda y: y.apply(lambda x : '0' if x == 0. else '1' if x == 1. else x))


#E Usuario mais similar por pergunta iterativa
def simuser(u_name):
  if u_name not in usuarios.values:
    return False
  u = df_user[u_name]
  return (df_user[u_name]
            .loc[u == u.max()]
            .index.drop(u_name)[0])

print("Digite a informacao abaixo")
u_dest = input()
u_sim  = simuser(u_dest)

#documento recomendado
docREC = dataframe_userdoc[u_sim].loc[dataframe_userdoc[u_sim]].loc[~dataframe_userdoc[u_dest]].index
#print(docREC)

#usuario leu
le_user = dataframe_userdoc[u_dest].loc[dataframe_userdoc[u_dest]].index
#print(u_dest_docs)

#usuario nao leu
nle_user = dfcosinecalc[docREC].loc[le_user]
#print(sim_sel_docs)

#Documento mais similar
doc_simi = nle_user[docREC].loc[le_user].mean()
#print(sim_mean)

#print documento
print(doc_simi.loc[doc_simi == doc_simi.max()].index[0])