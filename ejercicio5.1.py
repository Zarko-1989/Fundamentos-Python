'''
Unión e Intersección de Conjuntos: Dados dos conjuntos, 
encuentra su unión e intersección.
'''
def union_conjuntos(conjunto1, conjunto2):
  """
  Encuentra la unión de dos conjuntos.

  Parámetros:
    conjunto1: El primer conjunto.
    conjunto2: El segundo conjunto.

  Retorno:
    Un nuevo conjunto que contiene todos los elementos de ambos conjuntos.
  """
  union = conjunto1 | conjunto2
  return union

def interseccion_conjuntos(conjunto1, conjunto2):
  interseccion = conjunto1 & conjunto2
  return interseccion

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

union = union_conjuntos(conjunto1, conjunto2)
interseccion = interseccion_conjuntos(conjunto1, conjunto2)

print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
