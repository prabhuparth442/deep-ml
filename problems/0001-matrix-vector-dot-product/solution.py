def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	ans = []
	for row in a:
		sum = 0
		for i in range(len(row)):
			sum += row[i] * b[i]
		ans.append(sum)
		sum = 0
	return ans

