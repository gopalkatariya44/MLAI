bord = [[3, 0, 0, 8, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 4, 1, 5, 0, 0, 8, 3, 0],
        [0, 2, 0, 0, 0, 1, 0, 0, 0],
        [8, 5, 0, 4, 0, 3, 0, 1, 7],
        [0, 0, 0, 7, 0, 0, 0, 2, 0],
        [0, 8, 5, 0, 0, 9, 7, 4, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 7, 0, 0, 6]]

grid_size = 9

print("hey there")


def isNumberInRow(bord, number, row):
    for i in range(grid_size):
        if bord[row][i] == number:
            return True
        return False


def isNumberInColumn(bord, number, column):
    for i in range(grid_size):
        if bord[i][column] == number:
            return True
        return False


def isNumberInBox(bord, number, row, column):
    local_box_row = row - row % 3
    local_box_column = column - column % 3

    for local_box_row in range(local_box_row + 3):
        for local_box_column in range(local_box_column + 3):
            if bord[local_box_row][local_box_column] == number:
                return True
        return False


def isValidPlacement(bord, number, row, column):
    a = isNumberInRow(bord, number, row)
    b = isNumberInColumn(bord, number, column)
    c = isNumberInBox(bord, number, row, column)
    return (not a) and (not b) and (not c)
    # return isNumberInRow(bord, number, row) and isNumberInColumn(bord, number, column) and isNumberInBox(bord, number,
    #                                                                                                      row, column)


def solveBord(bord):
    for row in range(grid_size):
        for column in range(grid_size):
            if bord[row][column] == 0:
                for numberToTry in range(grid_size):
                    if isValidPlacement(bord, numberToTry, row, column):
                        bord[row][column] = numberToTry
                        if solveBord(bord):
                            return True
                        else:
                            bord[row][column] = 0
                return False
        return True


# def main():
for i in range(grid_size):
    for j in range(grid_size):
        print(bord[i][j], end=" ")
    print()


# if __name__ == '__main__':
#     main()
