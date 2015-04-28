#!/usr/bin/python
#author = "raviteja buddi"
import KSA
import PRGA
keysizes = []
f = open('Keys.txt','r')
for lin in f:
	KSA.fileks(lin)
	ab = KSA.fileks(lin)
	print(ab)
	PRGA.random(ab)
	keysizes.append(lin)
	

for i in range(0, len(keysizes)-1):
 noofbytes = (len(keysizes[i]) -1) * 8
 print (str(noofbytes) + " bits")
 PRGA.printtime(i)	
 print ("---------------------------------------------"	)
