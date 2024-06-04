"""Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
"""
def precio_total(monto):
  propina = monto * 0.20
  total = monto - propina
  return total
monto= float (input ("¿Cual es el precio? "))
monto_total=precio_total(monto)
print(f"El precio final es: {monto_total}")
