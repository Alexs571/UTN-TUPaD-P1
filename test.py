def funcion_m(num1, num2):
    resultado = 1200 # Este valor se sobrescribe siempre
    if num1 % 2 == 0:
        resultado = num1 * num2
    else:
        resultado = num2 * num1
    return resultado

def funcion_s(x, t, z):
    # Paso 1: Calcular x (x original es 3, x nuevo es 6)
    x = funcion_m(x, 2)

    # Paso 2: Calcular t (usando el nuevo x=6. El segundo blanco es 3)
    t = funcion_m(x, funcion_m(x, 3)) # <--- PRIMER BLANCO

    # Paso 3: Calcular z (usando el nuevo x=6 y el nuevo t=108. El primer blanco es x)
    z = funcion_m(x, t) # <--- SEGUNDO BLANCO

    return x, t, z

a = 3
b = 7
c = 4

# La función funcion_s devolverá (6, 108, 648)
a, b, c = funcion_s(a, b, c)

print(f"'{a}', '{b}', '{c}'") # La salida será '6', '108', '648'