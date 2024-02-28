'''Lector de Poemas: Crea un programa que lea un 
archivo de texto con un poema y lo muestre en la consola.'''

def leer_poema(archivo):
  try:
    with open(archivo, "r") as f:
      poema = f.read()
  except FileNotFoundError:
    print(f"Error: El archivo '{archivo}' no se encuentra.")
  else:
    print(poema)

archivo = "poema.txt"

leer_poema(archivo)
