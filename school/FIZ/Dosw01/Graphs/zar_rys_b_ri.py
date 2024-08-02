import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

resistance = [
6.7000,
10.5000,
13.2000,
15.2500,
17.1207,
18.9048,
20.4118,
20.6438,
22.9103,
24.1585,
25.4651,
26.3333,
]
delta_resistance = [
0.6726,
1.0530,
1.3232,
1.5281,
1.7152,
1.8936,
2.0443,
2.0673,
2.2941,
2.4189,
2.5611,
2.6474,
]
current = np.array([
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
])
delta_current = [
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
plt.title('Wykres 6\n Żarówka (Rys. B) Zależność R(I)')
plt.xlabel('I [A]')
plt.ylabel('R [Ω]')

plt.errorbar(current, resistance, xerr=delta_current, yerr=delta_resistance, fmt='o', capsize=5, capthick=1, ecolor='red', label='R(I)')
slope, intercept, r_value, p_value, std_err = linregress(current, resistance)
fit_line = slope * current + intercept
plt.plot(current, fit_line, label="Dopasowanie", color='blue')

plt.legend()
plt.show()