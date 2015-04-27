#!/usr/bin/python
#author = "raviteja buddi"
def fileks(lin):
	key = []
	b = 0
	for i in lin:
		a = bin(ord(i))[2:].zfill(8)
		b = str(b) + str(a)
	z = b[1:]

	for c in z:
		key.append(c)
	d = key
	e = len(d)
	s = []
	for i in range(0,256):
		s.append(i)
	j = 0
	for i in range(0,256):
		j = (j + s[i] + int(d[i % e])) % 256
		s[i],s[j] = s[j], s[i]
	return s