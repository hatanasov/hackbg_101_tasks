#!/usr/bin/env python3.6

def create_matrix():
    matrix = []
    while True:
        user_input = input()
        if user_input == '':
            break
        row = []
        for colour in user_input:
            row.append(colour)
        matrix.append(row)
    return matrix


def connected_colours(matrix):
    row_len = len(matrix)
    column_len = len(matrix[0])
    counter = 0
    for row, row_list in enumerate(matrix):
        for column, colour in enumerate(row_list):
            if colour != 'Checked':
                get_whole_group(colour, row, column, row_len, column_len, matrix)
                counter += 1
    return counter


def get_whole_group(colour, row, column, row_len, column_len, matrix):
    neighbours = []
    for r in range(0, row_len):
        for c in range(0, column_len):
            if matrix[r][c] != 'Checked':
                current_colour = matrix[r][c]
                if colour == current_colour and r in range(row - 1, row + 2) and c in range(column - 1, column + 2):
                    neighbours.append((r, c))
                    matrix[r][c] = 'Checked'
    for neighbour in neighbours:
        row = neighbour[0]
        column = neighbour[1]
        get_whole_group(colour, row, column, row_len, column_len, matrix)


matrix = create_matrix()
clicks = connected_colours(matrix)
print(clicks)
