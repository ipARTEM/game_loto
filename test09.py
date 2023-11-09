import numpy as np
import matplotlib.pyplot as plt

ts=np.arange(10)

print(ts)
print(type(ts))


plt.plot([1, 2, -6, 0, 4])
# plt.show()
var=[]
# var = [34, 67, 8. 9, 12, 56, 89, "привет", 5.8]

print(type(var))
#
# import numpy as np
# my_array = np.array(57, 322, 57, 11, 77)

er= np.arange(-10, 10, 0.1)
# print(er)

a=np.linspace(5, 8, 100)
# print(a)

my_array = np.random.randint(-5, 5, (4, 4))

# print(my_array[:2])

# import numpy as np
# my_array = np.array(57, 322, 57, 11, 77)

print(my_array.max())
