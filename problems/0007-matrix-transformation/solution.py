import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A = np.array(A, dtype=float)
    T = np.array(T, dtype=float)
    S = np.array(S, dtype=float)

    if abs(np.linalg.det(T)) < 1e-12 or abs(np.linalg.det(S)) < 1e-12:
        return -1                          

    return (np.linalg.inv(T) @ A @ S).tolist()  