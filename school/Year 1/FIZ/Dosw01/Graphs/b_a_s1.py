import matplotlib.pyplot as plt
import numpy as np
a = np.array([
5.5,
5.5,
5.5,
5.5,
5.5,
94.5,
89.0,
84.0,
79.0,
74.5,
])

b = np.array([
94.5,
89.5,   
84.5,
79.5,
74.5,
5.5,
6.0,
6.0,
6.0,
5.5,
])

delta = 0.01 
plt.figure(figsize=(10, 10))
plt.title("Wykres 1\nSoczewka 1 Zależność b(a)")

max_limit = 100
plt.xlim(0, max_limit)
plt.ylim(0, max_limit)
plt.gca().set_aspect('equal', adjustable='box')
ticks = np.linspace(0, max_limit, num=11)
plt.xticks(ticks)
plt.yticks(ticks)

plt.xlabel("a [cm]")
plt.ylabel("b [cm]")
plt.errorbar(a, b, xerr=delta, yerr=delta, fmt='o', capsize=5, capthick=1,ecolor='red',label='b(a)')
plt.legend()
plt.show()