#!/usr/bin/python
#author = "raviteja buddi"
import KSA
import PRGA
import plot
keysizes = []
sizelist=[]
f = open('Keys.txt','r')
for lin in f:
	KSA.fileks(lin)
	ab = KSA.fileks(lin)
	print(ab)
	PRGA.random(ab)
	keysizes.append(lin)
	

for i in range(0, len(keysizes)):
 noofbytes = (len(keysizes[i]) -1) * 8
 sizelist.append(noofbytes)
 print (str(noofbytes) + " bits")
 PRGA.printtime(i)	
 print ("---------------------------------------------"	)

t = PRGA.getTime()
#for i in range(0, len(t)-1):
#	print (str(sizelist[i]) + str(t[i]) )

plot.plotgraph(sizelist, t)

