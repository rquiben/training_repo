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


    def vector_product(vector1, vector2):
        """
        Calculate the vector product (cross product) of two 3-dimensional vectors.

        Args:
        vector1 (list of float): The first vector.
        vector2 (list of float): The second vector.

        Returns:
        list of float: The vector product of the two vectors.
        """
        if len(vector1) != 3 or len(vector2) != 3:
            raise ValueError("Both vectors must be 3-dimensional")

        return [
            vector1[1] * vector2[2] - vector1[2] * vector2[1],
            vector1[2] * vector2[0] - vector1[0] * vector2[2],
            vector1[0] * vector2[1] - vector1[1] * vector2[0]
        ]