def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	(a, b), (c, d) = matrix

	trace = a +d 
	det = a*d-b*c

	eigenvalues_positive = (trace + (trace**2 - 4*det)**0.5) / 2 
	eigenvalues_negative = (trace - (trace**2 - 4*det)**0.5) / 2 
	return [eigenvalues_positive,eigenvalues_negative]