# PARCIAL 2 - PROGRAMACION 1

# NOMBRE: Elías Joel Beltramino
# DNI: 42.127.826

# ----------------------------------------------------------------

# Definición de funciones
def guardar_cambios(catalogo):
    with open("catalogo.csv", "w") as archivo:
                for libro in catalogo:
                    archivo.write(f"{libro['TITULO']},{libro['CANTIDAD']}\n")

def normalizar_titulo(titulo):
    titulo = titulo.strip().lower()
    titulo_normalizado = " ".join(titulo.split())
    return titulo_normalizado

# 1
def ingresar_titulos(catalogo):
    
    while True:
        print()
        print("<-----INGRESAR TÍTULOS----->")
        booleano = False       
        titulo = input("Ingrese el título del libro que desea registrar: ")

        if titulo.strip() == "":
            print("ERROR! Debe ingresar un titulo valido.")
            print("Inténtelo nuevamente")
            continue

        else:
            for registro in catalogo:
                if normalizar_titulo(registro["TITULO"]) == normalizar_titulo(titulo):
                    booleano = True
                    break

            if booleano:
                continue

            else:
                while True:

                    cantidad = input(f"Ingrese la cantidad de ejemplares de {normalizar_titulo(titulo)}: ")

                    if not cantidad.isdigit() or int(cantidad) < 0:
                        print("ERROR! Debe ingresar una cantidad válida.")
                        print("Inténtelo nuevamente.")
                        continue

                    else:
                        titulo_guardar = " ".join(titulo.split())
                        catalogo.append({"TITULO": titulo_guardar, "CANTIDAD": int(cantidad)})
                        print(f"El título '{titulo_guardar}' con {cantidad} ejemplares ha sido registrado exitosamente.")
                        break  

            while True:
                booleano = False
                opcion = input("¿Desea ingresar otro título? (s/n): ").lower()

                if opcion == "s":
                    booleano = True
                    break

                elif opcion == "n":
                    booleano = False
                    break

                else:
                    print("ERROR! Debe ingresar una opción válida (s/n).")
                    print("Intentelo nuevamente.")
                    continue

            if booleano:
                continue    
            else:
                print("Volviendo al menú principal...")
                break             

# 2    
def ingresar_ejemplares(catalogo):
    if len(catalogo) == 0:
        print("El catálogo está vacío. Primero debe ingresar un titulo.")
        return
    else:
        while True:
            print()
            print("<-----INGRESAR EJEMPLARES----->")
            titulo = input("Ingrese el título del libro al que desea agregar ejemplares: ")

            booleano = False
            for registro in catalogo:
                if normalizar_titulo(registro["TITULO"]) == normalizar_titulo(titulo):
                    booleano = True
                    while True:
                        cantidad = input("Ingrese la cantidad de ejemplares a agregar: ")

                        if not cantidad.isdigit() or int(cantidad) < 0:
                            print("ERROR! Debe ingresar una cantidad válida.")
                            print("Inténtelo nuevamente.")
                            continue

                        else:
                            registro["CANTIDAD"] += int(cantidad)
                            print(f"Se han agregado {cantidad} ejemplares al título '{registro['TITULO']}'.")
                            break
                    break
                
            if not booleano:
                print("El título no existe en el catálogo.")

            while True:
                opcion = input("¿Desea ingresar ejemplares a otro título? (s/n): ").lower()

                if opcion == "s":
                    break

                elif opcion == "n":
                    print("Volviendo al menú principal...")
                    return

                else:
                    print("ERROR! Debe ingresar una opción válida (s/n).")
                    print("Intentelo nuevamente.")
                    continue

# 3
def mostrar_catalogo(catalogo):
    print("<-----CATÁLOGO----->")
    if len(catalogo) == 0:
        print("No existen títulos cargados.")
    else: 
        for libro in catalogo:
            print (f"TÍTULO: {libro['TITULO']} | EJEMPLARES: {libro['CANTIDAD']}")
    input("Presione ENTER para volver al menú principal...")

# 4            
def consultar_disponibilidad(catalogo):


# Programa Principal

catalogo = []

# Cargar catálogo desde catalogo.csv
with open("catalogo.csv", "a+") as archivo:
    archivo.seek(0)
    for linea in archivo:
        libro = linea.strip().split(",")
        catalogo.append({"TITULO": libro[0], "CANTIDAD": int(libro[1])})

# Bucle principal del programa

while True:
    print()
    print("----- Menú Biblioteca -----")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")

    opcion = input("Elegí una opción: ")

    if not opcion.isdigit():
        print("Debes ingresar un número válido")
        continue

    opcion = int(opcion)

    match opcion:
        case 1:
            ingresar_titulos(catalogo)
            guardar_cambios(catalogo)
        case 2:
            ingresar_ejemplares(catalogo)
            guardar_cambios(catalogo)
        case 3:
            mostrar_catalogo(catalogo)
        case 4:
            consultar_disponibilidad(catalogo)
        case 5:
            listar_agotados(catalogo)
        case 6:
            agregar_titulo(catalogo)
            guardar_cambios(catalogo)
        case 7:
            # ver que va por aca
            guardar_cambios(catalogo)
            pass
        case 8:
            print("¡Hasta luego!")
            break
        case _:
            print("Opción inválida. Intenta nuevamente.")



            # ponerle una funcion de guardado al final de cada modificacion 