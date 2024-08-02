import matplotlib.pyplot as plt

current = [0.29, 0.38, 0.45, 0.52, 0.58, 0.63, 0.68, 0.73, 0.77, 0.82, 0.86, 0.90]
voltage = [2.04, 3.97, 6.01, 8.02, 9.96, 11.95, 13.93, 15.87, 17.87, 19.90, 21.80, 23.80]
current_delta = [0.0245, 0.029, 0.0325, 0.036, 0.039, 0.0415, 0.044, 0.0465, 0.0485, 0.051, 0.053, 0.055]

plt.figure(figsize=(10, 6))
plt.title('Wykres 1\nŻarówka (Rys. A) Zależność I(U)')
plt.xlabel('U [V]')
plt.ylabel('I [A]')

plt.errorbar(voltage, current, yerr=current_delta, fmt='o', capsize=5, capthick=1, ecolor='red', label='I(U)')

plt.legend()
plt.show()