"""Ejercicio 9: Conversor de Divisas
Ejercicios Introducción a Python: Enunciados 2
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros."""
def dolars_euros (dolars):
  euros= dolars * 0.85
  return euros
dolarsconvert = float (input("Cantidad de dolares: "))
convert_euros = dolars_euros(dolarsconvert)
print (f"En Euros son: {convert_euros}")