# Lista para almacenar todos los contactos
agenda_contactos = []

# Función para agregar un contacto
def agregar_contacto():
    nombre = input("Digite el nombre del contacto: ")
    telefono = input("Digite el teléfono del contacto: ")
    correo = input("Digite el correo electrónico del contacto: ")

    # Crear una tupla con el teléfono y correo
    datos_contacto = (telefono, correo)

    # Crear un diccionario para el contacto
    contacto = {nombre: datos_contacto}

    # Agregar el contacto a la lista de contactos
    agenda_contactos.append(contacto)
    print(f"Contacto de {nombre} agregado exitosamente.")

# Función para buscar un contacto por nombre
def buscar_contacto():
    nombre_buscar = input("Digite el nombre del contacto que desea buscar: ")
    encontrado = False
    for contacto in agenda_contactos:
        if nombre_buscar in contacto:
            telefono, correo = contacto[nombre_buscar]
            print(f"Nombre: {nombre_buscar}, Teléfono: {telefono}, Correo: {correo}")
            encontrado = True
            break
    if not encontrado:
        print(f"No se encontró el contacto con el nombre {nombre_buscar}.")

# Función para mostrar todos los contactos
def mostrar_todos_los_contactos():
    if agenda_contactos:
        print("\n*** Agenda de Contactos ***")
        for contacto in agenda_contactos:
            for nombre, datos in contacto.items():
                telefono, correo = datos
                print(f"Nombre: {nombre}, Teléfono: {telefono}, Correo: {correo}")
    else:
        print("No hay contactos en la agenda.")

# Menú de opciones
def mostrar_menu():
    print("\n*** Agenda de Contactos ***")
    print("1. Agregar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

# Ciclo principal
while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opción (1-4): "))

    if opcion == 1:
        agregar_contacto()
    elif opcion == 2:
        buscar_contacto()
    elif opcion == 3:
        mostrar_todos_los_contactos()
    elif opcion == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción entre 1 y 4.")
