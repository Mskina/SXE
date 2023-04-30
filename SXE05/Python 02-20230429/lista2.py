lista = [1,2,2,3,3,3]
contador = 0
posicion = 0

valor_buscado = int(input("Introduzca valor buscado: "))

while posicion < len(lista):
    if valor_buscado == lista[posicion]:
        contador = contador + 1
    posicion = posicion + 1

print("El valor",valor_buscado,"aparece",contador,"veces")