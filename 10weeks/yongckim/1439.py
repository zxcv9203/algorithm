coin = input()
zero = 0
one = 0
front = ''
for i in coin :
	if i == '0' and front != i:
		front = i
		zero += 1
	if i == '1' and front != i:
		front = i
		one += 1
print(min(zero, one))