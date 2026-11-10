#Fran Mendez Gonzalez  10/11/2026
#Un servidor guarda el tiempo que lleva encendido como una cantidad total de segundos. Escribe un programa
#que pida esa cantidad (número entero) y muestre a cuántos días, horas, minutos y segundos corresponde.
#Debes resolverlo usando únicamente operaciones aritméticas (división entera // y resto %).

Segundos_por_dia = 24 * 60 * 60
Segundos_por_hora = 60* 60
Segundos_por_minuto = 60

total_segundos = int(input("Introduce el tiempo en segundos: "))

dias = total_segundos // Segundos_por_dia
resto = total_segundos % Segundos_por_dia

minutos = resto // Segundos_por_minuto
segundos = resto % Segundos_por_minuto


print (total_segundos son dias "dias", horas "horas", minutos "minutos", segundos "segundos")
