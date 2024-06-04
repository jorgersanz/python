"""Ejercicio 18: Contador de Palabras
Ejercicios Introducción a Python: Enunciados 3
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
"""
def contapalabras(texto):
  palabras= texto.split()
  total=len(palabras)
  return total
texto= input ("Introduce un texto: ")
palabras=contapalabras(texto)
print(f"la oracion tiene {palabras} palbras")