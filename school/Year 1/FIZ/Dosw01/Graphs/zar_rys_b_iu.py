import matplotlib.pyplot as plt

current = [
0.30,
0.38,
0.45,
0.52,
0.58,
0.63,
0.68,
0.73,
0.78,
0.82,
0.86,
0.90,
]
voltage = [
2.01,
3.99,
5.94,
7.93,
9.93,
11.91,
13.88,
15.07,
17.87,
19.81,
21.90,
23.70,
]
current_delta = [
0.015100,
0.019100,
0.022600,
0.026100,
0.029100,
0.031600,
0.034100,
0.036600,
0.039100,
0.041100,
0.043100,
0.045100,
]

plt.figure(figsize=(10, 6))

plt.title('Wykres 5\nŻarówka (Rys. B) Zależność I(U)')
plt.xlabel('U [V]')
plt.ylabel('I [A]')

plt.errorbar(voltage, current, yerr=current_delta, fmt='o', capsize=5, capthick=1, ecolor='red', label='I(U)')
plt.legend()

plt.show()