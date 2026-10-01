import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	arr = np.array(matrix)
	if mode == "row":
		means= arr.mean(axis=1)
	else:
		means=arr.mean(axis =0)
	
	return means.tolist()