import matplotlib.pyplot as plt

voltage=[
2.00,
3.98,
5.90,
7.84,
9.90,
11.77,
13.81,
15.73,
17.65,
19.62,
21.50,
23.90,
]

current=[
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
]

delta_current=[
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

plt.title('Wykres 7\nDrut (Rys. B) Zależność I(U)')
plt.xlabel('U [V]')
plt.ylabel('I [mA]')

plt.errorbar(voltage, current, yerr=delta_current, fmt='o', capsize=5, capthick=1, ecolor='red', label='I(U)')

plt.legend()
plt.show()