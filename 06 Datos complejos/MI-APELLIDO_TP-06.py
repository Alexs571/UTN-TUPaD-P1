# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
# Práctico 6: Estructuras de datos complejas

# Objetivo: Dominar el uso de estructuras de datos complejas en Python para
# almacenar, organizar y manipular datos de manera eficiente, aplicando
# buenas prácticas y optimizando el rendimiento de las aplicaciones. 

# Resultados de aprendizaje:
# 1. Comprensión y aplicación de iterables: listas, tuplas y sets. 
# 2. Introducción a estructuras de datos complejas: diccionarios. 

# --- Actividades ---

# 1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200 
# Manzana = 1500 
# Pera = 2300 

print("--- Actividad 1 ---")
print("Diccionario inicial:", precios_frutas)
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Diccionario después de añadir frutas:", precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# Banana = 1330 
# Manzana = 1700 
# Melón = 2800 

print("\n--- Actividad 2 ---")
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("Diccionario después de actualizar precios:", precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios. 

print("\n--- Actividad 3 ---")
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# Luego, pedí un nombre y mostrale el número asociado, si existe. 

print("\n--- Actividad 4 ---")
contactos = {}
print("Por favor, carga 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    numero = input(f"Ingresa el número de teléfono para {nombre}: ")
    contactos[nombre] = numero

nombre_buscar = input("Ingresa el nombre del contacto que quieres buscar: ")
if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print(f"El contacto {nombre_buscar} no se encuentra.")

# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set). 
# Un diccionario con la cantidad de veces que aparece cada palabra. 

print("\n--- Actividad 5 ---")
frase = input("Ingresa una frase: ")
palabras = frase.lower().replace(",", "").replace(".", "").split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

recuento_palabras = {}
for palabra in palabras:
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1
print("Recuento de palabras:", recuento_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

print("\n--- Actividad 6 ---")
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
    notas_str = input(f"Ingresa las 3 notas de {nombre} separadas por comas (ej: 7,8,9): ")
    try:
        notas = tuple(map(int, notas_str.split(',')))
        if len(notas) == 3:
            alumnos[nombre] = notas
        else:
            print("Debe ingresar exactamente 3 notas. Por favor, intenta de nuevo.")
            i -= 1
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar números separados por comas.")
        i -= 1

print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# Mostrá los que aprobaron ambos parciales. 
# Mostrá los que aprobaron solo uno de los dos. 
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

print("\n--- Actividad 7 ---")
parcial1_aprobados = {1, 2, 3, 4, 5, 9, 10}
parcial2_aprobados = {4, 5, 6, 7, 8, 9}

ambos_parciales = parcial1_aprobados.intersection(parcial2_aprobados)
print("Estudiantes que aprobaron ambos parciales:", ambos_parciales)

solo_uno = parcial1_aprobados.symmetric_difference(parcial2_aprobados)
print("Estudiantes que aprobaron solo uno de los dos parciales:", solo_uno)

al_menos_uno = parcial1_aprobados.union(parcial2_aprobados)
print("Estudiantes que aprobaron al menos un parcial (sin repetir):", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario:
# Consultar el stock de un producto ingresado. 
# Agregar unidades al stock si el producto ya existe. 
# Agregar un nuevo producto si no existe. 

print("\n--- Actividad 8 ---")
stock_productos = {
    "Leche": 50,
    "Pan": 30,
    "Huevos": 100,
    "Arroz": 25
}

while True:
    print("\n--- Gestión de Stock ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar stock (o nuevo producto)")
    print("3. Mostrar todo el stock")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        producto = input("Ingresa el nombre del producto a consultar: ")
        if producto in stock_productos:
            print(f"El stock de {producto} es: {stock_productos[producto]}")
        else:
            print("Producto no encontrado en el stock.")
    elif opcion == '2':
        producto = input("Ingresa el nombre del producto: ")
        try:
            cantidad = int(input("Ingresa la cantidad a agregar: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            if producto in stock_productos:
                stock_productos[producto] += cantidad
                print(f"Se agregaron {cantidad} unidades a {producto}. Nuevo stock: {stock_productos[producto]}")
            else:
                stock_productos[producto] = cantidad
                print(f"{producto} agregado al stock con cantidad inicial de {cantidad}.")
        except ValueError:
            print("Cantidad inválida. Por favor, ingresa un número entero.")
    elif opcion == '3':
        if stock_productos:
            print("\n--- Stock Actual ---")
            for prod, stock in stock_productos.items():
                print(f"{prod}: {stock} unidades")
        else:
            print("El stock está vacío.")
    elif opcion == '4':
        print("Saliendo del programa de gestión de stock.")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora. 

print("\n--- Actividad 9 ---")
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Cita con el médico",
    ("viernes", "18:00"): "Cena con amigos"
}

dia_consulta = input("Ingresa el día a consultar (ej: lunes): ").lower()
hora_consulta = input("Ingresa la hora a consultar (ej: 10:00): ")

clave_consulta = (dia_consulta, hora_consulta)
if clave_consulta in agenda:
    print(f"Actividad para {dia_consulta} a las {hora_consulta}: {agenda[clave_consulta]}")
else:
    print(f"No hay actividades programadas para {dia_consulta} a las {hora_consulta}.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# Las capitales sean las claves. 
# Los países sean los valores. 

print("\n--- Actividad 10 ---")
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "España": "Madrid",
    "Francia": "París",
    "México": "Ciudad de México"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario original (País: Capital):", paises_capitales)
print("Diccionario invertido (Capital: País):", capitales_paises)