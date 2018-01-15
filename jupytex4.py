from matplotlib import pyplot as plt
import numpy

x = numpy.arange(0, 10, 0.1)
y = numpy.cos(x)
plt.plot(x,y)
plt.show()
