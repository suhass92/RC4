#!/usr/bin/python
#author = "raviteja buddi"
import KSA
import PRGA
f = open('Keys.txt','r')
for lin in f:
	KSA.fileks(lin)
	ab = KSA.fileks(lin)
	print(ab)
	PRGA.random(ab)
