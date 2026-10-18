import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	size = len(b)
	x = np.zeros(size)

	for _ in range(n):
		x_new = np.zeros(size)
		for i in range(size):
			total =0.0
			for j in range(size):
				if j!= i:
					total += A[i][j] * x[j]
			x_new[i] = (b[i]-total)/A[i][i]
		x=x_new

	return np.round(x, 4).tolist()