# Elias Joel Beltramino
# TP 6
# DNI 42.127.826

# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola, Mundo!")

imprimir_hola_mundo()

# Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

nombre = input("Ingresa tu nombre: ")
saludar_usuario(nombre)

# Ejercicio 3
# Funciónes
def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
       
# Programa principal
# Solicitar datos al usuario           
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4
import math

# Funciones
# Calcula el área de un círculo
def calcular_area_circulo(radio: float) -> float:
    area = math.pi * radio ** 2
    return area

# Calcula el perímetro de un círculo
def calcular_perimetro_circulo(radio: float) -> float:
    perimetro = 2 * math.pi * radio
    return perimetro

# Programa principal
while True:
    radio = float(input("Ingrese el radio del círculo: "))

    # Verificamos que el radio sea positivo
    if radio <= 0:
        print("Error: El radio debe ser un número positivo.")
        continue
    else:
        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)
        print(f"El área del círculo es: {area:2f}")
        print(f"El perímetro del círculo es: {perimetro:2f}")
        break

# Ejercicio 5
# Funciones
# Convierte segundos a horas, minutos y segundos
def segundos_a_horas(segundos):
    horas = segundos // 3600
    segundos -= horas * 3600
    minutos = segundos // 60
    segundos -= minutos * 60

    return horas, minutos, segundos

# Programa principal
total_segundos = int(input("Ingrese el total de segundos: "))
horas, minutos, segundos = segundos_a_horas(total_segundos)
print(f"{total_segundos} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.")

# Ejercicio 6
# Funciones
# Muestra la tabla de multiplicar de un número dado
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
# Programa principal
while True:
    numero = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))
    if not numero.isdigit():
        print("Por favor, ingresa un número válido.")
        continue
    else:
        tabla_multiplicar(numero)
        break

# Ejercicio 7
# Funciones
# Realiza operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    
    return suma, resta, multiplicacion, division

# Programa principal
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

print("Resultados de las operaciones básicas:")
print(f"{num1} + {num2}: {suma}")
print(f"{num1} - {num2}: {resta}")
print(f"{num1} * {num2}: {multiplicacion}")
print(f"{num1} / {num2}: {division}")

# Ejercicio 8
# Funciónes
# Calcular el índice de masa corporal (IMC)
def  calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Programa principal
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

# Ejercicio 9
# Funcion para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * (9/5) + 32

# Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")

# Ejercicio 10
# Función para calcular el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
        
print(f"El promedio de {num1}, {num2} y {num3} es: {calcular_promedio(num1, num2, num3)}")