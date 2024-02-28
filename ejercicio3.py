'''
Lista de la Compra: Crea un programa que permita al usuario 
ingresar una lista de compras, elemento por elemento, 
y luego imprima la lista completa al final.
'''

# Lista para almacenar los productos
lista_compra = []

# Bucle para agregar productos a la lista
while True:
  producto = input("Ingresa un producto (o 'fin' para terminar): ")
  if producto.lower() == "fin":
    break
  else:
    lista_compra.append(producto)

# Imprimir la lista completa
print("Lista de la compra:")
for producto in lista_compra:
  print(f"  - {producto}")

