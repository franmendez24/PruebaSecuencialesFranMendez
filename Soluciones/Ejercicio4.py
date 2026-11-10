#Fran Mendez Gonzalez  10/11/2026
#Escribe un programa que pida un número entero de tres cifras y muestre:
#Cada una de sus cifras (centenas, decenas y unidades).
#La suma de sus cifras.
#El número invertido, calculado como número (no como texto), de forma que pueda usarse en otras operaciones.
#No se permite convertir el número a cadena de texto (str): usa // y %.

numero = int(input("Introduce un número de tres cifras: "))

centenas = numero // 100
decenas = (numero //10) % 10
unidades = numero % 10

suma_cifras = centenas + decenas + unidades

print("Centenas:", centenas, " Decenas:", decenas, " Unidades:", unidades)
print("Suma de las cifras:", suma_cifras)