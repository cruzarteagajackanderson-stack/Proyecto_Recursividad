# PROYECTO: FUNCIONES RECURSIVAS EN PYTHON


# PASO 3: FUNCION FACTORIAL

def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Ingrese un numero entero no negativo")

    # Caso base
    if n == 0 or n == 1:
        return 1

    # Caso recursivo
    return n * factorial(n - 1)


# FUNCION POTENCIA

def potencia(base, exponente):
    if not isinstance(exponente, int) or isinstance(exponente, bool) or exponente < 0:
        raise ValueError("El exponente debe ser no negativo")

    # Caso base
    if exponente == 0:
        return 1

    # Caso recursivo
    return base * potencia(base, exponente - 1)


# PASO 4: CONTEO RECURSIVO EN UNA LISTA

def contar_elemento(lista, elemento, indice=0):

    # Caso base
    if indice == len(lista):
        return 0

    # Caso recursivo
    if lista[indice] == elemento:
        return 1 + contar_elemento(lista, elemento, indice + 1)

    return contar_elemento(lista, elemento, indice + 1)


# PASO 5: SUMATORIA ITERATIVA

def sumatoria_iterativa(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Ingrese un numero entero no negativo")

    resultado = 0

    for numero in range(1, n + 1):
        resultado += numero

    return resultado


# SUMATORIA RECURSIVA

def sumatoria_recursiva(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Ingrese un numero entero no negativo")

    # Caso base
    if n == 0:
        return 0

    # Caso recursivo
    return n + sumatoria_recursiva(n - 1)



# PROGRAMA PRINCIPAL


print("===== PROYECTO DE RECURSIVIDAD =====")

# PRUEBAS DE FACTORIAL
print("\n1. FACTORIAL")

for numero in [3, 5, 6]:
    print("Factorial de", numero, "=", factorial(numero))


# PRUEBAS DE POTENCIA
print("\n2. POTENCIA")

for base, exponente in [(2, 3), (3, 2), (5, 2)]:
    print(base, "elevado a", exponente, "=", potencia(base, exponente))


# PRUEBA DE CONTEO EN LISTA
print("\n3. CONTEO EN UNA LISTA")

numeros = [2, 4, 2, 6, 2, 8]

print("Lista:", numeros)
print("El numero 2 aparece:", contar_elemento(numeros, 2), "veces")


# COMPARACION ITERATIVA Y RECURSIVA
print("\n4. COMPARACION DE SUMATORIA")

for numero in [3, 5, 7]:

    resultado_iterativo = sumatoria_iterativa(numero)
    resultado_recursivo = sumatoria_recursiva(numero)

    print("\nNumero:", numero)
    print("Resultado iterativo:", resultado_iterativo)
    print("Resultado recursivo:", resultado_recursivo)

print("\n===== FIN DEL PROGRAMA =====")
