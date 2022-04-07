import numpy as np
import matplotlib.pyplot as plt

x = np.random.beta(5, 1, (100, 1))

plt.plot(x)
plt.show()