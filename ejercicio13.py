"""Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
"""
def esprimo(num):
  if num<1:
    return False
  for i in range(2, int (num/2)):
    if num % i ==0:
      return False
  return True
numero = int (input("Dime que numero quieres ver si es primo: ") )
if esprimo(numero):
  print (f"el numero {numero} es primo")
else:
  print (f"el numero {numero} no es primo")
  