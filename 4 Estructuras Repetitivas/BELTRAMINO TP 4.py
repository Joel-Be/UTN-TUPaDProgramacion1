#           TP 4 REPETITIVAS
#   Nombre: Elías Joel Beltramino
#   DNI: 42.127.826

#   Ejercicio 1
#Definimos el for que muestre en pantalla de 0 a 100
for cont in range (101):
    print (cont)

#   Ejercicio 2
#El usuario ingresa n.
n = int(input("Ingrese un numero: "))

#definimos digitos en 1 y x como el valor absoluto de n.
digitos = 1
x =  abs(n)

#Dividimos entre 10 hasta que el valor sea menor que 10
while x >= 10:
    x = x // 10
    digitos+=1

#Mostramos resultado en pantalla
print (f"Hay {digitos} digitos en {n}")

#   Ejercicio 3
#Solicitamos los numeros al usuaro y definimos resultado en 0
x1 = int(input("Ingrese el primer numero entero: "))
x2 = int(input("Ingrese el segundo numero entero: "))
resultado = 0

#Nos aseguramos de que valor ingresado es menor y usamos el for correspondiente.
if x1 < x2:
    for cont in range (x1+1, x2):
        resultado += cont
elif x1 > x2:
    for cont in range (x2+1, x1):
        resultado += cont

#Mostramos el resultado en pantalla.
print (f"El resultado de los numeros enteros entre {x1} y {x2} es: {resultado}")

#   Ejercicio 4
#Definimos la variable de contador y la de suma
cont = 0
suma = 0

#Utilizamos un while con un valor de verdadero para que ingrese directamente
while True:
    x = int(input(f"Ingrese un numero ({cont + 1}° numero) (Ingrese 0 para mostrar el resultado): "))
    #cortamos el bucle si el valor es 0
    if (x==0):
        break

    suma += x
    cont += 1

#Mostramos el resultado
print (f"El resultado de los {cont} numeros ingresados es de: {suma}")

#   Ejercicio 5
import random

#definimos el numero random y el contador de intentos en 0 
num = random.randint(0, 9)
cont = 0

#Hacemos un while que entre directamente, consultamos el numero y sumamos 1 al contador de intentos
while True:
    x = int(input(f"Adivine el numero aleatorio entre 0 y 9 (Intento numero {cont+1}): "))
    cont += 1

    #Si aciertan el numero el bucle se va a detener
    if x == num:
        print ("CORRECTO!")
        break
    else:
        print("INCORRECTO!")
        print("Intentelo nuevamente")

#Mostramos resultado en pantalla
print (f"Le costo {cont} intentos descifrar el numero")

#   Ejercicio 6
#Simplemente comenzamos el for en 100 y le vamos restando 2 (siempre van a ser numero pares), en cada ciclo mostramos la variable.
for i in range (100, -1, -2):
    print(i)

#   Ejercicio 7
#Solicitamos al usuario un numero entero positivo
n = int(input("Ingrese un numero entero positivo: "))
suma = 0

#Verificamos que el usuario efectivamente ingrese un numero entero positivo
if n < 0:
    print ("ERROR!")
    print ("El numero ingresado es negativo, intentelo nuevamente.")
else:
    #A rtaves de un for sumamos todos los numeros comprendidos entre 0 y n
    for i in range (0, n + 1):
        suma += i
    print (f"La suma enre [0 - {n}] da como resultado {suma}")

#   Ejercicio 8
#Definimos las variables en 0.
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range (1, 101):
    #Solicitamos al usuario que ingrese un numero.
    n = int(input(f"Ingrese un numero [{i} / 100]"))
    #Consideramos el 0 como par.
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    #Consideramos el 0 como positivo.
    if n >= 0:
        positivos += 1
    else:
        negativos += 1
#Mostramos en pantalla los resultados.
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")

#   Ejercicio 9
#Definimos la cantidad de numeros que el programa admitira ingresar.
cantidad_num = 100
#Definimos media en 0.
media = 0

for i in range (0, cantidad_num):
    #Solicitamos al usuario que ingrese un numero.
    n = int(input(f"Ingrese un numero [{i+1} / {cantidad_num}]: "))
    #sumamos ese numero al la variable media.
    media += n
#Calculamos la media de todos los numeros ingresados.
media = float(media / cantidad_num)
#Mostramos el resultado en pantalla.
print(f"La media de los {cantidad_num} ingresados es de: {media}")

#   Ejercicio 10
#Solictamos al usuario que ingrese un numero.
n = int(input("Ingrese un numero: "))
#Identificamos la cantidad de digitos para saber cuantas veces repetir el digito.
largo = len(str(abs(n))) - 1
#Obtenemos el valor absoluto del numero para operar sin errores.
valor = abs(n)
#Definimos la variable que mostrara el resultado en 0.
invertido = 0
#Con un for que se repita desde el valor de largo hasta 0 invertimos el numero.
for i in range (largo, -1, -1):
    digito = valor % 10
    valor //= 10
    invertido = invertido + (digito * (10**i))
#Identificamos si el numero ingresado es positivo o negativo para acomodar el resultado
if n<0:
    invertido = invertido * (-1)
#Mostramos el resultado en pantalla.
print (f"{n} invertido es: {invertido}.")