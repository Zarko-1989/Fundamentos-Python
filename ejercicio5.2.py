'''
Agenda Telefónica: Crea un programa que permita al 
usuario añadir, eliminar y buscar números de teléfono en un diccionario.
'''

# Diccionario para almacenar los contactos
agenda = {}

def agregar_contacto(nombre, telefono):
  if nombre in agenda:
    print(f"El contacto {nombre} ya existe en la agenda.")
  else:
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado con éxito.")

def eliminar_contacto(nombre):
  if nombre not in agenda:
    print(f"El contacto {nombre} no existe en la agenda.")
  else:
    del agenda[nombre]
    print(f"Contacto {nombre} eliminado con éxito.")

def buscar_contacto(nombre):
  if nombre not in agenda:
    print(f"El contacto {nombre} no existe en la agenda.")
  else:
    telefono = agenda[nombre]
    print(f"Número de teléfono de {nombre}: {telefono}")

# Bucle principal
while True:
  print("-" * 20)
  print("** Agenda Telefónica **")
  print("-" * 20)
  print("1. Agregar contacto")
  print("2. Eliminar contacto")
  print("3. Buscar contacto")
  print("4. Salir")
  print("-" * 20)

  opcion = input("Elige una opción: ")

  if opcion == "1":
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el número de teléfono: ")
    agregar_contacto(nombre, telefono)
  elif opcion == "2":
    nombre = input("Ingresa el nombre del contacto a eliminar: ")
    eliminar_contacto(nombre)
  elif opcion == "3":
    nombre = input("Ingresa el nombre del contacto a buscar: ")
    buscar_contacto(nombre)
  elif opcion == "4":
    print("¡ADIOSSS!")
    break
  else:
    print("Opción no válida.")

