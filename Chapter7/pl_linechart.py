import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1, 2, 3], [3, 2, 1])
# plt.show()

# height = [161, 170, 182, 175, 173, 165]
# weight = [50, 58, 80, 70, 69, 55]
#
# plt.scatter(height, weight, alpha=0.7)
# plt.xlabel('height')
# plt.ylabel('weight')
# plt.title("scatter demo")
# plt.show()


np.random.seed(10)
N = 100
x = np.random.rand(N)
y1 = np.random.rand(N)
plt.scatter(x, y1)
plt.show()
