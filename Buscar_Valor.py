# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función que realiza la búsqueda de un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si el valor no se encuentra, retorna None

# Función para ingresar el valor a buscar con validación
def obtener_valor_buscado():
    while True:
        try:
            valor = int(input("Ingresa el valor que deseas buscar en la matriz: "))
            return valor
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Obtención del valor a buscar
valor_buscado = obtener_valor_buscado()

# Llamamos a la función y mostramos el resultado
resultado = buscar_valor(matriz, valor_buscado)

if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")