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



