'''
Contador de Palabras: Dada una cadena de texto, 
cuenta cuántas veces aparece cada palabra y 
presenta los resultados en un diccionario.
'''
from collections import Counter

def contar_palabras(texto):
  # Convertir el texto a minúsculas y dividirlo en palabras
  palabras = texto.lower().split()

  # Contar la frecuencia de cada palabra
  contador_palabras = Counter(palabras)

  return contador_palabras

# Ejemplo de uso
texto = "Hola mundo, cómo estás? Hola mundo!"
contador_palabras = contar_palabras(texto)

for palabra, frecuencia in contador_palabras.items():
  print(f"Palabra: {palabra}, Frecuencia: {frecuencia}")
