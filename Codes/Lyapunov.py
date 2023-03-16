# Load libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters

R = np.linspace(1, 4, 20000) # X axis
LE = [] # Y axis
result = []

# Generate x for each value of r
# Logistic map: x = rx(1-x)

for r in R:
    x = np.random.random()
    for n in range(100):
        x = r*x*(1-x)
    result = []
    # 100s of iteration
    for n in range(100):
        x = r*x*(1-x)
        result.append(np.log(abs(r-2*r*x)))

    LE.append(np.mean(result))

# Plot
plt.title('Lyapunov graph for Logistic map')
plt.ylabel('LE')
plt.xlabel('r')
plt.grid('on')
plt.plot(R, LE)
plt.show()
