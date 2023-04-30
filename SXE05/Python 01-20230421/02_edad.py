#Entrada: dia, mes y año de nacimiento (actuales inventadas)
#Salida: edad actual
dia_hoy=14
mes_hoy=4
anho_hoy=2023

dia_nac = int(input("Introduzca día de nacimiento: "))
mes_nac = int(input("Introduzca mes de nacimiento: "))
anho_nac = int(input("Introduzca año de nacimeinto: "))

edad = anho_hoy - anho_nac

if mes_hoy < mes_nac:
    edad = edad - 1

if (mes_hoy == mes_nac) and (dia_nac > dia_hoy):
    edad = edad - 1

print("Tienes",edad,"años")