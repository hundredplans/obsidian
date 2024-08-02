# F
- Wartosc sily / Force
- F ~ r (Wartosc sily jest propocjonalne do odleglosci)
- F zalezy od m (material/mass)
- F = ma
- F = kx *-> W jednej osi*

# r<sup>-></sup>
- Wektor polozenia

# k
- Wspolczynnik spreznosci
- Material
- Kierunek
- Some constant that multiplies our wektor polozenia / odchylennie
# F<sup>-></sup> 
- Wektor sily
- F<sup>-></sup> = -kr<sup>-></sup> (Zwrot sily jest przeciwny do odchylenia)
- F<sup>-></sup> = ma<sup>-></sup> (force = mass * acceleration)
	- -kr<sup>-></sup> = ma<sup>-></sup>
	- -kx = ma (jezeli na jednej osi, przyszpieszenie nie ma kierunku)
	- -kx = m • d<sup>2</sup>x/dt<sup>2</sup>
	- d<sup>2</sup>x/dt<sup>2</sup> = -kx / m
	
	- x(t) = ASin(ωt + φ) *-> This is a function we expect to derive into something similar, forget about -kx / m for now (A is the amplitude)*
		- dx/dt = ACos(ωt + φ) \* ω -> v(t)
		- d<sup>2</sup>x/dt<sup>2</sup> = -ASin(ωt +φ) \* ω<sup>2</sup> -> a(t)
		
	- -ASin(ωt +φ) \* ω<sup>2</sup> = -kASin(ωt +φ) / m *-> We place the equation x(t) instead of x and x''(t) instead of d<sup>2</sup>x/dt<sup>2</sup>*
		- After canelling out common terms:
		- ω<sup>2</sup> = k / m
		- ω = sqrt(k / m)

# A
- Amplituda, najwieksza wartosc I najmniejsza sin'a
- Dla cos'a przesun o pi/2 (sin - pi/2)
# ω
- ω = sqrt(k / m)
- ω = 2PI / T = 2PI • f
# v<sup>-></sup>
- v<sup>-></sup> = dr<sup>-></sup>/dt

# a<sup>-></sup>
- a<sup>-></sup> = F<sup>-></sup> / m (Drugie prawo newtona)
- a<sup>-></sup> = dr<sup>-></sup>/dt<sup>2</sup>

# E<sub>k</sub> 
- Kinetic energy
- E<sub>k</sub> = mv<sup>2</sup> / 2
	- v(t) = AωCos(ωt + φ)
	- E<sub>k</sub> = (m • A<sup>2</sup>ω<sup>2</sup>cos<sup>2</sup>(ωt + φ) / 2 *-> Sub in for v(t)*
	- ω = sqrt(k / m)
- E<sub>k</sub> = kA<sup>2</sup>cos<sup>2</sup>(ωt + φ) / 2 *-> Sub in ω<sup>2</sup>*

# E<sub>p</sub>
- Energia potencjalna
- W = Praca / work
- E<sub>p</sub> =
	- -∫F • dx = 
	- -∫-kx • dx = 
	- ∫kx • dx
	- kx<sup>2</sup> / 2 *-> Since integral of x is x<sup>2</sup> / 2*
- We know x(t) = Asin(ωt + φ)
	- kx(t)<sup>2</sup> / 2 =
	- kA<sup>2</sup>sin<sup>2</sup>(ωt + φ) / 2
- Notice that kA<sup>2</sup> / 2 is the same as in E<sub>k</sub>
# E<sub>c</sub>
- Energia calkowita
- E<sub>c</sub> = E<sub>k</sub> + E<sub>p</sub>
- E<sub>c</sub> = kA<sup>2</sup>cos<sup>2</sup>(ωt + φ) / 2 + kA<sub>2</sub>sin<sup>2</sup>(ωt + φ) / 2
	- E<sub>c</sub> = (kA<sup>2</sup> / 2)(cos<sup>2</sup>(ωt + φ) + sin<sup>2</sup>(ωt + φ))
	- E<sub>c</sub> = kA<sup>2</sup> / 2 *-> cos<sup>2</sup> + sin<sup>2</sup> = 1*
- Energa calkowita zawsze jest rownowazna, k, A sa constant
- Potencjalna I kinetyczna zmienia sie ale calkowita zostaja kA<sup>2</sup>/2
# General
- Zmiana predkosci jest najwieksza na brzegach (Potencjalna energia)
- Kinetyczna energia jest najwieksza w srodku