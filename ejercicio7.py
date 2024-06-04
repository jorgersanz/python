"""Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario."""
def suma (a, b):
  return a+b
def resta (a, b):
  return a-b
def multi (a, b):
  return a*b
def divi (a, b):
  if b!=0:
    return a/b
  else:
    return("Error")
print("Operacion que quiere hacer")
print("1.suma")
print("2.resta")
print("3. multiplicación")
print("4.division")
operacion = int(input("selecciona el número de la operacion a realizar(1,2,3,4): "))
numa= float(input("introduce el primer número: "))
numb= float(input("introduce el primer número: "))
if operacion == 1:
  resultado = suma(numa,numb)
elif operacion == 2:
  resultado = resta(numa,numb)
elif operacion == 3:
  resultado = multi(numa,numb)
elif operacion == 4:
  resultado = divi(numa,numb)
else: 
  resultado = "selecciona una operacion correcta"
print(f"resultado: {resultado}")

