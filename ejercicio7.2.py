'''Analizador de Log: Desarrolla un script que lea 
un archivo de registro (log) y encuentre e informe 
sobre ciertos patrones de error.'''

import re

def analizar_log(archivo):
  try:
    with open(archivo, "r") as f:
      lineas = f.readlines()
  except FileNotFoundError:
    print(f"Error: El archivo '{archivo}' no se encuentra.")
  else:
    # Patrones de error
    patrones = {
      "404": re.compile(r"404 Not Found"),
      "500": re.compile(r"500 Internal Server Error"),
      "Error de conexión": re.compile(r"Connection refused"),
    }

    # Conteo de errores
    conteo_errores = {
      "404": 0,
      "500": 0,
      "Error de conexión": 0,
    }

    for linea in lineas:
      for patron, regex in patrones.items():
        if regex.search(linea):
          conteo_errores[patron] += 1

    # Mostrar resultados
    for patron, conteo in conteo_errores.items():
      if conteo > 0:
        print(f"Se encontraron {conteo} errores de tipo '{patron}'.")

archivo = "log.txt"

analizar_log(archivo)
