"""Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros."""
def milla_km (millas):
  km= millas * 1.60934
  return km
millasconvert = float (input("distancia en millas: "))
convert_km = milla_km(millasconvert)
print (f"En kilometros son: {convert_km}")