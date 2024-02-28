import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar el número de intentos
intentos = 0

# Bucle principal del juego
while True:
    # Pedir al usuario que ingrese un número
    adivinanza = int(input("Ingresa tu suposición (entre 1 y 100): "))

    # Incrementar el número de intentos
    intentos += 1

    if adivinanza == numero_secreto:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
        break
    elif adivinanza > numero_secreto:
        print("Tu número es demasiado alto.")
    else:
        print("Tu número es demasiado bajo.")

