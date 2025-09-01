#           TP 3 CONDICIONALES
#   Nombre: Elías Joel Beltramino
#   DNI: 42.127.826

#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print ("Es mayor de edad")
else:
    print ("Es menor de edad")


#Ejercicio 2
nota = float(input("Ingrese una nota de 0 al 10: "))
if nota <= 10 and nota >= 0:
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")
else:
    print("La nootra no cumple los parametros solicitados")


#Ejercicio 3
n = int(input("Ingrese un número par: "))
#considerando que el cero no es par ni impar
if (n == 0) or (n%2 != 0):
    print("Por favor, ingrese un número par")
else:
    print("Ha ingresado un número par")


#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad >= 0: 
    if edad < 12:
        print("Niño/a")
    elif 12 <= edad < 18:
        print("Adolescente")
    elif 18 <= edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")
else:
    print("La edad no puede ser negativa")


#Ejercicio 5
passw = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

if 8 <= len(passw) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Sesgo positivo")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo negativo")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("Sin sesgo")
else:
    print("No se cumple ninguna de las condiciones")


#Ejercicio 7
string = input("Ingrese una palabra o frase: ")

if len(string) > 1:

    if string[len(string)-1]=="a" or string[len(string)-1]=="e" or string[len(string)-1]=="i" or string[len(string)-1]=="o" or string[len(string)-1]=="u":
        print (f"{string}!")

    elif string[len(string)-1]=="A" or string[len(string)-1]=="E" or string[len(string)-1]=="I" or string[len(string)-1]=="O" or string[len(string)-1]=="U":
        print (f"{string}!")
        
    else:
        print (string)

else:
    print("Debe ingresar una frase o palabra, intentelo nuevamente")


#Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("1: Si quiere su nombre en mayúsculas.")
print("2: Si quiere su nombre en minúsculas.")
print("3: Si quiere su nombre con la primera letra mayúscula.")
n = int(input("Ingrese el numero de la accion que desea realizar: "))

if 1<=n<=3:
    if n==1:
        print(nombre.upper())
    elif n==2:
        print(nombre.lower())
    else:
        print(nombre.lower().title())
else:
    print ("El numero ingresado es incorrecto, por favor vuelva a intentarlo")


#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud >= 0:
    if magnitud<3:
        print ("Muy leve (imperceptible)")
    elif 3 <= magnitud < 4:
        print ("Leve (ligeramente perceptible).")
    elif 4 <= magnitud < 5:
        print ("Moderado (sentido por personas, pero generalmente no causa daños).")
    elif 5 <= magnitud < 6:
        print ("Fuerte (puede causar daños en estructurasdébiles).")
    elif 6 <= magnitud < 7:
        print ("Muy Fuerte (puede causar daños significativos).")
    else:
        print ("Extremo (puede causar graves daños a gran escala).")
else:
    print ("El numero ingresado es incorrecto")


#Ejercicio 10
hemisferio = input ("En que hemisferio se encuentra? N (Norte) o S (Sur): ")
hemisferio = hemisferio.lower()
ok = False
if hemisferio == "n" or hemisferio == "s":
    print ("1: Enero")
    print ("2: Febrero")
    print ("3: Marzo")
    print ("4: Abril")
    print ("5: Mayo")
    print ("6: Junio")
    print ("7: Julio")
    print ("8: Agosto")
    print ("9: Septiembre")
    print ("10: Octubre")
    print ("11: Noviembre")
    print ("12: Diciembre")
    mes = int(input("Ingrese el numero del mes del año en el que se encuentra: "))

    if 1 <= mes <= 12:
        dia = int(input("Ingrese el numero del dia actual: "))
        if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and (1<=dia<=31):
            ok = True
        elif (mes==4 or mes==6 or mes==9 or mes==11) and (1<=dia<=30):
            ok = True
        elif mes==2 and 1<=dia<=29:  
            ok = True
        else:
            print("ERROR")
            print("El dia ingresado no existe en el mes seleccionado")
            print("Intentelo nuevamente") 
    else:
        print("ERROR")
        print("El valor ingresado no coincide con los solicitados")
        print("Intentelo nuevamente")        
else:
    print("ERROR")
    print("El valor ingresado no coincide con los solicitados")
    print("Intentelo nuevamente")

if ok == True:
    if mes == 1 or mes == 2:
        print ("Invierno") if (hemisferio=="n") else print("Verano")
    elif mes == 3:
        if dia<=20:
            print ("Invierno") if (hemisferio=="n") else print("Verano")
        else:
            print ("Primavera") if (hemisferio=="n") else print("Otoño")
    elif mes == 4 or mes == 5:
        print ("Primavera") if (hemisferio=="n") else print("Otoño")
    elif mes == 6:
        if dia<=20:
            print ("Primavera") if (hemisferio=="n") else print("Otoño")
        else:
            print ("Verano") if (hemisferio=="n") else print("Invierno")
    elif mes == 7 or mes == 8:
        print ("Verano") if (hemisferio=="n") else print("Invierno")
    elif mes == 9:
        if dia<=20:
            print ("Verano") if (hemisferio=="n") else print("Invierno")
        else:
            print ("Otoño") if (hemisferio=="n") else print("Primavera")
    elif mes == 10 or mes == 11:
        print ("Otoño") if (hemisferio=="n") else print("Primavera")
    elif mes == 12:
        if dia<=20:
            print ("Otoño") if (hemisferio=="n") else print("Primavera")
        else:
            print ("Invierno") if (hemisferio=="n") else print("Verano")