"""Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
"""
def calbisiesto(year):
    
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False
year =  int(input("introduce un año: "))
if calbisiesto(year):
  print (f"el año {year} es bisiesto")
else:
  print (f"el año {year} no es bisiesto")