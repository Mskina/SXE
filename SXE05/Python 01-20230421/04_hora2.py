#hora, minuto y segundo
#hora, minuto y segundo dentro de 1 segundo
hora = int(input("Introduzca la hora: "))
minuto = int(input("Introduzca el minuto: "))
segundo = int(input("Introduzca el segundo: "))

segundo = segundo + 1
if segundo == 60:
    segundo = 0
    minuto = minuto + 1
    if minuto == 60:
        minuto = 0
        hora = hora + 1
        if hora == 24:
            hora = 0

print("En un segundo serán las",hora,":",minuto,":",segundo)