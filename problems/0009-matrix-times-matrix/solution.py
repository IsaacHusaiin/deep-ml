def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:
	if len(a[0]) != len(b):
		return -1

	result =[]
	for i in range(len(a)):
		row =[]
		for j in range(len(b[0])):
			total =0 

			for x in range (len(b)):
				total += a[i][x]* b[x][j]
			row.append(total)
		result.append(row)
	return result
	