'''Registro de Usuario: Escribe un programa que permita 
al usuario ingresar su nombre y edad, y guarda estos datos 
en un archivo.'''

def registrar_usuario(nombre, edad):
  with open("usuarios.txt", "a") as archivo:
    archivo.write(f"{nombre},{edad}\n")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

registrar_usuario(nombre, edad)

print("Usuario registrado con éxito.")
