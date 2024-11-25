def scalar_product(vector1, vector2):
    """
    Calculate the scalar product of two vectors.

    Args:
    vector1 (list of float): The first vector.
    vector2 (list of float): The second vector.

    Returns:
    float: The scalar product of the two vectors.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")

    return sum(x * y for x, y in zip(vector1, vector2))

    def matrix_product(matrix1, matrix2):
        """
        Calculate the matrix product of two matrices.

        Args:
        matrix1 (list of list of float): The first matrix.
        matrix2 (list of list of float): The second matrix.

        Returns:
        list of list of float: The matrix product of the two matrices.
        """
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

        result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result