# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
# for i in range(101):
#     print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene
# num = int(input("Ingrese un número entero: "))
# num_str = str(num)
# print(f"La cantidad de digitos es: {len(num_str)}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# suma = 0


# for i in range(num1+1, num2):
#     suma += i
# print(f"La suma de los números entre {num1} y {num2} es: {suma}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# sum = 0
# num = int(input("Ingrese un número entero (0 para salir): "))
# while num != 0:
#     sum += num
#     num = int(input("Ingrese otro número entero (0 para salir): "))
# print(f"La suma total es: {sum}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# num = int(input("Ingrese un número entre 0 y 9: "))
# intentos = 0
# import random
# num_random = random.randint(0, 9)
# while num != num_random:
#     intentos += 1
#     if num < num_random:
#         print("El número es mayor.")
#     else:
#         print("El número es menor.")
#     num = int(input("Ingrese otro número entre 0 y 9: "))
# print(f"¡Felicidades! Adivinaste el número {num_random} en {intentos} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
# for i in range(100, -1, -1):
#     if i % 2 == 0:
#         print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario
# n = int(input("Ingrese un número entero positivo: "))
# suma = 0
# for i in range(n + 1):
#     suma += i
# print("La suma de los números entre 0 y", n, "es:", suma)


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
# Cambiá este valor para probar con menos números
# cantidad = 100  

# pares = impares = positivos = negativos = 0

# for _ in range(cantidad):
#     num = int(input("Ingrese un número entero: "))
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1

# print("Pares:", pares)
# print("Impares:", impares)
# print("Positivos:", positivos)
# print("Negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
# Cambiá este valor para probar con menos números
# 

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# n = int(input("Ingrese un número entero: "))
# n_str= str(n)
# n_invertido = n_str[::-1] 
# n_invertido = int(n_invertido) 
# print("El número invertido es:", n_invertido)