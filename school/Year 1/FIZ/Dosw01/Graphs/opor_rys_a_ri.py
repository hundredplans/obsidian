import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

resistance = [
111.6022,
112.9213,
110.3131,
111.1576,
110.6667,
110.7807,
110.8453,
110.7019,
111.0285,
111.3789,
109.5000,
113.3333,
]
delta_resistance = [
11.7823,
11.6121,
11.2363,
11.2722,
11.1907,
11.1820,
11.1737,
11.1478,
11.1723,
11.2009,
16.4750,
16.7778,
]
current = np.array([
18.10,
35.60,
54.30,
71.70,
90.00,
107.60,
125.40,
143.90,
161.40,
178.40,
200.00,
210.00,
])
delta_current = [
0.000001005,
0.000001880,
0.000002815,
0.000003685,
0.000004600,
0.000005480,
0.000006370,
0.000007295,
0.000008170,
0.000009020,
0.000020000,
0.000020500,
]

plt.figure(figsize=(10, 6))
plt.title('Wykres 4\nDrut (Rys. A) Zależność R(I)')
plt.xlabel('I [mA]')
plt.ylabel('R [Ω]')

plt.errorbar(current, resistance, xerr=delta_current, yerr=delta_resistance, fmt='o', capsize=5, capthick=1, ecolor='red', label='R(I)')
slope, intercept, r_value, p_value, std_err = linregress(current, resistance)
fit_line = slope * current + intercept
plt.plot(current, fit_line, label="Dopasowanie", color='blue')

plt.legend()
plt.show()