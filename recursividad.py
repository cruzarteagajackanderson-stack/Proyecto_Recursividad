
# SISTEMA DE ANALISIS DE ENTREGAS DIGITALES

# 1. REGISTRO DE OCHO ENTREGAS SIMULADAS

entregas = [
    {"codigo": "EST001", "archivo": "trabajo_final.pdf", "intentos": 2, "puntaje": 18, "observaciones": "Entrega completa"},
    {"codigo": "EST002", "archivo": "tarea_v2.docx", "intentos": 1, "puntaje": 16, "observaciones": "Entrega correcta"},
    {"codigo": "EST003", "archivo": "proyecto_final.pdf", "intentos": 3, "puntaje": 20, "observaciones": "Buen trabajo"},
    {"codigo": "EST004", "archivo": "actividad.docx", "intentos": 1, "puntaje": 15, "observaciones": "Entrega incompleta"},
    {"codigo": "EST005", "archivo": "informe_v2.pdf", "intentos": 2, "puntaje": 17, "observaciones": "Entrega corregida"},
    {"codigo": "EST006", "archivo": "practica_final.docx", "intentos": 1, "puntaje": 19, "observaciones": "Entrega completa"},
    {"codigo": "EST007", "archivo": "ejercicio.pdf", "intentos": 2, "puntaje": 14, "observaciones": "Falta informacion"},
    {"codigo": "EST008", "archivo": "entrega_final.pdf", "intentos": 1, "puntaje": 18, "observaciones": "Entrega correcta"}
]


# 2. SUMATORIA RECURSIVA DE PUNTAJES

def sumar_puntajes_recursivo(lista, indice=0):
    if indice == len(lista):
        return 0

    return lista[indice]["puntaje"] + sumar_puntajes_recursivo(lista, indice + 1)


# 3. SUMATORIA ITERATIVA DE PUNTAJES

def sumar_puntajes_iterativo(lista):
    total = 0

    for entrega in lista:
        total += entrega["puntaje"]

    return total


# 4. BUSQUEDA RECURSIVA DE CODIGO DE ESTUDIANTE

def buscar_codigo_recursivo(lista, codigo, indice=0):
    if not isinstance(codigo, str) or not codigo.strip():
        raise ValueError("El codigo de busqueda no puede estar vacio")

    if indice == len(lista):
        return None

    if lista[indice]["codigo"] == codigo:
        return lista[indice]

    return buscar_codigo_recursivo(lista, codigo, indice + 1)


# 5. CONTEO RECURSIVO DE ARCHIVOS POR PALABRA CLAVE

def contar_archivos_recursivo(lista, palabra, indice=0):
    if not isinstance(palabra, str) or not palabra.strip():
        raise ValueError("La palabra clave no puede estar vacia")

    if indice == len(lista):
        return 0

    archivo = lista[indice]["archivo"].lower()

    if palabra.lower() in archivo:
        return 1 + contar_archivos_recursivo(lista, palabra, indice + 1)

    return contar_archivos_recursivo(lista, palabra, indice + 1)


# 6. FUNCION RECURSIVA ADICIONAL: FACTORIAL

def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Ingrese un entero no negativo")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# 7. EJECUCION DEL PROGRAMA

if __name__ == "__main__":

    print("SISTEMA DE ANALISIS DE ENTREGAS DIGITALES")
    print("-----------------------------------------")

    print("\nLISTA DE ENTREGAS:")
    for entrega in entregas:
        print(entrega)

    print("\nSUMATORIA DE PUNTAJES:")
    print("Resultado recursivo:", sumar_puntajes_recursivo(entregas))
    print("Resultado iterativo:", sumar_puntajes_iterativo(entregas))

    print("\nBUSQUEDA DE ESTUDIANTES:")
    print("EST004:", buscar_codigo_recursivo(entregas, "EST004"))
    print("EST099:", buscar_codigo_recursivo(entregas, "EST099"))

    print("\nCONTEO DE ARCHIVOS:")
    print("Archivos con 'final':", contar_archivos_recursivo(entregas, "final"))
    print("Archivos con 'v2':", contar_archivos_recursivo(entregas, "v2"))

    print("\nFACTORIAL:")
    print("Factorial de 5:", factorial(5))

    print("\nPRUEBAS DE VALIDACION:")

    try:
        factorial(-3)
    except ValueError as error:
        print("Factorial negativo:", error)

    try:
        contar_archivos_recursivo(entregas, "")
    except ValueError as error:
        print("Palabra clave vacia:", error)

    try:
        buscar_codigo_recursivo(entregas, "")
    except ValueError as error:
        print("Codigo vacio:", error)

    print("\nPRUEBAS ADICIONALES:")
    print("Lista vacia:", sumar_puntajes_recursivo([]))
    print("Factorial de 0:", factorial(0))
