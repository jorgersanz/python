"""Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual."""

def calcedad(year):
  today = 2024
  edad=today-year
  return edad
year =  int(input("introduce tu año de nacimiento: "))
edad = calcedad(year)
print (f"tienes {edad} años")
