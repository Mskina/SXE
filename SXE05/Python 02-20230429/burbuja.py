lista = [17,25,3,1,4]

for pasada in range(len(lista)):
    eficiente = len(lista) - pasada - 1 
    for x in range(eficiente):
        if lista[x] > lista[x+1]:
            temporal = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = temporal

print(lista)