
lineas = int(input("Cuantas líneas?"))
contador = 1
texto = ""
for x in range(lineas):
    for y in range(contador):
        texto = texto + "* "
    print(texto)
    texto = ""
    contador = contador + 1 