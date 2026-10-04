import math

def sigmoid(z: float) -> float:
	result = 1.0/(1 + math.exp(-z))
	return result