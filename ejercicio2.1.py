'''
Calculadora de Factorial: Crea un programa que calcule el factorial 
de un número ingresado por el usuario. Utiliza tanto un ciclo for 
como un ciclo while para realizar el cálculo.
'''

def factorial(n):
    if n == 0 and n == 1:
        return 1
    respuesta = 1
    for numero in range(1, n + 1):
        respuesta = respuesta * numero
    return respuesta

print(
    factorial(5)
)

