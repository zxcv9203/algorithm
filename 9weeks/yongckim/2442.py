n = int(input())
i = 0
j = 1
while i < n:
	j = 1
	while j < n * 2:
		if i + n >= j and n - i <= j:
			print('*', end='')
		elif j < n:
			print(' ', end='')
		j += 1
	print()
	i += 1
