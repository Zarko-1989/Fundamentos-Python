'''
Inversión de Tupla: Escribe un programa que invierta 
los elementos de una tupla.
'''

def invertir_tupla(tupla):
  tupla_invertida = tuple(tupla[::-1])
  return tupla_invertida

# Ejemplo de uso
tupla_original = ("a", "b", "c", "d", "e")
tupla_invertida = invertir_tupla(tupla_original)

print(f"Tupla original: {tupla_original}")
print(f"Tupla invertida: {tupla_invertida}")
