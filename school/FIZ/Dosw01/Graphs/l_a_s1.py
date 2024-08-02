import matplotlib.pyplot as plt
import numpy as np
a = np.array(
    [
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
    ]
)

l = np.array(
    [
100,
95,
90,
85,
80,
100,
95,
90,
85,
80
    ]
)

delta = 0.01 
plt.figure(figsize=(10, 6))
plt.title("Wykres 2\nSoczewka 1 Zależność l(a)")
plt.xlabel("a [cm]")
plt.ylabel("l [cm]")

max_limit = 100
miny_limit = 75
maxy_limit = 105
plt.xlim(0, max_limit)
plt.ylim(miny_limit, maxy_limit)
plt.gca().set_aspect('equal', adjustable='box')
xticks = np.linspace(0, max_limit, num = 11)
yticks = np.linspace(miny_limit, maxy_limit, num = 7)
yticks = yticks[1:-1]
plt.xticks(xticks)
plt.yticks(yticks)

plt.errorbar(a, l, xerr=delta, yerr=delta, fmt='o', capsize=5, capthick=1,ecolor='red',label='l(a)')
plt.legend()
plt.show()