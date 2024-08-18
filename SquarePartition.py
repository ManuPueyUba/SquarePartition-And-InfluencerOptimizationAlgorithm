import sys
import time
import os

def paintMiddleWithoutIncludingSilo(silo, square, plantation):
    siloRow, siloColumn = silo
    middle = len(square) // 2

    if len(square) == 1:
        return square

    if plantation > 8:
        plantation = 1

    # if the silo is in the top left corner
    if siloRow < middle and siloColumn < middle:
        showSquare(square)
        square[middle - 1][middle] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)
        square[middle][middle - 1] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)
        square[middle][middle] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)

        silo1 = siloRow, siloColumn
        silo2 = (middle - 1, 0)
        silo3 = (0, middle - 1)
        silo4 = (0, 0)

    # if the silo is in the top right corner
    elif siloRow < middle and siloColumn >= middle:
        showSquare(square)
        square[middle - 1][middle - 1] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)
        square[middle][middle - 1] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)
        square[middle][middle] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)

        siloColumn -= middle

        silo1 = (middle - 1, middle - 1)
        silo2 = siloRow, siloColumn
        silo3 = (0, middle - 1)
        silo4 = (0, 0)

    # if the silo is in the bottom left corner
    elif siloRow >= middle and siloColumn < middle:
        showSquare(square)
        square[middle - 1][middle - 1] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)
        square[middle - 1][middle] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)
        square[middle][middle] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)

        siloRow -= middle

        silo1 = (middle - 1, middle - 1)
        silo2 = (middle - 1, 0)
        silo3 = siloRow, siloColumn
        silo4 = (0, 0)

    # if the silo is in the bottom right corner
    elif siloRow >= middle and siloColumn >= middle:
        showSquare(square)
        square[middle - 1][middle - 1] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)
        square[middle - 1][middle] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)
        square[middle][middle - 1] = plantation
        showSquare(square)  # Mostrar el estado actual del cuadrado
        time.sleep(0.2)

        siloRow -= middle
        siloColumn -= middle

        silo1 = (middle - 1, middle - 1)
        silo2 = (middle - 1, 0)
        silo3 = (0, middle - 1)
        silo4 = siloRow, siloColumn

    if len(square) == 2:
        return square
    else:
        square1, square2, square3, square4 = divideSquare(square)

    plantation += 1
    square1 = paintMiddleWithoutIncludingSilo(silo1, square1, plantation)
    plantation += 1
    square2 = paintMiddleWithoutIncludingSilo(silo2, square2, plantation)
    plantation += 1
    square3 = paintMiddleWithoutIncludingSilo(silo3, square3, plantation)
    plantation += 1
    square4 = paintMiddleWithoutIncludingSilo(silo4, square4, plantation)
    square = joinSquares(square1, square2, square3, square4)
    return square


def divideSquare(square):
    n = len(square)
    middle = n // 2

    square1 = [row[:middle] for row in square[:middle]]
    square2 = [row[middle:] for row in square[:middle]]
    square3 = [row[:middle] for row in square[middle:]]
    square4 = [row[middle:] for row in square[middle:]]

    return square1, square2, square3, square4


def joinSquares(square1, square2, square3, square4):
    n = len(square1)

    merged_matrix = []
    for i in range(n):
        row = square1[i] + square2[i]
        merged_matrix.append(row)

    for i in range(n):
        row = square3[i] + square4[i]
        merged_matrix.append(row)

    return merged_matrix


def createSquare(silo, squareSize):
    siloRow, siloColumn = silo
    square = []
    for i in range(squareSize):
        row = []
        for j in range(squareSize):
            row.append(1)
        square.append(row)
    square[siloRow][siloColumn] = 0
    return square

# Función para mostrar el cuadrado completo
def showSquare(square):
    clearConsole()
    printSquare(square)
    time.sleep(0.5)

# Función para imprimir la matriz en la consola con colores y caracteres
def printSquare(square):
    for row in square:
        for cell in row:
            if cell == 0:
                print("\033[1;31m" + "■", end=" ")  # Rojo para el silo
            elif cell == 1:
                print("\033[1;37m" + "■", end=" ")  # Gris para el campo sin pintar
            else:
                print("\033[1;32m" + "■", end=" ")  # Verde para el campo pintado
        print("\033[0m")  # Resetear el color

# Función para limpiar la consola
def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    try:
        squareSize = int(sys.argv[1])
        siloRow = int(sys.argv[2])
        siloColumn = int(sys.argv[3])
    except ValueError:
        print("Error: arguments must be integers.")
        return

    silo = (siloRow, siloColumn)
    square = createSquare(silo, squareSize)
    print("Cuadrado Inicial:")
    printSquare(square)
    time.sleep(1)  # Pausa antes de empezar a pintar
    square = paintMiddleWithoutIncludingSilo(silo, square, 2)  # Iniciar la plantación con el valor 2
    print("Cuadrado Final:")
    printSquare(square)

main()
