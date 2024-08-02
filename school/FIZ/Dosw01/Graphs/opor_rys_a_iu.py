import matplotlib.pyplot as plt

voltage=[
2.02,
4.02,
5.99,
7.97,
9.96,
11.92,
13.90,
15.93,
17.92,
19.87,
21.90,
23.80,
]

current=[
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
]

delta_current=[
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

plt.title('Wykres 3\nDrut (Rys. A) Zależność I(U)')
plt.xlabel('U [V]')
plt.ylabel('I [mA]')

plt.errorbar(voltage, current, yerr=delta_current, fmt='o', capsize=5, capthick=1, ecolor='red', label='I(U)')
plt.legend()
plt.show()