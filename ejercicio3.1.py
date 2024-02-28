'''
Eliminación de Duplicados: Escribe un programa que tome una 
lista de números ingresada por el usuario y elimine todos 
los números duplicados.
'''

def eliminar_duplicados(lista):
  numeros_unicos = set()
  lista_sin_duplicados = []
  for numero in lista:
    if numero not in numeros_unicos:
      numeros_unicos.add(numero)
      lista_sin_duplicados.append(numero)
  return lista_sin_duplicados

# Obtener la lista de números del usuario
numeros = list(map(int, input("Ingresa una lista de números separados por comas: ").split(",")))

# Eliminar los duplicados
numeros_sin_duplicados = eliminar_duplicados(numeros)

# Imprimir el resultado
print("Lista sin duplicados:")
print(", ".join(map(str, numeros_sin_duplicados)))
