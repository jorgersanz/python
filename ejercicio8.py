"""Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona."""

def IMC (peso, altura):
  imc= peso /(altura ** 2)
  return imc
peso = float(input("introduce peso Kg: "))
altura = float(input("introduce altura en m: "))
imc = IMC (peso, altura)
print (f"EL Indice de Masa Corporal es: {imc:.2f}")