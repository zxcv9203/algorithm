now = [int(x) for x in input().split(':')]
st = [int(x) for x in input().split(':')]
if now[2] > st[2]:
	st[1] -= 1
	st[2] += 60
st[2] -= now[2]
if now[1] > st[1]:
	if st[0] == 0 :
		st[0] = 23
	else :
		st[0] -= 1
	st[1] += 60
st[1] -= now[1]
st[0] -= now[0]
if st[0] < 0:
	st[0] += 24
print("{0:02}:{1:02}:{2:02}".format(st[0], st[1], st[2]))