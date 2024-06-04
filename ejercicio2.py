"""
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
"""
def calc_total(monto):
  propina = monto * 0.15
  total = monto + propina
  return total
monto= float (input ("¿cuanto es el monto?"))
monto_total=calc_total(monto)
print(f"El monto total es: {monto_total}")
