import sys

def pintarMedioSinIncluirSilo(silo, cuadrado, plantacion):
    siloFila, siloColumna = silo
    medio = len(cuadrado) // 2

    if len(cuadrado) == 1:
        return cuadrado

    if plantacion > 8:
        plantacion = 1

    # si el silo esta en la esquina superior izquierda
    if siloFila < medio and siloColumna < medio:
        # Horizontal = x
        # Vertical = y
        cuadrado[medio - 1][medio] = plantacion
        cuadrado[medio][medio - 1] = plantacion
        cuadrado[medio][medio] = plantacion

        silo1 = siloFila, siloColumna
        silo2 = (medio - 1, 0)
        silo3 = (0, medio - 1)
        silo4 = (0, 0)

    # si el silo esta en la esquina superior derecha
    elif siloFila < medio and siloColumna >= medio:
        cuadrado[medio - 1][medio - 1] = plantacion
        cuadrado[medio][medio - 1] = plantacion
        cuadrado[medio][medio] = plantacion
        siloColumna -= medio

        silo1 = (medio - 1, medio - 1)
        silo2 = siloFila, siloColumna
        silo3 = (0, medio - 1)
        silo4 = (0, 0)

    # si el silo esta en la esquina inferior izquierda
    elif siloFila >= medio and siloColumna < medio:
        cuadrado[medio - 1][medio - 1] = plantacion
        cuadrado[medio - 1][medio] = plantacion
        cuadrado[medio][medio] = plantacion

        siloFila -= medio

        silo1 = (medio - 1, medio - 1)
        silo2 = (medio - 1, 0)
        silo3 = siloFila, siloColumna
        silo4 = (0, 0)

    # si el silo esta en la esquina inferior derecha
    elif siloFila >= medio and siloColumna >= medio:
        cuadrado[medio - 1][medio - 1] = plantacion
        cuadrado[medio - 1][medio] = plantacion
        cuadrado[medio][medio - 1] = plantacion

        siloFila -= medio
        siloColumna -= medio

        silo1 = (medio - 1, medio - 1)
        silo2 = (medio - 1, 0)
        silo3 = (0, medio - 1)
        silo4 = siloFila, siloColumna

    if len(cuadrado) == 2:
        return cuadrado
    else:
        cuadrado1, cuadrado2, cuadrado3, cuadrado4 = dividirCuadrado(cuadrado)

    plantacion += 1
    cuadrado1 = pintarMedioSinIncluirSilo(silo1, cuadrado1, plantacion)
    plantacion += 1
    cuadrado2 = pintarMedioSinIncluirSilo(silo2, cuadrado2, plantacion)
    plantacion += 1
    cuadrado3 = pintarMedioSinIncluirSilo(silo3, cuadrado3, plantacion)
    plantacion += 1
    cuadrado4 = pintarMedioSinIncluirSilo(silo4, cuadrado4, plantacion)
    cuadrado = unirCuadrados(cuadrado1, cuadrado2, cuadrado3, cuadrado4)
    return cuadrado


def dividirCuadrado(cuadrado):
    n = len(cuadrado)
    medio = n // 2

    cuadrado1 = [fila[:medio] for fila in cuadrado[:medio]]
    cuadrado2 = [fila[medio:] for fila in cuadrado[:medio]]
    cuadrado3 = [fila[:medio] for fila in cuadrado[medio:]]
    cuadrado4 = [fila[medio:] for fila in cuadrado[medio:]]

    return cuadrado1, cuadrado2, cuadrado3, cuadrado4


def unirCuadrados(cuadrado1, cuadrado2, cuadrado3, cuadrado4):
    n = len(cuadrado1)

    matriz_unida = []
    for i in range(n):
        fila = cuadrado1[i] + cuadrado2[i]
        matriz_unida.append(fila)

    for i in range(n):
        fila = cuadrado3[i] + cuadrado4[i]
        matriz_unida.append(fila)

    return matriz_unida


# Cuadrado con listas
def crearCuadrado(silo, tamanioCuadrado):
    siloFila, siloColumna = silo
    cuadrado = []
    for i in range(tamanioCuadrado):
        fila = []
        for j in range(tamanioCuadrado):
            fila.append(1)
        cuadrado.append(fila)
    cuadrado[siloFila][siloColumna] = 0
    return cuadrado


def main():
    try:
        tamanioCuadrado = int(sys.argv[1])
        siloFila = int(sys.argv[2])
        siloColumna = int(sys.argv[3])
    except ValueError:
        print("Error: los argumentos deben ser enteros.")
        return

    silo = (siloFila, siloColumna)
    cuadrado = crearCuadrado(silo, tamanioCuadrado)
    for fila in cuadrado:
        print(fila)
    cuadrado = pintarMedioSinIncluirSilo(silo, cuadrado, 1)
    print("Cuadrado Final:")
    for fila in cuadrado:
        print(fila)
    return cuadrado


main()