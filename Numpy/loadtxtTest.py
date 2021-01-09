import numpy as np
print("start".center(50, "="))
try:
    arr = np.loadtxt("temp.txt", skiprows = 1)
except:
    print("fileNotFoundException")
else:
    print(arr.ndim)
    print(arr.size)
    print(arr.shape)
    print(arr.dtype)
print("end".center(50, "="))