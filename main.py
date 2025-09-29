def sarrus_iterative(matrix):
    """
    Calcula el determinante de una matriz 3x3 usando la regla de Sarrus (iterativo).
    """
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("La matriz debe ser de 3x3")
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    det = (
        a * e * i +
        b * f * g +
        c * d * h -
        c * e * g -
        b * d * i -
        a * f * h
    )
    return det

def sarrus_recursive(matrix):
    """
    Calcula el determinante de una matriz 3x3 de forma recursiva (expansión por cofactores).
    """
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("La matriz debe ser de 3x3")
    
    def determinant_2x2(m):
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    
    det = 0
    for col in range(3):
        minor = [
            [matrix[1][(col+1)%3], matrix[1][(col+2)%3]],
            [matrix[2][(col+1)%3], matrix[2][(col+2)%3]]
        ]
        det += matrix[0][col] * ((-1)**col) * determinant_2x2(minor)
    return det

# Ejemplo de uso:
if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Iterativo:", sarrus_iterative(matriz))
    print("Recursivo:", sarrus_recursive(matriz))