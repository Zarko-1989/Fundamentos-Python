'''Función Recursiva de Fibonacci: Implementa una función 
recursiva que calcule el n-ésimo número de Fibonacci.'''

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
numero = 10

resultado = fibonacci(numero)

print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")
