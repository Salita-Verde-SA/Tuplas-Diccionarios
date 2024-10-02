texto = "manzana naranja manzana pera pera pera naranja manzana"
palabra= texto.split()
# Dividimos el texto en una lista de palabras
print(palabra)
i=0
dic= {}
for i in palabra:
    if i in dic:
        dic[i]+=1
        #Si esta se suma
    else:
        dic[i]=1
        #sino 1
print(dic)
