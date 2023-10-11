secret_number = 7  # Elige un número secreto (puedes cambiarlo si lo deseas)

print("¡Bienvenido al juego Adivina el número secreto!")

while True:
    user_number = int(input("Ingresa un número entero: "))

    if user_number == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break  # Salir del bucle cuando el número es adivinado
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
