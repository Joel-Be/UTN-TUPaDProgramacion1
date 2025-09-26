# EJERCICIO 1
# Inicializamos algunas variables que se utilizaran posteriormente
lista = []
suma = 0
menor = float ('inf')
mayor = float ('-inf')

# Solicitamos las notas de todos los estudiantes.
for i in range (0, 10):
    while True:
        nota = float (input(f"Ingrese la nota del estudiante numero {i+1}: "))
        if 0 <= nota <=10:
            break
        else:
            print ("ERROR! La nota debe ser entre 0 y 10")
    lista.append(nota)

# Calculamos las notas mayor y menor
for nota in lista:
    suma += nota
    if nota < menor:
        menor = nota
    if nota > mayor:
        mayor = nota
promedio = suma / len(lista)

# Mostramos la informacion solicitada en pantalla
print (f"Lista de notas: {lista}")
print (f"Promedio de todas las notas: {promedio}")
print (f"Nota mas alta: {mayor}")
print (f"Nota mas baja: {menor}")


# EJERCICIO 2
# Inicializamos la lista vacia.
lista = []

# A traves de un for que de 5 vueltas vamos agregando los productos a la lista.
for i in range(0, 5):
    producto = input(f"Ingrese un producto a la lista ({i+1} / 5): ").lower()
    lista.append(producto)

# Ordenamos la lista
lista = sorted (lista)

# Mostramos la la lista ordenada
print (f"Lista ordenada: {lista}")

# Preguntamos que producto desea eliminar, asegurandonos de que efectivamente se encuentre en la lista.
while True:
    eliminar = input("Que producto desea eliminar?: ").lower()
    if eliminar in lista:
        lista.remove (eliminar)
        print (f"{eliminar} eliminado exitosamente")
        break
    else:
        print (f"El producto {eliminar} no se encuentra en la lista {lista}")
        print ("Intentelo nuevamente")

# Mostramos la lista en pantalla
print (f"Lista actualizada: {lista}")


# EJERCICIO 3
# Importamos random e inicializamos listas.
import random
lista = []
lista_par = []
lista_impar = []

# Generamos la lista con 15 numeros al azar
for i in range (15):
    lista.append(random.randrange(1,101))

# Vamos cargagando en cada lista los numeros pares e impares por separado.
for n in lista:
    if n%2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

# Mostramos ambas listas en pantalla
print(f"Lista de numeros pares ({len(lista_par)} numeros): {lista_par}")
print(f"Lista de numeros impares ({len(lista_impar)} numeros): {lista_impar}")


# EJERCICIO 4
# Inicializamos la lista que aparece en los ejercicios y una vacia.
lista = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_final = []

# Solo cargamos en la nueva lista los elementos que no se encuentren en la misma.
for n in lista:
    if not(n in lista_final):
        lista_final.append(n)

# Mostramos el resultado en pantalla.
print (lista_final)


# EJERCICIO 5
# Inicializamos la lista de estudiantes vacia
estudiantes = []

# Ingresamos los nombres de todos los estudiantes presentes
for i in range (8):
    nombre = input(f"Ingrese el nombre de un estudiante ({i + 1} / 8)").title()
    estudiantes.append(nombre)

# Dentro de un bucle le preguntamos que desea realizar.
# Podra agregar o quitar estudiantes hasta que desee salir
while True:
    print("¿Que desea hacer con la lista?")
    print("1 - Agregar un estudiante a la lista.")
    print("2 - Quitar un estudiante de la lista.")
    print("3 - Finalizar y mostrar la lista final.")
    n = int(input("Ingrese el numero correspondiente:"))

    if n == 1:
        nombre = input("Ingrese el nombre del alumno que desea agregar: ").title()
        estudiantes.append(nombre)
        print(f"{nombre} agregado exitosamente.")
    elif n == 2:
        while True:
            nombre = input("Ingrese el nombre del alumno que desea quitar: ").title()
            if nombre in estudiantes:
                estudiantes.remove(nombre)
                print(f"{nombre} eliminado exitosamente.")
                break
            else:
                print ("ERROR! No se encuentra el nombre del estudiante en la lista")
                print ("Intentelo nuevamente")
    elif n == 3:
        break
    else:
        print("ERROR! El numero ingresado es invalido, por favor ingrese un numero de los que se encuentran en pantalla")

