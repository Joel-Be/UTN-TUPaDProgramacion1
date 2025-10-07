while True:
    print("-----MENU PRINCIPAL-----")
    print("1. Simulación de Puertas Lógicas Básicas")
    print("2. Conversión de Números")
    print("3. ")
    print("4. Salir del programa")
    opcion = input("Elegí una opción: ")

    if not opcion.isdigit():
        print("Debes ingresar un número válido")
        continue

    opcion = int(opcion)

    match opcion:

        case 1:
            pass

        case 2:
            while True:
                print("-----CONVERSIÓN DE NÚMEROS-----")
                print("1. Convertir de Natural a Binario")
                print("2. Convertir de Binario a Natural")
                print("3. Volver al menu principal")

                opcion = input("Elegí una opción: ")

                if not opcion.isdigit():
                    print("Debes ingresar un número válido")
                    continue

                opcion = int(opcion)

                match opcion:

                    case 1:
                        while True:
                            # convertir de natural a binario .
                            natural = input("Ingrese un número natural mayor o igual a 0: ")

                            if not natural.isdigit():
                                print("Debes ingresar un número válido")
                                continue
                            
                            natural = int(natural)
                            if natural < 0:
                                print("Debes ingresar un número natural (0 o mayor)")
                                continue
                            
                    case 2:
                        pass

                    case 3:
                        break


        case 3:
            pass

        case 4:
            print("Cerrando programa...")
            break

        case _:
           print ("ERROR!")
           print("El numero ingresaado no esta dentro de los parametros solicitados")
           print("Intentelo nuevamente")
           continue