import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

resistance = [
    7.0345,
    10.4474,
    13.3556,
    15.4231,
    17.1724,
    18.9683,
    20.4853,
    21.7397,
    23.2078,
    24.2683,
    25.3488,
    26.4444,
]
delta_resistance = [
0.94636,
1.31993,
1.63257,
1.83910,
2.01349,
2.19807,
2.34993,
2.47191,
2.62231,
2.72291,
2.84127,
2.94938,
]

current = np.array([
0.29,
0.38,
0.45,
0.52,
0.58,
0.63,
0.68,
0.73,
0.77,
0.82,
0.86,
0.90,
])
delta_current = [
0.024500,
0.029000,
0.032500,
0.036000,
0.039000,
0.041500,
0.044000,
0.046500,
0.048500,
0.051000,
0.053000,
0.055000,
]

plt.figure(figsize=(10, 6))
plt.title('Wykres 2\n Żarówka (Rys. A) Zależność R(I)')
plt.xlabel('I [A]')
plt.ylabel('R [Ω]')

plt.errorbar(current, resistance, xerr=delta_current, yerr=delta_resistance, fmt='o', capsize=5, capthick=1, ecolor='red', label='R(I)')

slope, intercept, r_value, p_value, std_err = linregress(current, resistance)
fit_line = slope * current + intercept
plt.plot(current, fit_line, label="Dopasowanie", color='blue')

plt.legend()
plt.show()