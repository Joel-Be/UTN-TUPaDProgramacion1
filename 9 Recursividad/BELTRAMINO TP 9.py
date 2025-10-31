# NOMBRE: Elías Joel Beltramino 
# DNI: 42.127.826

# TP 9 - Recursividad


# EJERCICIO 1:

# Definición de funciones.
def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)

def factorial_hasta_n(n):
    if n == 1:
        print("1! = 1")
        return 1
    else:
        factorial_hasta_n(n - 1)
        print(f"{n}! = {factorial(n)}")

# Programa Principal
n = int(input("Ingrese un número entero positivo: "))
factorial_hasta_n(n)

# --------------------------------------------------------------

# EJERCICIO 2:

# Definición de funciones.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_hasta_n(n):
    if n == 0:
        print("F(0) = 0")
    else:
        fibonacci_hasta_n(n - 1)
        print(f"F({n}) = {fibonacci(n)}")

# Programa Principal
n = int(input("Ingrese un número entero positivo: "))
fibonacci_hasta_n(n)

# --------------------------------------------------------------

# EJERCICIO 3:

# Definición de funciones.
def potencia(x, y):
    return 1 if y == 0 else x * potencia(x, y - 1)

# Programa Principal
x = int(input("Ingrese la base (entero): "))
y = int(input("Ingrese el exponente (entero no negativo): "))
print(f"{x}**{y} = {potencia(x, y)}")

# --------------------------------------------------------------

# EJERCICIO 4:

# Definición de funciones.
def decimal_binario(n):
    if n == 0:
        return ""
    else:
        return f"{str(decimal_binario(n//2))}{str(n%2)}"

# Programa Principal
n = int(input("Ingrese un número entero positivo: "))
print(f"El número {n} en binario es: {decimal_binario(n)}")

# --------------------------------------------------------------

# EJERCICIO 5:

# Definición de funciones.
def es_palindromo(cadena, inicio, final):
  
    if inicio >= final:
        return True
    
    else:
        if cadena[inicio] == cadena[final] and es_palindromo(cadena, inicio + 1, final - 1):
            return True
        else:
            return False

# Programa Principal
cadena = input("Ingrese una cadena de caracteres: ").lower()
print ("Es palindromo!") if es_palindromo(cadena, 0, len(cadena) - 1) else print("No es palindromo.")

# --------------------------------------------------------------

# EJERCICIO 6:

# Definición de funciones.
def suma_digitos(n):
    n = abs(n)
    return 0 if n == 0 else n % 10 + suma_digitos(n // 10)
        
# Programa Principal
n = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")

# --------------------------------------------------------------

# EJERCICIO 7:

# Definición de funciones.
def contar_bloques(n):
    return 1 if n == 1 else n + contar_bloques(n - 1)
    
# Programa Principal
n = int(input("Ingrese la cantidad de bloques de la base de la pirámide: "))
print(f"La cantidad total de bloques en la pirámide es: {contar_bloques(n)}")

# --------------------------------------------------------------

# EJERCICIO 8:

# Definición de funciones.
def contar_digito(numero, digito):
    numero = abs(numero)
    if numero == 0 and digito == 0:
        return 1
    elif numero == 0:
        return 0
    else:
        return 0 + (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
    
# Programa Principal
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9) a contar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")