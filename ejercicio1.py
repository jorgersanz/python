"""
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
"""

def celsius_to_farenheit(celsius):
  far = celsius * 9/5 + 32
  return far

temp= float(input("put the celsius to convert:"))
farenheit=celsius_to_farenheit(temp)
print(farenheit)