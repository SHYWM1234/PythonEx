import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 200)
f1 = np.power(10, x)
f2 = np.power(np.e, x)
f3 = np.power(2, x)

plt.plot(x, f1, 'r', x, f2, 'b', x, f3, 'g', linewidth = 2)
plt.axis([-4, 4, -0.5, 8])
plt.text(1, 7.5, r'$10^x$', fontsize = 16)
plt.text(2.2, 7.5, r'$e^x$', fontsize = 16)
plt.text(3.2, 7.5, r'$2^x$', fontsize = 16)

plt.show()
