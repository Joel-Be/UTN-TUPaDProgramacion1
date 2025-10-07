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
            pass

        case 3:
            pass

        case _:
           print ("ERROR!")
           print("El numero ingresaado no esta dentro de los parametros solicitados")
           print("Intentelo nuevamente")
           continue