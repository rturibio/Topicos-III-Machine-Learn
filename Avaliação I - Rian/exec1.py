
import pandas as pd
import numpy as np
import math 

v1 = np.array([2,2])

v2 = np.array([0,2])

mult = np.dot(v1, v2)
print(mult)

magnitude = np.linalg.norm(v1)
magnitude2 = np.linalg.norm(v2)

print(magnitude)
print(magnitude2)

resMag = magnitude * magnitude2

print(resMag)

print(mult/resMag)

angleInDegree = math.degrees(math.acos(mult/resMag))
print("θ =",angleInDegree,"°")
