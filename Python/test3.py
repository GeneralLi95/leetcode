import numpy as np


x = np.linspace(1,10,10)
print("right",  x[1:])
print("left ", x[:-1])

x_mid = (x[:-1] + x[1:])/2

print(x_mid)


print(2**5)
print(np.power(2,5))


print(np.ceil(0.2))