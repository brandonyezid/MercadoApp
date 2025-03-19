# Función que recibe una lista de números y devuelve el número más grande
def encontrar_numero_mas_grande():
    # Solicitar al usuario que ingrese una lista de números
    lista_de_numeros = input("Ingresa una lista de numeros separados por espacio: ")

    # Convertir la entrada de texto en una lista de números
    lista_de_numeros = [int(numero) for numero in lista_de_numeros.split()]

    # Verificar si la lista está vacía
    if len(lista_de_numeros) == 0:
        return "La lista está vacía, no se puede encontrar el número más grande."
    
    # Encontrar el número más grande usando la función max()
    numero_mas_grande = max(lista_de_numeros)
    
    return numero_mas_grande

# Llamada a la función y mostrar el resultado
resultado = encontrar_numero_mas_grande()
print(f"El número más grande de la lista es: {resultado}")