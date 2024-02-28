'''
Concatenación de Listas: Crea dos listas con diferentes elementos, 
luego combínalas en una sola lista y ordénalos.
'''

lista1 = ["a", "b", "c", "d"]
lista2 = ["e", "f", "g", "h"]

#Combinar las dos listas en una sola
lista_combinada = lista1 + lista2

# Ordenar la lista combinada
lista_combinada.sort()

# Imprimir la lista ordenada
print(f"Lista ordenada: {lista_combinada}")
