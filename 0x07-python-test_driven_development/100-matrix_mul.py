def matrix_mul(m_a, m_b):
    """Multiply two matrices"""
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else "m_b must be a list")
    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" if not all(isinstance(row, list) for row in m_a) else "m_b must be a list of lists")
    # Check if m_a and m_b are not empty
    if len(m_a) == 0 or len(m_b) == 0 or len(m_a[0]) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_a can't be empty" if len(m_a) == 0 or len(m_a[0]) == 0 else "m_b can't be empty")
    # Check if m_a and m_b contain only integers or floats
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) or not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a should contain only integers or floats" if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) else "m_b should contain only integers or floats")
    # Check if m_a and m_b are rectangles
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" if not all(len(row) == len(m_a[0]) for row in m_a) else "each row of m_b must be of the same size")
    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    # Initialize C with zeros
    C = []
    for i in range(len(m_a)):
        C.append([0] * len(m_b[0]))
    # Compute the dot product of each row and column
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            C[i][j] = sum(a * b for a, b in zip(m_a[i], [row[j] for row in m_b]))
    # Return C
    return C
