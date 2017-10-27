import numpy as np
import matplotlib.pyplot as plt

data = [3, 5, 6, 2, 9, 3, 7, 5, 7, 3, 8]

print 'Mean:', np.mean(data)
print 'Standard Deviation:', np.std(data)
plt.hist(data)
plt.show()