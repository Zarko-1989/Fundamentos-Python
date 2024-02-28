'''
Contador de Vocales: Desarrolla un programa que cuente la cantidad de 
vocales en una frase proporcionada por el usuario.
'''

def contar_vocales(frase):
  vocales = "aeiou"
  conteo_vocales = {}
  for letra in frase.lower():
    if letra in vocales:
      conteo_vocales.setdefault(letra, 0)
      conteo_vocales[letra] += 1
  return conteo_vocales

# Obtener la frase del usuario
frase = input("Ingresa una frase: ")

# Contar las vocales
conteo_vocales = contar_vocales(frase)

# Imprimir el resultado
print("Las vocales en la frase son:")
for vocal, cantidad in conteo_vocales.items():
  print(f"  {vocal}: {cantidad}")
