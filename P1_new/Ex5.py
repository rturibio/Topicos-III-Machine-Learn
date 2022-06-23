import json
 
path = open('Ex5.json')
data = json.load(path)
 
print("Insira um caminho vazio para finalizar!") 


lastdata = data


print(lastdata)

while True:
    try:
        line = ""
        if isinstance(lastdata, list):
            line = input("Digite o próximo elemento da lista: ")
        else:
            line = input("Digite do caminho completo: ")
        if line == "":
            print("Resultado do caminho completo: ", lastdata)
            break
        else:
            if isinstance(lastdata, list):
                lastdata = lastdata[int(line)]
            else:
                lastdata = lastdata.get(line)
            print(lastdata)
      
    except Exception as e:
        print(e)

    
path.close()