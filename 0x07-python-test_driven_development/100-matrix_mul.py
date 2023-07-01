#!/usr/bin/python3
# 100-matrix_mul.py
"""Function defines  matrix multiplications."""


def matrix_mul(m_a, m_b):

    """Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(therow, list) for therow in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(therow, list) for therow in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(dig, int) or isinstance(dig, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(dig, int) or isinstance(dig, float))
               for dig in [num for therow in m_b for num in therow]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(therow) == len(m_a[0]) for therow in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(therow) == len(m_b[0]) for therow in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_invert_b = []
    for j in range(len(m_b[0])):
        new_row = []
        for k in range(len(m_b)):
            new_row.append(m_b[k][j])
        new_invert_b.append(new_row)

    the_new_mat = []
    for therow in m_a:
        new_row = []
        for thecol in new_invert_b:
            prod = 0
            for a in range(len(new_invert_b[0])):
                prod += therow[a] * thecol[a]
            new_row.append(prod)
        the_new_mat.append(new_row)

    return the_new_mat
