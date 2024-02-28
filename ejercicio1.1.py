'''
Calculadora de IMC: Crea un programa que calcule el Índice de Masa Corporal (IMC)
a partir del peso (en kilogramos) y la altura (en metros) ingresados por el usuario.
'''

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

altura2 = altura*altura
imc = (peso/altura2)

print("Su IMC es: ",imc)



