""" PSIT Week 13
Wiput Pootong (60070090)
MultiplyMatrix
"""

def multiply(mat_a, mat_b, row, col):
    """ Multiply Matrix """
    row = [mat_a[row][j] for j in range(len(mat_a[0]))]
    col = [mat_b[i][col] for i in range(len(mat_b))]

    result = 0
    for i in range(len(row)):
        result += row[i] * col[i]

    return result

def main():
    """ Find sum of curcular prime """

    # Get row for matrix A
    row = int(input())
    # Get column for matrix A and row for Matrix B
    col = int(input())
    # Get column for matrix B
    col_b = int(input())

    # Create Matrix A
    matrix = [[float(input()) for _ in range(col)] for _ in range(row)]
    # Create Matrix B
    matrix_b = [[float(input()) for _ in range(col_b)] for _ in range(col)]

    # Create result list
    result = [[0 for _ in range(col_b)] for _ in range(row)]

    for row_count in range(row):
        for col_count in range(col_b):
            result[row_count][col_count] = multiply(matrix, matrix_b, row_count, col_count)

    # Print result
    for row in result:
        for col in row:
            print("%d " %col, end='')
        print()

main()
