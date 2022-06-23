import numpy as np
# Generate some random data
data = np.random.randn(3, 3)
print(data)

np.savetxt('exec4.txt', data)
