import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using the module NumPy
    Args:
        m_a: a list of lists containing ints/floats
        m_b: a list of lists containing ints/floats
    Returns:
        a new matrix containing the product of m_a and m_b
    Raises:
        TypeError: if m_a or m_b are not list of lists of ints/floats
        ValueError: if m_a or m_b are empty or have different shapes
    """
    # Check if m_a and m_b are valid matrices
    if not isinstance(m_a, list) or len(m_a) == 0 or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or len(m_b) == 0 or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Convert the matrices to numpy arrays and perform matrix multiplication
    a = np.array(m_a)
    b = np.array(m_b)
    c = np.matmul(a, b)

    # Return the result as a list of lists
    return c.tolist()
