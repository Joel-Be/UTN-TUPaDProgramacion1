# PARCIAL 2 - PROGRAMACION 1

# NOMBRE: Elías Joel Beltramino
# DNI: 42.127.826

# ----------------------------------------------------------------

# Definición de funciones
# Guardar datos en catalogo.csv
def guardar_cambios(catalogo):
    with open("catalogo.csv", "w") as archivo:
                for libro in catalogo:
                    archivo.write(f"{libro['TITULO']},{libro['CANTIDAD']}\n")

# Normalizar el titulo
def normalizar_titulo(titulo):
    titulo = titulo.strip().lower()
    titulo_normalizado = " ".join(titulo.split())
    return titulo_normalizado

# Opción 1
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

# Opción 2    
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

# Opción 3
def mostrar_catalogo(catalogo):
    print("<-----CATÁLOGO----->")
    if len(catalogo) == 0:
        print("No existen títulos cargados.")
    else: 
        for libro in catalogo:
            print (f"TÍTULO: {libro['TITULO']} | EJEMPLARES: {libro['CANTIDAD']}")
    input("Presione ENTER para volver al menú principal...")

# Opción 4           
def consultar_disponibilidad(catalogo):
    if len(catalogo) == 0:
        print("No hay títulos cargados en el catálogo")
        input("Presione ENTER para volver al menú principal...")
    
    else:
        while True:
            booleano = False

            print("<-----CONSULTAR DISPONIBILIDAD----->")
            titulo = input("Ingrese el título del libro que desea consultar ejemplares: ")

            for registro in catalogo:
                if normalizar_titulo(registro["TITULO"]) == normalizar_titulo(titulo):
                    booleano = True
                    print(f"Cantidad de ejemplares de {registro['TITULO']}: {registro['CANTIDAD']}")
                    break

            if not booleano:
                print("El título no existe en el catálogo.")

            while True:
                opcion = input("¿Desea consultar ejemplares de otro título? (s/n): ").lower()

                if opcion == "s":
                    break

                elif opcion == "n":
                    print("Volviendo al menú principal...")
                    return

                else:
                    print("ERROR! Debe ingresar una opción válida (s/n).")
                    print("Intentelo nuevamente.")
                    continue

# Opción 5
def listar_agotados(catalogo):
    if len(catalogo) == 0:
        print("El catálogo se encuentra vacio, primero debe agregar un título.")
        input("Presione ENTER para volver al menú principal...")

    else:

        no_hay_agotados = True
        print("<-----LISTADO DE AGOTADOS----->")

        for agotados in catalogo:

            if agotados['CANTIDAD'] == 0:
                print(agotados['TITULO'])
                no_hay_agotados = False

        if no_hay_agotados:
            print("No hay ejemplares agotados")

    input("Presione ENTER para volver al menú principal...")
            
# Opción 6
def agregar_titulo(catalogo):
   while True:
        booleano = False
        print()
        print("<-----AGREGAR TÍTULO----->")
             
        titulo = input("Ingrese el título del libro que desea agregar: ")

        if titulo.strip() == "":
            print("ERROR! Debe ingresar un titulo valido.")
            print("Inténtelo nuevamente")
            continue

        else:
            for registro in catalogo:
                if normalizar_titulo(registro["TITULO"]) == normalizar_titulo(titulo):
                    print("El título ya se encuentra registrado")
                    print("Inténtelo nuevamente")
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
                        print(f"El título '{titulo_guardar}' con {cantidad} ejemplares ha sido agregado exitosamente.")
                        input("Presione ENTER para volver al menú principal...")
                        return    

# Opción 7
def actualizar_ejemplares(catalogo):
    if len(catalogo) == 0:
                print("No existen titulos cargados, primero debe ingresar al menos un titulo")
                input("Presione ENTER para volver al menú principal...")
                return

    else:
        while True:
            print()
            print("<-----PRESTAMOS Y DEVOLUCIONES----->")
            print("1. Prestamos")
            print("2. Devoluciones")
            print("3. Volver al menu principal")
                    
            opcion = input("Elegí una opción: ")

            if not opcion.isdigit():
                print("Debes ingresar un número válido")
                continue

            opcion = int(opcion)

            match opcion:

                case 1:
                    prestamos(catalogo)
                    guardar_cambios(catalogo)
                
                case 2:
                    devoluciones(catalogo)
                    guardar_cambios(catalogo)
                
                case 3:
                    return
                
                case _:
                    print("ERROR! Debe ingresar un numero del 1 al 3.")
                    print("Inténtelo nuevamente")
                    continue
                            
