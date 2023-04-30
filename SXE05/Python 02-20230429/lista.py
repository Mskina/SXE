lista = [1,2,2,3,3,3]
contador = 0

valor_buscado = int(input("Introduzca valor buscado: "))

for x in range(len(lista)):
    if valor_buscado == lista[x]:
        contador = contador + 1

print("El valor",valor_buscado,"aparece",contador,"veces")