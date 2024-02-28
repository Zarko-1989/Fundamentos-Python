# Diccionario de sinónimos
sinonimos = {
  "alegre": ["contento", "feliz", "dichoso"],
  "triste": ["apenado", "melancólico", "deprimido"],
  "grande": ["enorme", "gigante", "colosal"],
  "pequeño": ["diminuto", "minúsculo", "ínfimo"],
  "bueno": ["excelente", "óptimo", "magnífico"],
  "malo": ["pésimo", "deficiente", "horrible"],
}

# Obtener la palabra del usuario
palabra = input("Ingresa una palabra: ")

# Buscar la palabra en el diccionario
if palabra in sinonimos:
  # Imprimir la lista de sinónimos
  print(f"Sinónimos de {palabra}:")
  for sinonimo in sinonimos[palabra]:
    print(f"  - {sinonimo}")
else:
  # Indicar que la palabra no está en el diccionario
  print(f"La palabra '{palabra}' no está en el diccionario.")

