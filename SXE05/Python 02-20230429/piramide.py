lineas = int(input("Introduzca líneas: "))
texto = ""
for x in range(lineas):

    espacios = lineas - 1 - x
    for y in range(espacios):
        texto = texto + " "

    asteriscos = lineas - espacios
    for y in range(asteriscos):
        texto = texto + "* "
    
    print(texto)
    texto = ""
    