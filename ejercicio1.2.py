'''
Generador de Nombre de Usuario: Solicita al usuario su nombre, apellido y año de nacimiento, 
y genera un nombre de usuario 
combinándolos (por ejemplo, "AnaSmith1990").
'''

print("Digite su nombre: ")
nombre = input()

print("Digite su apellido: ")
apellido = input()

print("Digite su fecha de nacimiento: ")
fnacimiento = input()

print("Su usuario es: ",nombre+apellido+fnacimiento)