# Opción 7-1
def prestamos(catalogo):
    while True:
        print()
        print("<-----PRESTAMOS----->")
        titulo = input("Ingrese el título del libro que desea prestar: ")

        booleano = False
        for registro in catalogo:
            if normalizar_titulo(registro["TITULO"]) == normalizar_titulo(titulo):
                booleano = True

                # si el libro no tiene ejemplares, no puede prestarse
                if registro['CANTIDAD'] == 0:
                    print(f"No es posible prestar '{registro['TITULO']}' porque no existen ejemplares disponibles.")
                    break

                print(f"{registro['TITULO']}: {registro['CANTIDAD']} ejemplares disponibles")

                while True:
                    ejemplares = input("Cuantos ejemplares desea prestar: ")

                    if not ejemplares.isdigit() or int(ejemplares) <= 0:
                        print("ERROR! Debe ingresar una cantidad válida.")
                        print("Inténtelo nuevamente.")
                        continue
                    else:
                        ejemplares = int(ejemplares)

                        if registro['CANTIDAD'] - ejemplares < 0:
                            print("ERROR! No puede prestar más ejemplares de los disponibles.")
                            print(f"Solo tiene [{registro['CANTIDAD']}] ejemplares de {registro['TITULO']}.")
                            print("Debe ingresar un número menor.")
                            continue
                        else:
                            registro['CANTIDAD'] -= ejemplares
                            print("Registro de ejemplares actualizado con exito")
                            print(f"Le quedan disponibles {registro['CANTIDAD']} ejemplares de {registro['TITULO']}")
                            break
                break

        if not booleano:
            print("El título no existe en el catálogo.")

        while True:
            opcion = input("¿Desea registrar otro préstamo? (s/n): ").lower()

            if opcion == "s":
                break
            elif opcion == "n":
                print("Volviendo al menú actualizar ejemplares...")
                return
            else:
                print("ERROR! Debe ingresar una opción válida (s/n).")
                print("Intentelo nuevamente.")
                continue
   
# Opción 7-2
def devoluciones(catalogo):
    while True:
        print()
        print("<-----DEVOLUCIONES----->")
        titulo = input("Ingrese el título del libro que desea devolver: ")

        booleano = False
        for registro in catalogo:

            if normalizar_titulo(registro["TITULO"]) == normalizar_titulo(titulo):
                booleano = True
                print(f"{registro['TITULO']}: {registro['CANTIDAD']} ejemplares registrados actualmente")

                while True:
                    ejemplares = input("Cuantos ejemplares desea devolver: ")

                    if not ejemplares.isdigit() or int(ejemplares) <= 0:
                        print("ERROR! Debe ingresar una cantidad válida.")
                        print("Inténtelo nuevamente.")
                        continue

                    else:
                        ejemplares = int(ejemplares)
                        registro['CANTIDAD'] += ejemplares
                        print("Registro de ejemplares actualizado con exito")
                        print(f"Ahora tiene {registro['CANTIDAD']} ejemplares de {registro['TITULO']}")
                        break

                break

        if not booleano:
            print("El título no existe en el catálogo.")

        while True:
            opcion = input("¿Desea registrar otra devolución? (s/n): ").lower()

            if opcion == "s":
                break

            elif opcion == "n":
                print("Volviendo al menú actualizar ejemplares...")
                return
            
            else:
                print("ERROR! Debe ingresar una opción válida (s/n).")
                print("Intentelo nuevamente.")
                continue

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
            actualizar_ejemplares(catalogo)

        case 8:
            print("¡Hasta luego!")
            break
        
        case _:
            print("Opción inválida. Intenta nuevamente.")