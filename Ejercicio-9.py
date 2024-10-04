texto = "manzana naranja manzana pera pera pera naranja manzana"

diccionario = {}
cadena = ""
contador = 0

for i in texto:
    if i != " ":
        cadena = cadena + i
    contador += 1
    if i == " " or len(texto) == contador:
        try:
            diccionario[cadena] += 1
        except KeyError:
            diccionario[cadena] = 1
        finally:
            cadena = ""

for i in diccionario:
    print(f"La palabra {i} se repite {diccionario[i]} veces")
