import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    ATA = np.matmul(A.T, A)
    
    a, b, d = ATA[0][0], ATA[0][1], ATA[1][1]
    
    theta = 0.5*np.arctan2(2*b,(a-d))
    c, s = np.cos(theta), np.sin(theta)

    J = np.array([[c, -s],[s, c]])
    D = J.T @ ATA @ J
    
    V = J

    S = np.sqrt(np.maximum(np.diag(D), 0))
    
    u1 = A @ V[:, 0] / S[0]
    u2 = A @ V[:, 1] / S[1]

    U = np.column_stack((u1, u2))

    return U, S, V.T

