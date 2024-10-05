import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

resistance = [
111.1111,
109.9448,
111.5312,
111.5220,
112.5000,
111.4583,
111.8219,
111.1661,
111.0761,
110.8475,
108.9711,
119.5000,
]
delta_resistance = [
11.7340,
11.3010,
11.3658,
11.3123,
11.3790,
11.2523,
11.2735,
11.1959,
11.1781,
11.1479,
16.4709,
17.9750,
]
current = np.array([
18.00,
36.20,
52.90,
70.30,
88.00,
105.60,
123.50,
141.50,
158.90,
177.00,
197.30,
200.00,
])
delta_current = [
0.000001000,
0.000001910,
0.000002745,
0.000003615,
0.000004500,
0.000005380,
0.000006275,
0.000007175,
0.000008045,
0.000008950,
0.000019865,
0.000020000,
]

plt.figure(figsize=(10, 6))
plt.title('Wykres 8\nDrut (Rys. B) Zależność R(I)')
plt.xlabel('I [mA]')
plt.ylabel('R [Ω]')

plt.errorbar(current, resistance, xerr=delta_current, yerr=delta_resistance, fmt='o', capsize=5, capthick=1, ecolor='red', label='R(I)')
slope, intercept, r_value, p_value, std_err = linregress(current, resistance)
fit_line = slope * current + intercept
plt.plot(current, fit_line, label="Dopasowanie", color='blue')

plt.legend()
plt.show()