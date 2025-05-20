# 1
def imprimir_hola_mundo():
    print("Hola Mundo")
    
    
#2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
    
    
#3 
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    return None
    
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = int(input("Ingrese su edad: "))
# residencia = input("Ingrese su lugar de residencia: ")
# informacion_personal(nombre, apellido, edad, residencia)

#4
def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

# radio = float(input("Ingrese el radio del círculo: "))
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)
# print(f"El área del círculo es: {area}")
# print(f"El perímetro del círculo es: {perimetro}")

#5
def segundos_a_horas(segundos):
    horas = segundos // 3600
#     return horas

# segundos = int(input("Ingrese la cantidad de segundos: "))
# horas = segundos_a_horas(segundos)
# print(f"{segundos} segundos son {horas} horas")

#6
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
   

# numero = int(input("Ingrese un número: "))
# tabla_multiplicar(numero)

#7
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    
    return suma, resta, multiplicacion, division    

# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# suma, resta, multiplicacion, division = operaciones_basicas(a, b)
# print(f"Suma: {suma}")
# print(f"Resta: {resta}")
# print(f"Multiplicación: {multiplicacion}")
# print(f"División: {division}")

#8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# altura = float(input("Ingrese su altura en metros: "))
# peso = float(input("Ingrese su peso en kilogramos: "))
# imc = calcular_imc(peso, altura)
# print(f"Su IMC es: {imc}")

#9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# temp_celsius = float(input("Ingrese la temperatura en Celsius: "))
# temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
# print(f"{temp_celsius}°C son {temp_fahrenheit}°F")


#10
def calcular_promedio(a, b,c):
    promedio = (a + b + c) / 3
    return promedio

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

print(f"El promedio de {a}, {b} y {c} es: {calcular_promedio(a, b, c)}")