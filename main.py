# Lista de productos
productos = []

# Menú de opciones 
print("***merqueoApp***")
print("***1. Agregar productos a tu lista de productos***")
print("***2. Mostrar tu lista de mercado***")
print("***3. Modificar tu lista de mercado***")
print("***4. Retirar producto de la lista de mercado***")
print("***5. Salir***")

opcion = 100

while opcion != 5:
    opcion = int(input("Digite la opción del menú: "))

    if opcion == 1:
        print("Creando la lista")
        # Crear un diccionario para cada producto
        producto = {}
        producto["id"] = len(productos) + 1  # Asignar un ID único
        producto["nombre"] = input("Digite el nombre del producto: ")
        producto["presentacion"] = input("Digite la presentación: ")
        producto["cantidad"] = int(input("Digite la cantidad: "))
        producto["precio"] = float(input("Digite el precio del producto: "))

        # Agregar el producto a la lista
        productos.append(producto)
        print("Producto agregado:", producto)

    elif opcion == 2:
        print("Mostrando la lista de productos")
        if productos:
            for p in productos:
                print(p["nombre"])
        else:
            print("No hay productos en la lista.")

    elif opcion == 3:
        print("Modificando la lista")
        id_producto = int(input("Digite el ID del producto a modificar: "))
        # Buscar el producto por ID
        producto_encontrado = None
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            print(f"Producto encontrado: {producto_encontrado}")
            
            # Modificar los campos del producto
            nuevo_nombre = input(f"Nuevo nombre del producto ({producto_encontrado['nombre']}): ")
            if nuevo_nombre:
                producto_encontrado["nombre"] = nuevo_nombre

            nueva_presentacion = input(f"Nueva presentación ({producto_encontrado['presentacion']}): ")
            if nueva_presentacion:
                producto_encontrado["presentacion"] = nueva_presentacion

            nueva_cantidad = input(f"Nueva cantidad en stock ({producto_encontrado['cantidad']}): ")
            if nueva_cantidad:
                producto_encontrado["cantidad"] = int(nueva_cantidad)

            nuevo_precio = input(f"Nuevo precio por unidad ({producto_encontrado['precio']}): ")
            if nuevo_precio:
                producto_encontrado["precio"] = float(nuevo_precio)

            print("Producto modificado exitosamente:", producto_encontrado)
        else:
            print("Producto no encontrado.")

    elif opcion == 4:
        print("Retirando producto de la lista")
        id_producto = int(input("Digite el ID del producto a retirar: "))
        # Buscar el producto por ID y retirarlo
        producto_encontrado = None
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            productos.remove(producto_encontrado)
            print(f"Producto {producto_encontrado['nombre']} retirado del inventario.")
        else:
            print("Producto no encontrado.")

    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
