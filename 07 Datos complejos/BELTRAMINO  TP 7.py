# NOMBRE: Elías Joel Beltramino
# DNI: 42.127.826

# Ejercicio 1
# Diccionario con precios iniciales de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

# Agregar nuevas frutas y sus precios.
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Ejercicio 2
# Modificar precios de algunas frutas.
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio 3
# Convertir las keys en lista.
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)  # Imprime las frutas.



# Ejercicio 4.
num_telefonicos = {}
for i in range(5):
    print(f"Teléfono {i+1} de 5:")
    nombre = (input("Ingrese el nombre: ")).title()
    numero = input("Ingrese el número telefónico: ")
    num_telefonicos[nombre] = numero

while True:
    consulta = (input("Ingrese el nombre a consultar (o 'salir' para terminar): ")).title()

    if consulta.lower() == 'salir':
        break

    elif consulta in num_telefonicos:
        print(f"El número telefónico de {consulta} es: {num_telefonicos[consulta]}")

    else:
        print(f"No se encontró el nombre {consulta} en la agenda.")


# Ejercicio 5.
frase = input("Ingrese una frase: ").lower()
palabras_unicas = set(frase.split())
lista = frase.split()
diccionario = {}
for i in lista:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1

print(f"Las palabras únicas son: {palabras_unicas} ")
print(f"El diccionario de cantidad de veces es: {diccionario} ")



# Ejercicio 6. 
notas_estudiantes = {}
for i in range(3):
    print(f"Estudiante {i+1} de 3:")
    nombre = (input("Ingrese el nombre del estudiante: ")).title()

    while True:
        try:
            nota_1 = float(input("Ingrese la primer nota del estudiante (0 - 10): "))
            nota_2 = float(input("Ingrese la segunda nota del estudiante (0 - 10): "))
            nota_3 = float(input("Ingrese la tercera nota del estudiante (0 - 10): "))
            if all(0 <= nota <= 10 for nota in [nota_1, nota_2, nota_3]):
                break

            else:
                print("Error: Las notas deben estar entre 0 y 10. Intente nuevamente.")

        except ValueError:
            print("Error: Entrada inválida. Por favor ingrese un número válido para las notas.")

    notas_estudiantes[nombre] = (nota_1, nota_2, nota_3)

for nombre in notas_estudiantes:
    promedio = 0
    for nota in range(3):
        promedio += notas_estudiantes[nombre][nota]
    promedio /= 3
    print(f"El promedio de {nombre} es: {promedio:.2f}")


# Ejercicio 7.
parcial_1 = {"Joel", "flavia", "Gerardo", "Franco", "Abril"}
parcial_2 = {"Joel", "Antonella", "Abril", "Facundo", "Martin"}

interseccion = parcial_1 & parcial_2
diferencia_sim = parcial_1 ^ parcial_2
union = parcial_1 | parcial_2

print(f"Estudiantes que aprobaron ambos parciales: {interseccion}")
print(f"Estudiantes que aprobaron solo uno de los parciales: {diferencia_sim}")
print(f"Estudiantes que aprobaron al menos uno de los parciales: {union}")


# Ejercicio 8.
diccionario = {"banana" : 10, "manzana" : 5, "pera" : 2}
while True:
    print("Inventario de productos")
    print("1: Consultar stock de un producto")
    print("2: Agregar stock a un producto")
    print("3: Agregar stock de un nuevo producto")
    print("4: Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if not opcion.isdigit():
        print("Opción inválida. Por favor seleccione una opción válida.")
        continue

    match opcion:
        case "1":
            consulta = input("Ingrese el nombre del producto a consultar: ").lower()
            if consulta in diccionario:
                print(f"El stock de {consulta} es: {diccionario[consulta]}")
            else:
                print(f"El producto {consulta} no se encuentra en el inventario.")

        case "2":
            producto = input("Ingrese el nombre del producto al que desea agregar stock: ").lower()
            if producto in diccionario:
                stock = int(input(f"Ingrese la cantidad de stock a agregar a {producto}: "))
                diccionario[producto] += stock
                print(f"Nuevo stock de {producto}: {diccionario[producto]}")
            else:
                print(f"El producto {producto} no se encuentra en el inventario.")

        case "3":
            producto= input("Ingrese el nombre del nuevo producto: ").lower()
            if producto in  diccionario:
                print(f"El producto {producto} ya existe en el inventario.")
            else:
                stock = int(input(f"Ingrese la cantidad de stock para {producto}: "))
                diccionario[producto] = stock
                print(f"Producto {producto} agregado con stock {stock}.")

        case "4":
            print("Saliendo del programa.")
            break

        case _:
            print("Opción inválida. Por favor seleccione una opción válida.")
            continue



# Ejercicio 9.
agenda = {}
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
while True:
    print("1: Agregar evento.")
    print("2: Consultar evento.")
    print("3: Salir.")

    opcion = input("Seleccione una opción (1-3): ")

    if not opcion.isdigit():
        print("Opción inválida. Por favor seleccione una opción válida.")
        continue

    match opcion:
        case "1":
            while True:
                dia = input("Ingrese el día de la semana para el evento: ").title()

                if dia in dias:
                    hora = input("Ingrese la hora del evento: ")
                    descripcion = input("Ingrese la descripción del evento: ")

                    agenda [(dia, hora)] = descripcion
                    print(f"Evento agregado para el {dia} a las {hora}.")
                    break

                else:
                    print("Día inválido. Por favor ingrese un día válido de la semana.")
                    

        case "2":
            while True:
                dia = input("Ingrese el día de la semana del evento a consultar: ").title()
                hora = input("Ingrese la hora del evento a consultar: ")
                if (dia, hora) in agenda:
                    print(f"Evento para el {dia} a las {hora}: {agenda[(dia, hora)]}")
                    break
                else:
                    print(f"No hay evento programado para el {dia} a las {hora}.")

        case "3":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción inválida. Por favor seleccione una opción válida.")
            continue



# Ejercicio 10.
original = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Colombia": "Bogotá", "Chile": "Santiago"}
invertido = {}

for paises in original:
    invertido[original[paises]] = paises

print(f"Diccionario original: {original}")
print(f"Diccionario invertido: {invertido}")