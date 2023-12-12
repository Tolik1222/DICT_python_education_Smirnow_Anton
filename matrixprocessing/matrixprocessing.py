"""implement various operations with matrices, including addition, multiplication, finding the determinant and working with inverse matrices."""


def read_matrix_size():
    rows, cols = map(int, input("Enter matrix size: > ").split())
    return rows, cols


def read_matrix(rows, cols):
    print("Enter matrix:")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix


def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return None  # Error, unable to add matrices
    result = []
    for i in range(len(matrix_a)):
        result.append([a + b for a, b in zip(matrix_a[i], matrix_b[i])])
    return result


def multiply_matrix_by_constant(matrix, constant):
    result = []
    for row in matrix:
        result.append([element * constant for element in row])
    return result


def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return None  # Error, cannot multiply matrices
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            element = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
            row.append(element)
        result.append(row)
    return result


def transpose_matrix(matrix, transpose_type):
    if transpose_type == 1:  # Main diagonal
        return [list(row) for row in zip(*matrix)]
    elif transpose_type == 2:  # Side diagonal
        return [row[::-1] for row in matrix[::-1]]
    elif transpose_type == 3:  # Vertical line
        return [row[::-1] for row in matrix]
    elif transpose_type == 4:  # Horizontal line
        return matrix[::-1]
    else:
        return None  # Wrong choice


def calculate_determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None  # The determinant can be calculated only for square matrices
    n = len(matrix)

    # Base case for a 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for i in range(n):
        submatrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        sign = 1 if i % 2 == 0 else -1
        determinant += sign * matrix[0][i] * calculate_determinant(submatrix)

    return determinant


def inverse_matrix(matrix):
    determinant = calculate_determinant(matrix)
    if determinant == 0:
        return None  # The matrix does not have an inverse
    n = len(matrix)

    # Calculation of algebraic auxiliaries (auxiliary matrices)
    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            cofactor_row.append(((-1) ** (i + j)) * calculate_determinant(minor))
        cofactors.append(cofactor_row)

    # Transposition of the auxiliary matrix and division by the determinant
    inverse = [[round(cofactors[j][i] / determinant, 2) for i in range(n)] for j in range(n)]
    return inverse


def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        print(*row)


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

    choice = input("Your choice: > ")

    if choice == '0':
        break
    elif choice == '1':
        rows_a, cols_a = read_matrix_size()
        matrix_a = read_matrix(rows_a, cols_a)

        rows_b, cols_b = read_matrix_size()
        matrix_b = read_matrix(rows_b, cols_b)

        result = add_matrices(matrix_a, matrix_b)
        if result is not None:
            print_matrix(result)
        else:
            print("Matrices cannot be added. Please ensure they have the same dimensions.")
    elif choice == '2':
        rows, cols = read_matrix_size()
        matrix = read_matrix(rows, cols)
        constant = float(input("Enter constant: > "))
        result = multiply_matrix_by_constant(matrix, constant)
        print_matrix(result)
    elif choice == '3':
        rows_a, cols_a = read_matrix_size()
        matrix_a = read_matrix(rows_a, cols_a)

        rows_b, cols_b = read_matrix_size()
        matrix_b = read_matrix(rows_b, cols_b)

        result = multiply_matrices(matrix_a, matrix_b)
        if result is not None:
            print_matrix(result)
        else:
            print(
                "Matrices cannot be multiplied. Please ensure the number of columns in the first matrix is equal to the number of rows in the second matrix.")
    elif choice == '4':
        transpose_type = int(
            input("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice: > "))
        rows, cols = read_matrix_size()
        matrix = read_matrix(rows, cols)
        transposed_matrix = transpose_matrix(matrix, transpose_type)
        if transposed_matrix is not None:
            print_matrix(transposed_matrix)
        else:
            print("Invalid transpose type.")
    elif choice == '5':
        rows, cols = read_matrix_size()
        matrix = read_matrix(rows, cols)
        determinant = calculate_determinant(matrix)
        if determinant is not None:
            print("The result is:")
            print(determinant)
        else:
            print("The determinant can only be calculated for square matrices.")
    elif choice == '6':
        rows, cols = read_matrix_size()
        matrix = read_matrix(rows, cols)
        inverse = inverse_matrix(matrix)
        if inverse is not None:
            print_matrix(inverse)
        else:
            print("This matrix doesn't have an inverse.")
    else:
        print("Invalid choice. Please enter a valid option.")
