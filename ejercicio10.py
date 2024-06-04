"""Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
"""
def determinardia(num):
  diassemana =["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
  if num>=1 and num<=7:
    return diassemana[num-1]
dia= int(input("introduce un numero del 1 al 7: "))
nombre=determinardia(dia)
print (f"El dia de la semana correspoindiente es: {nombre}")