def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperatura = float(input("Ingrese la temperatura: "))
unidad = input("¿A qué unidad desea convertirla? (Celsius o Fahrenheit): ").lower()

if unidad == "c":
    temperatura_convertida = celsius_a_fahrenheit(temperatura)
    print(f"{temperatura} grados Celsius equivalen a {temperatura_convertida} grados Fahrenheit.")
elif unidad == "f":
    temperatura_convertida = fahrenheit_a_celsius(temperatura)
    print(f"{temperatura} grados Fahrenheit equivalen a {temperatura_convertida} grados Celsius.")
else:
    print("Unidad no válida. Por favor, ingrese 'Celsius' o 'Fahrenheit'.")
