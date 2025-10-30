# NOMBRE: Elías Joel Beltramino 
# DNI: 42.127.826

# TP 8 - Manejo de Archivos

# Todos los ejercicios de 1 al 5 los realice uno tras otro sobre el archivo que dejaba el ejercicio anterior como si fuese un solo programa.

# En el ejercicio 6 cree un menu principal para elegir que accion tomar como si fuese un programa totalmente aisalado del resto.


# Ejercicio 1:
archivo = open("productos.txt", "w")
archivo.write("Manzanas,500,50\n")
archivo.write("Bananas,200,60\n")
archivo.write("Peras,400,80\n")
archivo.close()

# Ejercicio 2:
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        lista = linea.strip().split(",")
        print(f"Producto: {lista[0]} | Precio: ${lista[1]} | Cantidad: {lista[2]}")
    

# Ejercicio 3:
producto = input("Ingrese el nombre del producto que desea agregar: ").title()
precio = input("Ingrese el precio del producto: ")
cantidad = input("Ingrese la cantidad del producto: ")
with open ("productos.txt", "a") as archivo:
    archivo.write(f"{producto},{precio},{cantidad}\n")

# Ejercicio 4:
productos = []
with open ("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip().split(",")
        producto = {"nombre":linea[0], "precio":float(linea[1]), "cantidad":int(linea[2])}
        productos.append(producto)


# Ejercicio 5:
producto = input("Ingrese el nombre del producto a buscar: ").title()
encontrado = False
for i in productos:
    if i["nombre"] == producto:
        print(f"Producto: {i['nombre']} | Precio: ${i['precio']} | Cantidad: {i['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado.")


# Ejercicio 6:
# Funciones para las opciones del menu
def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos disponibles.")    
    else:
        for producto in productos:
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

def buscar_producto(productos):
    producto_nombre = input("Ingrese el nombre del producto a buscar: ").title()
    encontrado = False
    for producto in productos:
        if producto["nombre"] == producto_nombre:
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

def agregar_producto(productos):
    producto_nombre = input("Ingrese el nombre del producto que desea agregar: ").title()
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    nuevo_producto = {"nombre": producto_nombre, "precio": precio, "cantidad": cantidad}
    productos.append(nuevo_producto)


# Programa Pincipal
# Primero leemos el archivo y cargamos nuevamente la lista de productos como la dejo el usuario anteriormente.
productos = []
with open ("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip().split(",")
        producto = {"nombre":linea[0], "precio":float(linea[1]), "cantidad":int(linea[2])}
        productos.append(producto)

# Este es el ciclo white principal del programa, todo va a suceder dentro de este ciclo
# Cuando el usuario desee salir se guardara todo en el archivo y se saldra del programa
while True:
    print ("----- MENU PRINCIPAL -----")
    print()
    print("1. Mostrar todos los productos")
    print("2. Buscar un producto por nombre")
    print("3. Agregar un nuevo producto")
    print("4. Salir Y guardar cambios")

    opcion = input("Seleccione una opcion (1-4): ")

    if not opcion.isdigit():
        print("Opcion invalida. Por favor, intente de nuevo.")
        print()
        continue

    match opcion:
        case "1":
            mostrar_productos(productos)
            print()
        case "2":
            buscar_producto(productos)
            print()
        case "3":
            agregar_producto(productos)
            print()
        case "4":
            # Guardamos los cambios en el archivo antes de salir
            with open ("productos.txt", "w") as archivo:
                for producto in productos:
                    archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
            print("Cambios guardados. Saliendo del programa.")
            break
        case _:
            print("Opcion invalida. Por favor, intente de nuevo.")
            print()