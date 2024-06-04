"""Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo."""
def arearect(base,altura):
  rectangulo=base*altura
  return rectangulo
base =  int(input("introduce la base del rectangulo: "))
altura =  int(input("introduce la altura del rectangulo: "))
area=arearect(base,altura)
print (f"El área del rectangulo es: {area}")