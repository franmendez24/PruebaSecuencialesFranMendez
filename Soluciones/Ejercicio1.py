#Fran Mendez Gonzalez  10/11/2026
#Escribe un programa que pida el precio de un producto sin IVA y muestre el importe del IVA (21 %)
#y el precio final que debe pagar el cliente.

Tipo_IVA = 0.21

precio_sin_iva = float(input("Introduce el precio sin IVA: "))

importe_iva = round(precio_sin_iva * Tipo_IVA, 2)
precio_final = round(precio_sin_iva + importe_iva, 2)

print("IVA (21%):", importe_iva)
print("Precio final:", precio_final)
