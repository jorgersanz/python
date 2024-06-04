"""
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
"""
def cont_voc (palabra):
  vocales = "aeiouAEIOU"
  Cont=0
  for letra in palabra:
    if letra in vocales:
      Cont += 1
  return Cont
palabra = input("introduce una palabra: ")
num_voc = cont_voc (palabra) 
print (f"el número de vocales es: {num_voc}")

    
