#Dependiendo del numero de "n" que haya, puede ser un 
#Algoritmo recursivo o iterativo
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