# Mostramos en pantalla la lista final.
print(f"Lista final: {estudiantes}")


# EJERCICIO 6
# Inicializamos matrices
lista =[]
lista_final = []

# Solicitamos al usuario que ingrese los 7 numeros
print("Vamos a ingresar 7 números en una lista")
for i in range (7):
    n = int(input(f"Ingrese un número ({i + 1} / 7): "))
    lista.append(n)

# Primero guardamos el ultimo en la nueva matriz
lista_final.append(lista[len(lista) - 1])

# Luego guardamos el resto mmenos el ultimo
for n in range(len(lista)-1):
    lista_final.append(lista[n])

# Mostramos en pantalla
print(f"Lista sin modificar: {lista}")
print(f"Lista rotada: {lista_final}")


# EJERCICIO 7
# Inicializamos variables y matrices
matriz = []
dias = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
promedio_mayor = 0
promedio_menor = 0
amplitud = float('-inf')
dia_amplitud = "dia"

# Solicitamos las temperaturas de cada dia
for i in dias:
    print()
    print(i)
    minima = float(input("Ingrese la temperatura mínima: "))
    maxima = float(input("Ingrese la temperatura máxima: "))
    matriz.append([minima, maxima])

#calculamos los promedios y que dia tuvo mayor amplitud termica.
for f in range(7):
    promedio_menor += matriz [f] [0]
    promedio_mayor += matriz [f] [1]
    if matriz [f] [1] - matriz [f] [0] > amplitud:
        amplitud = matriz [f] [1] - matriz [f] [0]
        dia_amplitud = dias[f]
promedio_mayor = promedio_mayor / 7
promedio_menor = promedio_menor / 7

# Mostramos en pantalla
print (f"Promedio semanal de las mayores temperaturas es de: {promedio_mayor}")
print (f"Promedio semanal de las menores temperaturas es de: {promedio_menor}")
print (f"El dia con mayor aplitud termica fue: {dia_amplitud}")


# EJERCICIO 8
#Inicializamos algunas matyrices y variables para utilizar luego
estudiantes = []
materias = ["Programacion 1", "AySO", "Matematica"]
promedios = []
promedio_materia = 0

# Solicitamos nombre de cada est. y notas por materia. Calculamos el promedio y lo guardamos junto con todo en la matriz estudiantes
for i in range(5):
    print()
    nombre = input(f"Ingrese el nombre del estudiante ({i+1} / 5): ").title()
    p1 = float(input("Ingrese nota de Programacion 1: "))
    ayso = float(input("Ingrese nota de AySO: "))
    matematica = float(input("Ingrese nota de Matematica: "))
    promedio_estudiante = (p1 + ayso + matematica) / 3

    estudiantes.append([nombre, p1, ayso, matematica, promedio_estudiante])

# Calculamos el promedio de cada materia y la guardamos en la matriz PROMEDIOS
for f in range(1, 4):
    promedio_materia = 0
    for c in range(5):
        promedio_materia +=  estudiantes [c][f]
    promedio_materia = promedio_materia / 5
    promedios.append([materias [f-1], promedio_materia])

# Mostramos en pantalla el promedio de cada estudiante
print()
print ("Promedio de cada estudiante")
for e in range (5):
    print (f"{estudiantes[e][0]}: {estudiantes[e][4]}")

# Mostramos el promedio de cada materia
print()
print("Promedio de cada materia")
for m in range(3):
    print(f"{promedios[m][0]}: {promedios[m][1]}")


# EJERCICIO 9
# Inicializamos el tablero vacio
tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
# Inicializamos variable booleana que determina cuando termina el partido
fin = False

#Mostramos en pantalla el tablero inicial
print()
print(tablero[0])
print(tablero[1])
print(tablero[2])

