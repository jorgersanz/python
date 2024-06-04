"""Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
"""
def contarparesimpares (list):
  pares=0
  impares=0
  for num in list:
    if num % 2 ==0:
      pares =pares + 1
    else:
      impares= impares + 1
  return pares, impares
numeros = list(map(int,input("introduce una lista de numeros separados por espacio: ").split()))
pares, impares = contarparesimpares(numeros)
print (f"La lista tiene {pares} numeros pares y {impares} numeros impares")