"""Escribir una función que calcule el máximo común divisor de dos números y otra
que calcule el mínimo común múltiplo."""

def maximoComunDivisor(x,y):
	if x < y:
		return maximoComunDivisor(y, x)

	while y != 0:
		x = y
		y = x % y

	return x

def minimoComunMultiplo(x,y):
	return (x* y) / maximoComunDivisor(x, y)

print(maximoComunDivisor(2,3))
print(maximoComunDivisor(12,3))
print(minimoComunMultiplo(2,24))
print(minimoComunMultiplo(24,12))
