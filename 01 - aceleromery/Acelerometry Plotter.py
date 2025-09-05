import numpy as np
import matplotlib.pyplot as plt 

data = np.genfromtxt("outputdata.txt", delimiter=',')
number_iterations = data.shape[0]


iterations = np.ones((number_iterations))
for i in range(1, number_iterations):
    iterations[i] = i+1
iterations = iterations.astype('int32')

plt.plot(iterations, data)
plt.show()