"""
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no
"""
def verify_years(years):
  if years>=18:
    return ("Yeah")
  else:
    return ("No")
years=int(input("Put your years: "))
verify = verify_years(years)
print ( verify)
