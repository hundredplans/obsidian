import matplotlib.pyplot as plt
import numpy as np
a = np.array([
12,
12,
12,
12,
11.5,
88.5,
84,
78.5,
73.5,
68.5,
])

b = np.array([
88,
83,
78,
73,
68.5,
11.5,
11,
11.5,
11.5,
11.5,
])

delta = 0.01 
plt.figure(figsize=(10, 6))
plt.title("Wykres 3\nSoczewka 2 Zależność b(a)")
plt.xlabel("a [cm]")
plt.ylabel("b [cm]")

max_limit = 100
plt.xlim(0, max_limit)
plt.ylim(0, max_limit)
plt.gca().set_aspect('equal', adjustable='box')
ticks = np.linspace(0, max_limit, num=11)
plt.xticks(ticks)
plt.yticks(ticks)

plt.errorbar(a, b, xerr=delta, yerr=delta, fmt='o', capsize=5, capthick=1,ecolor='red',label='b(a)')
plt.legend()
plt.show()