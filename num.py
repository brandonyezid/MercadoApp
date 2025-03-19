# Iniciamos el ciclo while
while True:
    numero = int(input("Ingresa un número (o un número negativo para salir): "))
    
    # Verificamos si el número es negativo para salir del ciclo
    if numero < 0:
        print("Has ingresado un número negativo. El programa terminará.")
        break
    else:
        print(f"Has ingresado el número: {numero}")
