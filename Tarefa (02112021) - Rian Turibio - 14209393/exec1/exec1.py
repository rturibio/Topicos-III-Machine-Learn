import os
if os.path.exists("arq01.txt"):
  os.remove("arq01.txt")

info = 0
while (info != 'sair'):
    print("Digite a informacao abaixo: e para sair digite sair.. ")
    info = input()
    with open('arq01.txt', 'a') as arquivo:
        arquivo.write(info + '\n')

arquivo = open('arq01.txt','r')
print('Resultado:')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()