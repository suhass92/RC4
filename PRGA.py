#!/usr/bin/python
#author = "raviteja buddi"
import time
start_time = time.clock()
def random(ab):
	f = "This is my plaintext"
	g = len(f)
	i = 0
	j = 0
	y = 0
	k = []
	while int(g) > 0:
		i = (i + 1) % 256
		j = (j + ab[i]) % 256
		ab[i], ab[j] = ab[j], ab[i]
		p = ab[(ab[i] + ab[j]) % 256]
		k.append(p)
		g-=1
	print("---%s seconds ---" % (time.clock() - start_time))
	m = len(k)
	for h in range(0,m):
		x = bin(k[h])[2:].zfill(8)
		y = str(y) + str(x)
	n = y[1:]
	print('The key stream is :\n')
	print(n)