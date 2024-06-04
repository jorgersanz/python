"""Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
"""
suma=0
for number in range (2,101,2):
  suma += number
print (f"La suma de todos los números pares del 1 al 100 es: {suma}")
