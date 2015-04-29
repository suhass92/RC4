#!/usr/bin/env python
import matplotlib.pyplot as plt
#import numpy as npt
def plotgraph(x, y):

	plt.plot(x, y)
	plt.title("Key size vs Time taken graph")
	plt.xlabel("Key Sizes(Bits)")
	plt.ylabel("Time(s)")
	plt.show()


