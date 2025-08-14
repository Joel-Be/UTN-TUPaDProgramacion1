#Ejercicio 1
print ("Hola Mundo!")

#Ejercicio 2
nombre = input ("Ingrese su numbre: ")
print (f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su numbre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input ("Ingrese su edad: "))
residencia = input ("Ingrese su lugar de residencia actual: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#Ejercicio 4
radio = float (input ("Ingrese el radio del círculo: "))
area = 3.1416 * (radio**2)
perimetro = 2 * 3.1416 * radio
print (f"El área es {area} y el perímetro es {perimetro}")

#Ejercicio 5
segundos = int(input("Ingrese una cantidad de  segundos: "))
horas = segundos / 3600
print (f"{segundos} segundos equivale a {horas} horas.")

#Ejercicio 6
n = int(input("Ingrese un número: "))
print (n, "x 1 = ", n*1)
print (n, "x 2 = ", n*2)
print (n, "x 3 = ", n*3)
print (n, "x 4 = ", n*4)
print (n, "x 5 = ", n*5)
print (n, "x 6 = ", n*6)
print (n, "x 7 = ", n*7)
print (n, "x 8 = ", n*8)
print (n, "x 9 = ", n*9)
print (n, "x 10 = ", n*10)

#Ejercicio 7
n1 = int(input("Ingrese el primer número entero distinto de 0: "))
n2 = int(input("Ingrese el segundo número entero distinto de 0: "))
print (n1, "+", n2, " = ", n1+n2)
print (n1, "-", n2, " = ", n1-n2)
print (n1, "x", n2, " = ", n1*n2)
print (n1, "/", n2, " = ", n1/n2)

#Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura**2)
print (f"Su indice de masa corporal es de {imc}")

#Ejercicio 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheint = (9/5) * celsius + 32
print (f"{fahrenheint} grados Fahrenheit")

#Ejercicio 10
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
print ("El promedio de los tres números es de ", (n1+n2+n3)/3)