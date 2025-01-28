import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 400)
y1 =2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

plt.plot (x, y1, label='y =2x + 1', color='blue', linestyle='-', linewidth=2)
plt.plot (x, y2, label='y =2x + 1', color='green', linestyle='-', linewidth=2)
plt.plot (x, y3, label='y =2x + 2', color='red', linestyle='-', linewidth=2)

plt.title('Graphs of y = 2x + 1, y = 2x + 2, y= 2x + 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.grid(True)
