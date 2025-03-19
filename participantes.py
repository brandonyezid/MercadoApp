# Lista para almacenar los participantes
participantes = []

# Función para registrar participantes
def registrar_participante():
    nombre = input("Digite el nombre del participante: ")
    edad = int(input("Digite la edad del participante: "))
    correo = input("Digite el correo electrónico del participante: ")

    # Crear una tupla con la edad y correo
    datos = (edad, correo)

    # Crear un diccionario para el participante
    participante = {nombre: datos}

    # Agregar el participante al listado de participantes
    participantes.append(participante)

# Ciclo para registrar múltiples participantes
while True:
    print("\n*** Registro de Participantes ***")
    registrar_participante()
    
    # Preguntar si desea registrar otro participante
    continuar = input("¿Desea registrar otro participante? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar la lista de participantes registrados
print("\n*** Lista de Participantes Registrados ***")
for participante in participantes:
    for nombre, datos in participante.items():
        edad, correo = datos
        print(f"Nombre: {nombre}, Edad: {edad}, Correo: {correo}")
