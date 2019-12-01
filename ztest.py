import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0, 10, 25, 40, 40, 50, 60, 70, 80, 140]

plt.xlabel('Просто X')
plt.ylabel('Просто Y')
plt.title('Посто график')
plt.xticks([0, 2, 4, 6, 8, 10], [1, 2, 3, 4, 5])

plt.plot(x, y)
plt.show()
