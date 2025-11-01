titulos = []
ejemplares = []
agotados = []
opcion = 0

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
            print()
            print("<-----INGRESAR TÍTULOS----->") 

            while True:
                
                titulo = input("Ingrese el título del libro que desea registrar: ").title()

                if titulo.strip() == "":
                    print("ERROR! Debe ingresar un titulo valido.")
                    print("Intentelo nuevamnete")
                    continue

                elif titulo in titulos:
                    print("ERROR! El titulo ya se encuentra registrado.")
                    print("Inténtelo nuevamente")
                    continue

                else:
                    titulos.append(titulo)
                    posicion = titulos.index(titulo)
                    ejemplares.insert(posicion, 0)
                    print("Título registrado correctamente")

                    while True:
                        si_no = input("¿Desea agregar mas títulos? (s/n)").lower()

                        if si_no == "s" or si_no == "n":
                            break

                        else:
                            print("ERROR! Debe ingresar 'S' o 'N'")
                            continue
                        
                    match si_no:
                            case "s":
                                continue
                            case "n":
                                break

        case 2:
            if len(titulos) != 0:

                print()
                print("<-----INGRESAR EJEMPLARES----->")

                while True:

                    titulo = input("Ingrese el titulo del ejemplar que desea agregar: ").title()

                    if titulo in titulos:

                        while True:
                            ejemp = input(f"Ingrese cuantos ejemplares quiere agregar de {titulo}: ")

                            if ejemp.isdigit():
                                ejemp = int(ejemp)

                                if ejemp < 0:
                                    print("ERROR! No puede ingresar numeros negativos.")
                                    print("Inténtelo nuevamente")
                                    continue

                                else:
                                    posicion = titulos.index(titulo)
                                    ejemplares [posicion] += ejemp
                                    print(f"{ejemp} ejemplares de {titulo} agregados correctamente.")
                                    break

                            else:
                                print("ERROR! Debe ingresar un número entero.")
                                print("Inténtelo nuevamente")
                                continue
                    else:
                        print("ERROR! El titulo ingresado no se encuentra registrado")
                        continue
                    
                    while True:
                        si_no = input("¿Desea agregar mas ejemplares? (s/n)").lower()
                        if si_no == "s" or si_no == "n":
                            break
                        else:
                            print("ERROR! Debe ingresar 'S' o 'N'")
                            continue
                        
                    match si_no:
                            case "s":
                                continue
                        
                            case "n":
                                break

            else:
                print("No hay ningun titulo cargado")
                print("Primero debera utilizar la opcion 1 para registrar un título")

        case 3:
            if len(titulos) != 0:

                print()
                print("<-----LISTADO COMPLETO----->")
                for i in range (len(titulos)):
                    print(f"{titulos[i]}: {ejemplares[i]} ejemplares")
                
                print()
                input("Presione ENTER para volver al menú principal...")

            else:
                print("No existen libros cargados en el catalogo.")
                input("Presione ENTER para volver al menú principal...")

        case 4:
            print()
            print("<-----CONSULTAR DISPONIBILIDAD----->")
            while True:
                titulo = input("Ingrese el título de los ejemplares que desea consultar").title()

                if titulo.strip() == "":
                    print("ERROR! Debe ingresar un titulo valido.")
                    print("Intentelo nuevamnete")
                    continue

                elif not (titulo in titulos):
                    print("ERROR! El titulo no se encuentra registrado.")
                    print("Inténtelo nuevamente")
                    continue

                else:
                    posicion = titulos.index(titulo)
                    print (f"{titulo} posee {ejemplares [posicion]} ejemplares")

                while True:
                        si_no = input("¿Desea consultar por otro ttítulo? (s/n)").lower()

                        if si_no == "s" or si_no == "n":
                            break

                        else:
                            print("ERROR! Debe ingresar 'S' o 'N'")
                            continue
                        
                match si_no:
                    case "s":
                        continue

                    case "n":
                        break

        case 5:      
            for i in range(len(ejemplares)):
                if ejemplares [i] == 0:
                    agotados.append(i)

            if len(agotados) == 0:
                print("No existen ejemplares agotados")

            else:
                print("<-----EJEMPLARES AGOTADOS----->")
                for i in agotados:
                    print(f"{titulos[i]} — {ejemplares[i]} ejemplares")

                agotados.clear()
                print()
                input("Presione ENTER para volver al menú principal...")

        case 6:
            print()
            print("<-----AGREGAR TÍTULOS Y EJEMPLARES----->") 

            while True:
                
                titulo = input("Ingrese el título del libro que desea registar: ").title()

                if titulo.strip() == "":
                    print("ERROR! Debe ingresar un titulo valido.")
                    print("Intentelo nuevamnete")
                    continue

                elif titulo in titulos:
                    print("ERROR! El titulo ya se encuentra registrado.")
                    print("Inténtelo nuevamente")
                    continue

                else:
                    while True:
                        ejemp = input(f"Ingrese cuantos ejemplares de {titulo} desea agregar: ")
                        if ejemp.isdigit():
                                ejemp = int(ejemp)

                                if ejemp < 0:
                                    print("ERROR! No puede ingresar numeros negativos.")
                                    print("Inténtelo nuevamente")
                                    continue

                                else:
                                    break

                        else:
                            print("ERROR! Debe ingresar un número entero.")
                            print("Inténtelo nuevamente")
                            continue

                    titulos.append(titulo)
                    posicion = titulos.index(titulo)
                    ejemplares.insert(posicion, ejemp)
                    print("Título y ejemplares registrados correctamente")

                while True:
                    si_no = input("¿Desea agregar mas títulos y ejemplares? (s/n)").lower()

                    if si_no == "s" or si_no == "n":
                        break

                    else:
                        print("ERROR! Debe ingresar 'S' o 'N'")
                        continue
                        
                match si_no:
                    case "s":
                        continue

                    case "n":
                        break
                        
        case 7:
            if len(titulos) == 0:
                print("No existen titulos cargados, primero debe ingresar al menos un titulo")
                continue
            
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
                            while True:
                                print("<-----PRESTAMOS----->")
                                titulo = input("Ingrese el nombre del libro que desea prestar]").title()
                            
                                if titulo.strip() == "":
                                    print("ERROR! Debe ingresar un titulo valido.")
                                    print("Intentelo nuevamnete")
                                    continue

                                elif not(titulo in titulos):
                                    print("ERROR! El titulo no se encuentra registrado.")
                                    print("Inténtelo nuevamente")
                                    continue

                                else:
                                    while True:
                                        ejemp = input(f"¿Cuantos ejemplares de {titulo} quiere quitar del registro?")

                                        if ejemp.isdigit():
                                            ejemp = int(ejemp)

                                            if ejemp < 0:
                                                print("ERROR! No puede ingresar numeros negativos.")
                                                print("Inténtelo nuevamente")
                                                continue

                                            else:
                                                posicion = titulos.index(titulo)

                                                if ejemplares [posicion] - ejemp < 0:
                                                    print ("ERROR!")
                                                    print (f"Solo tiene [{ejemplares[posicion]} ejemplares de {titulo}.")
                                                    print ("Debe ingresar un número menor")
                                                    continue
                                                else:
                                                    ejemplares [posicion] -= ejemp
                                                    print("Registro de ejemplares actualizado con exito")
                                                    print(f"Le quedan disponibles {ejemplares[posicion]} ejemplares de {titulo}")
                                                    break
                                                    
                                        else:
                                            print("ERROR! Debe ingresar un número entero.")
                                            print("Inténtelo nuevamente")
                                            continue

                                
                            

                        case 2:
                            # Logica de devoluciones
                            pass

                        case 3:
                            break

                        case _:
                            print("ERROR! Debe ingresar un numero del 1 al 3.")
                            print("Inténtelo nuevamente")
                            continue

        case 8:
            print("Cerrando programa...")
            break

        case _:
            print("ERROR! Debes elegir un número del 1 al 8")