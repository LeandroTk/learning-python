def conta_digito(d, n):
	num = 0
	while n >= 10:
		aux_n = n % 10

		if d == aux_n:
			num += 1

		n = n // 10

	if d == n:
		num += 1

	return num

print(conta_digito(3, 5335))
print(conta_digito(2, 5335))

