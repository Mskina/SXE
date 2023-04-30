#Entrada: nombre y edad
#Salida: indica si es o no es mayor de edad
texto = input("INtroduzca su nombre: ")
edad = input("Introduzca su edad: ")
edad = int(edad)
print("Hola",texto,"tienes",edad,"años")
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")