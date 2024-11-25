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