def conta_repeticao(n, m):
	list_of_n_digits = []
	list_of_m_digits = []

	while n > 0:
		list_of_n_digits.append(n % 10)
		n = n // 10

	while m > 0:
		list_of_m_digits.append(m % 10)
		m = m // 10

	list_of_n_digits.sort()
	list_of_m_digits.sort()

	number_of_digits = len(list_of_n_digits)
	repetion_number = 0

	for n_digit, m_digit in zip(list_of_n_digits, list_of_m_digits):
		if n_digit == m_digit:
			repetion_number += 1

	return repetion_number

print(conta_repeticao(3553, 5335))
print(conta_repeticao(3535, 5335))
print(conta_repeticao(5335, 5335))
print(conta_repeticao(3335, 5335))