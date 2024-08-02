import matplotlib.pyplot as plt
import numpy as np
a = np.array(
    [
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
plt.title("Wykres 4\nSoczewka 2 Zależność l(a)")
plt.xlabel("a [cm]")
plt.ylabel("l [cm]")

max_limit = 100
miny_limit = 75
maxy_limit = 105
plt.xlim(0, max_limit)
plt.ylim(miny_limit, maxy_limit)
xticks = np.linspace(0, max_limit, num = 11)
yticks = np.linspace(miny_limit, maxy_limit, num = 7)
yticks = yticks[1:-1]
plt.xticks(xticks)
plt.yticks(yticks)

plt.errorbar(a, l, xerr=delta, yerr=delta, fmt='o', capsize=5, capthick=1,ecolor='red',label='l(a)')
plt.legend()
plt.show()