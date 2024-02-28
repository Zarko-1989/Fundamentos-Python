'''
Mayores y Menores: Dada una lista de números, encuentra el 
número más grande y el más pequeño en la lista.
'''

def encontrar_mayores_menores(lista):
  mayor = lista[0]
  menor = lista[0]
  for numero in lista[1:]:
    if numero > mayor:
      mayor = numero
    elif numero < menor:
      menor = numero
  return {"mayor": mayor, "menor": menor}

# Obtener la lista de números del usuario
numeros = list(map(int, input("Ingresa una lista de números separados por comas: ").split(",")))

# Encontrar el mayor y el menor
mayores_menores = encontrar_mayores_menores(numeros)

# Imprimir el resultado
print(f"El número mayor es: {mayores_menores['mayor']}")
print(f"El número menor es: {mayores_menores['menor']}")

