import matplotlib.pyplot as plt
import numpy as np

alist = [i**2 for i in range(10)]
blist = [1/(i+1e-4) for i in range(10)]

arr = np.array(alist)
barr = np.array(blist)

plt.plot(arr)
plt.plot(barr)

plt.show()