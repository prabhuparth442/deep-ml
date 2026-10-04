import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    U, S, V = np.linalg.svd(A, full_matrices = False)
    return (U, S,V)