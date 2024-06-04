"""
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
"""
def palindromo(word):
  invert_word = word[::-1]
  if invert_word == word:
    return True
  else:
    return False
word=input("dime una palabra: ")
if palindromo(word):
  print ("Es palindromo")
else: 
  print ("No es palindromo")




