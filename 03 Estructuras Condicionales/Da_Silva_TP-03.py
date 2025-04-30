import random
from statistics import mean, median, mode

while True:
    print("Elija un ejercicio entre  1 y 10 (0 para salir):")
    ejercicio = int(input("Ejercicio: "))

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.  

    if ejercicio == 1:
        edad = int(input("Ingrese su edad: "))
        if edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
        break

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
    elif ejercicio == 2:
        nota = float(input("Ingrese su nota: "))
        if nota >= 6:
            print("Aprobado")
        else:
            print("Desaprobado")
       
    elif ejercicio == 3:
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar    
        num = int(input("Ingrese un número: "))
        if num % 2 == 0:
            print("Ha ingresado un número par")
        else:
            print("Por favor, ingrese un número par")    
       
    elif ejercicio == 4:
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
      edad = int(input("Ingrese su edad: "))
      if edad < 12:
          print("Niño/a")
      elif edad < 18:
          print("Adolescente")
      elif edad < 30:
          print("Adulto/a joven")
      else:
          print("Adulto/a") 
   
    elif ejercicio == 5:      

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string

        password = input("Ingrese una contraseña (8 a 14 caracteres): ")
        if len(password) >= 8 and len(password) <= 14:
            print("Ha ingresado una contraseña correcta")
        else:
            print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
   
    elif ejercicio == 6:    
#         escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
        num_random = [random.randint(1, 100) for _ in range(10)]
        print(num_random)
        if mean(num_random) > median(num_random):
            print("Sesgo positivo")
        elif mean(num_random) < median(num_random):
            print("Sesgo negativo")
        else:
            print("No hay sesgo")


    elif ejercicio == 7:

# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla

        frase = input("Ingrese una frase o palabra: ")
        if frase[-1].lower() in "aeiou":
            frase += "!"
        print(frase)
    elif ejercicio == 8:
#  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
        nombre = input("Ingrese su nombre: ")
        opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para capitalizar: "))
        if opcion == 1:
            print(nombre.upper())
        elif opcion == 2:
            print(nombre.lower())
        elif opcion == 3:
            print(nombre.title())
        else:
            print("Opción no válida")
    elif ejercicio == 9:
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
       magnitud = float(input("Ingrese la magnitud del terremoto: "))
       if magnitud < 3:
           print("Muy leve")
       elif magnitud < 4:
           print("Leve")
       elif magnitud < 5:
           print("Moderado")
       elif magnitud < 6:
           print("Fuerte")
       elif magnitud < 7:
           print("Muy Fuerte")
       else:
           print("Extremo")

    elif ejercicio == 10:
        hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))

        if hemisferio == "S":
            if (mes ==12 and dia >= 21) or (mes == 3 and dia <= 20):
                print("Verano")
            elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
                print("Otoño")
            elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
                print("Invierno")
            elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
                print("Primavera")    
        elif hemisferio == "N":
            if (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
                print("Verano")
            elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
                print("Otoño")
            elif (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
                print("Invierno")
            elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
                print("Primavera")

    elif ejercicio == 0:
        print("Saliendo...")
        break
    else:
        print("Ejercicio no válido. Por favor, elija un ejercicio entre 1 y 10 (0 para salir).")
        continue