# Este while detrminara cada vuelta, en total seran 3
while True:
    
    
    for jugador in range (1, 3):

        # Identificamos de quien es el turno para saber que ficha poner
        if jugador == 1:
            ficha = "X"
        else:
            ficha = "O"

        # Solicitamos al usuario la fila y la columna
        print(f"TURNO DE JUGADOR {jugador} --> {ficha}")
        fila = int(input("Ingrese la FILA de la posicion deseada: "))
        columna = int(input("Ingrese la COLUMNA de la posicion deseada: "))

        # Impactamos la jugada en el tablero
        tablero [fila - 1][columna - 1] = ficha
        
        # Mostramos el tablero cada jugada
        print()
        print(tablero[0])
        print(tablero[1])
        print(tablero[2])

        # La partida solo termina cuando alguien gana
        if (tablero[0][0] == tablero[1][0] == tablero[2][0] != "-") or (tablero[0][1] == tablero[1][1] == tablero[2][1] != "-") or (tablero[0][2] == tablero[1][2] == tablero[2][2] != "-"):
            fin = True
        elif (tablero[0][0] == tablero[0][1] == tablero[0][2] != "-") or (tablero[1][0] == tablero[1][1] == tablero[1][2] != "-") or (tablero[2][0] == tablero[2][1] == tablero[2][2] != "-"):
            fin = True
        elif (tablero[0][0] == tablero[1][1] == tablero[2][2] != "-") or (tablero[0][2] == tablero[1][1] == tablero[2][0] != "-"):
            fin = True

        # Cuando el booleano este en True detenemos todo
        if fin == True:
            break
    if fin == True:
        break
# Anunciamos al ganador
print (f"EL GANADOR ES JUGADOR {jugador}!!!")


# EJERCICIO 10
# Declaramos matrices y variables que utilizaremos a lo largo del algoritmo.
ventas = []
dias = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
total_manzanas = 0
total_bananas = 0
total_naranjas = 0
total_peras = 0
mayores_ventas = int('-inf')
mayores_ventas_dia = "vacio"
producto_mas_vendido = []

# Un for recorrera todos los días mientras el usuario carga las ventas, luego se guardan dia y ventas en la lista.
# Tambien aprovechamos y ya guardamos las ventas totales de cada día.
for i in dias:
    print()
    print(i)
    manzanas = int(input(f"Ingrese cuantas unidades de MANZANAS se vendieron: "))
    bananas = int(input(f"Ingrese cuantas unidades de BANANAS se vendieron: "))
    naranjas = int(input(f"Ingrese cuantas unidades de NARANJAS se vendieron: "))
    peras = int(input(f"Ingrese cuantas unidades de PERAS se vendieron: "))
    ventas_totales = manzanas + bananas + naranjas + peras
    ventas.append([i, manzanas, bananas, naranjas, peras, ventas_totales])

# Calculamos cuantas ventas por semana tiene cada producto
# Tambien guardamos el dia que hayan tenido mas ventas.
for i in range(7):
    total_manzanas += ventas[i][1]
    total_bananas += ventas[i][2]
    total_naranjas += ventas[i][3]
    total_peras += ventas[i][4]

    if ventas [i][5] > mayores_ventas:
        mayores_ventas = ventas[i][5]
        mayores_ventas_dia = ventas [i][0]

# Identificamos que producto se vendio mas en toda la semana.
# Lo guardamos en una variable junto con su total de ventas
if (total_manzanas >=  total_bananas) and (total_manzanas >=  total_naranjas) and (total_manzanas >=  total_peras):
    producto_mas_vendido.append("MANZANAS")
    producto_mas_vendido.append(total_manzanas)
elif (total_bananas >=  total_manzanas) and (total_bananas >=  total_naranjas) and (total_bananas >=  total_peras):
    producto_mas_vendido.append("BANANAS")
    producto_mas_vendido.append(total_bananas)
elif (total_naranjas >=  total_manzanas) and (total_naranjas >=  total_bananas) and (total_naranjas >=  total_peras):
    producto_mas_vendido.append("NARANJAS")
    producto_mas_vendido.append(total_naranjas)
else:
    producto_mas_vendido.append("PERAS")
    producto_mas_vendido.append(total_peras)

# Mostramos toda la información solicitada en pantalla.
print()
print(f"Total de manzanas vendidas: {total_manzanas}")
print(f"Total de bananas vendidas: {total_bananas}")
print(f"Total de naranjas vendidas: {total_naranjas}")
print(f"Total de peras vendidas: {total_peras}")
print()
print(f"El día con mayores ventas fue: {mayores_ventas_dia}")
print(f"El producto mas vendido de la semana fueron las {producto_mas_vendido[0]} con {producto_mas_vendido[1]} ventas.")