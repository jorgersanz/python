"""Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
"""
def mintohour (minutos):
  horas = int (minutos/60)
  minresto = minutos % 60
  return horas, minresto
minutos = int(input("introduce la cantidad de minutos: "))
horas, minresto = mintohour (minutos)
print(f"{minutos} serian {horas} horas y {minresto} minutos")