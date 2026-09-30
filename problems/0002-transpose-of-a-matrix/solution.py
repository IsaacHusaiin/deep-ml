def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """

    m = len(a)
    n= len(a[0])
    result =[]

    for j in range(n):
        new_row =[]
        for i in range(m):
            new_row.append(a[i][j])
        result.append(new_row)
    return result
    # Your code here
    pass