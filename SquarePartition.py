import sys

def paintMiddleWithoutIncludingSilo(silo, square, plantation):
    siloRow, siloColumn = silo
    middle = len(square) // 2

    if len(square) == 1:
        return square

    if plantation > 8:
        plantation = 1

    # if the silo is in the top left corner
    if siloRow < middle and siloColumn < middle:
        square[middle - 1][middle] = plantation
        square[middle][middle - 1] = plantation
        square[middle][middle] = plantation

        silo1 = siloRow, siloColumn
        silo2 = (middle - 1, 0)
        silo3 = (0, middle - 1)
        silo4 = (0, 0)

    # if the silo is in the top right corner
    elif siloRow < middle and siloColumn >= middle:
        square[middle - 1][middle - 1] = plantation
        square[middle][middle - 1] = plantation
        square[middle][middle] = plantation
        siloColumn -= middle

        silo1 = (middle - 1, middle - 1)
        silo2 = siloRow, siloColumn
        silo3 = (0, middle - 1)
        silo4 = (0, 0)

    # if the silo is in the bottom left corner
    elif siloRow >= middle and siloColumn < middle:
        square[middle - 1][middle - 1] = plantation
        square[middle - 1][middle] = plantation
        square[middle][middle] = plantation

        siloRow -= middle

        silo1 = (middle - 1, middle - 1)
        silo2 = (middle - 1, 0)
        silo3 = siloRow, siloColumn
        silo4 = (0, 0)

    # if the silo is in the bottom right corner
    elif siloRow >= middle and siloColumn >= middle:
        square[middle - 1][middle - 1] = plantation
        square[middle - 1][middle] = plantation
        square[middle][middle - 1] = plantation

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


# Square with lists
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
    for row in square:
        print(row)
    square = paintMiddleWithoutIncludingSilo(silo, square, 1)
    print("Final Square:")
    for row in square:
        print(row)
    return square


main()
