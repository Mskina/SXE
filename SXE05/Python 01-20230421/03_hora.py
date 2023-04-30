#hora, minuto y segundo
#hora, minuto y segundo dentro de 1 segundo
hora = int(input("Introduzca la hora: "))
minuto = int(input("Introduzca el minuto: "))
segundo = int(input("Introduzca el segundo: "))

acarreo_minuto = (segundo + 1) // 60
segundo = (segundo + 1) % 60

acarreo_hora = (minuto + acarreo_minuto) // 60
minuto = (minuto + acarreo_minuto) % 60

hora = (hora + acarreo_hora) % 24

print("En un segundo serán las",hora,":",minuto,":",segundo)


