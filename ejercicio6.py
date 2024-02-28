'''
Función de Conversión de Divisas: Escribe una función
que convierta una cantidad de dinero de una moneda a 
otra utilizando tasas de cambio dadas.'''

def convertir_moneda(cantidad, moneda_origen, moneda_destino, tasas_cambio):
  """
  Convierte una cantidad de dinero de una moneda a otra utilizando tasas de cambio dadas.

  Parámetros:
    cantidad: La cantidad de dinero a convertir.
    moneda_origen: La moneda original.
    moneda_destino: La moneda a la que se desea convertir.
    tasas_cambio: Un diccionario con las tasas de cambio, donde la clave es la moneda y el valor es el factor de conversión.

  Retorno:
    La cantidad de dinero convertida a la moneda destino.
  """
  if moneda_origen not in tasas_cambio:
    raise ValueError(f"Moneda origen '{moneda_origen}' no válida.")
  if moneda_destino not in tasas_cambio:
    raise ValueError(f"Moneda destino '{moneda_destino}' no válida.")

  tasa_origen = tasas_cambio[moneda_origen]
  tasa_destino = tasas_cambio[moneda_destino]

  conversion = cantidad * tasa_origen / tasa_destino

  return conversion

# Ejemplo de uso
tasas_cambio = {
  "EUR": 1.0,
  "USD": 1.14,
  "MXN": 20.40,
}

cantidad = 100
moneda_origen = "EUR"
moneda_destino = "USD"

conversion = convertir_moneda(cantidad, moneda_origen, moneda_destino, tasas_cambio)

print(f"{cantidad} {moneda_origen} equivalen a {conversion} {moneda_destino}")

