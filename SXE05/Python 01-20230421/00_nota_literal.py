#Entrada: nota numérica
#Salida: nota literal

nota = int(input("Introduzca nota: "))

if nota < 5:
    print("Suspenso")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
    
