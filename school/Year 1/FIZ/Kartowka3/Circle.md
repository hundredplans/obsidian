# r<sup>-></sup>
- r on it's own is just the radius
	- r<sup>→</sup> = x(t)i + y(t)j
	- i, j are constants
	- i = Vector2(1, 0)
	- j = Vector2(0, 1)
	
- rcos(φ)ti + rsin(φ)tj
	- We can get the position given an angle on a unit circle and then scale it accordingly
	- = d/dt(rcos(φ)ti + rsin(φ)tj) *-> This is to find v<sup>-></sup>*
	- = d/dt(rcos(φ)t) * i + d/dt(rsin(φ)t) * j
	- Can place i, j outside as they are constants
	- (r(-sin(φ)t) * dφ/dt * i) + (r(cos(φ)t) * dφ/dt * j) = v<sup>→</sup>
	- Each component is v<sub>x</sub> + v<sub>y</sub> ^
# v<sup>→</sup>
- Tempo zmian wektora polozenia / Wektor predkosci
- dr<sup>→</sup> / dt (Derivative of r, dlugosc kola)
- v<sub>x</sub>, v<sub>y</sub> = ∫a<sub>x</sub>dt, ∫a<sub>y</sub>dt *-> Each component of predkosc can be integrated from acceleration, same with the whole*
- v<sup>→</sup> = w<sup>→</sup> x r<sup>→</sup>
# a<sup>→</sup>
- Przyspieszenie
- Pochodna wektora predkosci v(t) z [[wzgledem]] czasu (a<sup>-></sup> = dv<sup>-></sup>/dt)
- a<sup>→</sup> = d<sup>2</sup>r<sup>→</sup> / dt<sup>2</sup> = d/dt(v(t)) = d/dt(ω<sup>→</sup> x r<sup>→</sup>)
	- (dω<sup>-></sup>/dt) x r<sup>-></sup> + ω<sup>-></sup> x (dr<sup>-></sup>/dt) (dr<sup>-></sup>/dt is same as v<sup>-></sup>)
	- dω<sup>→</sup> / dt = Przyspieszenie katowe = ℰ<sup>→</sup> 
	- ℰ<sup>→</sup> x r<sup>-></sup> + ω<sup>→</sup> x v<sup>-></sup>
	- ℰ<sup>→</sup> x r<sup>-></sup> = a<sub>s</sub><sup>-></sup> 
			- ω<sup>→</sup> x v<sup>-></sup> = a<sub>d</sub><sup>-></sup> 
- a<sup>-></sup> = a<sub>s</sub><sup>-></sup> + a<sub>d</sub><sup>-></sup> 
# ω<sup>→</sup>
- Predkosc katowa
- Always is perpendicular to the plane which is rotating
- Points up if the motion is clockwise
- Points down if the motion is anticlockwise
- ω<sup>→</sup> = dφ/dt
- Used for motion in the same plane
# v(t)
- v = Predkosc liniowa
- v(t) = |v<sup>→</sup>(t)| = sqrt(v<sub>x</sub><sup>2</sup> + v<sub>y</sub><sup>2</sup>)
	- We plug in the formula below (Which we get from position on a unit circle and scaling) into the sqrt formula above
	- r(-sin(φ)t) * dφ/dt * i) + (r(cos(φ)t) * dφ/dt * j)
	- sqrt((dφ/dt)<sup>2</sup> * r<sup>2</sup>sin<sup>2</sup>(φ) + (dφ/dt)<sup>2</sup> * r<sup>2</sup>cos<sup>2</sup>(φ))
	- This formula when cleaned up gives us v = ωr
- v = ωr
	- Predkosc liniowa punkta poruszujacego sie po kole

# a<sub>s</sub><sup>-></sup> 
- Przyspieszenie styczne do kola
- ℰ<sup>→</sup> x r<sup>-></sup>
- Kiedy ω<sup>-></sup> jest staly, since ℰ<sup>→</sup> is the integral of ω<sup>-></sup>
	- ℰ<sup>→</sup> = 0
	- ℰ<sup>→</sup> x r<sup>-></sup> = 0 *-> Cross product of 0 is 0*
	- Then a<sub>d</sub><sup>-></sup> = a<sup>-></sup> 
	- Meaning przyspieszenie stycznie do kola nie ma efektu jezeli predkosc katowa jest stala
# a<sub>d</sub><sup>-></sup> 
- Przyspieszenie dosrodkowe do kola (Points opposite of r<sup>-></sup>)
- a<sub>d</sub><sup>-></sup> = ω<sup>-></sup> x v<sup>-></sup> = ω<sup>-></sup> x (ω<sup>-></sup> x r<sup>-></sup>) 
- = (ω<sup>-></sup> • r<sup>-></sup>)ω<sup>-></sup> - (ω<sup>-></sup> • ω<sup>-></sup>)r<sup>-></sup>  (Just triple product formula, found at bottom)
- = -ω<sup>2</sup>r<sup>-></sup> =  a<sub>d</sub><sup>-></sup> (Simplifcation of formula above)
- = ω<sup>2</sup>r
- ^ Somehow, dude just trust me
- Note that -ω<sup>2</sup> is not the vector, can kind of trink of negative sign as flipping it to point inward
- = v<sup>2</sup> / r
# ℰ<sup>→</sup> 
- Przyspieszenie katow
- dω<sup>-></sup> / dt = ℰ<sup>→</sup> 
- d/dt(ωω<sub>0</sub><sup>-></sup>) *-> ω<sub>0</sub><sup>-></sup> jest wersorem do gory*
- Points the same way as ω (up if circular)
- If you aren't moving the plane of rotation, this is the only acceleration applied

# ℰ
- ℰ = ω / t
# ω
- Tempo zmian przesunieca katowego (angular displacement)
- ω = (dφ / dt)
- ω = v / r
- ω = 2π / T
- ω = 2πf
# T
- Czas na 1 obrot kola
- 1 / T = f
- T = 1 / f

# f
- Ilosc obrotow w jedna sekunde (that's why 1 / T = f)
# d
- Srednica (2r)

# General
- To get predkosc (v<sup>→</sup>)from acceleration (a<sup>→</sup>), calkowac
- You can remove the <sup>→</sup> by taking the dlugosc of said vector
	- If it's 2D, only need sqrt(x<sup>2</sup> + y<sup>2</sup>)
	- Otherwise x,y,z
- Wektor x Wektor means cross product
	- a x (b x c) = (a • c) * b - (a • b) * c
- Can think of predkosc vs wektor as a distance vs a distance with a direction
- a<sup>-></sup> • b<sup>-></sup> = |a<sup>-></sup>| * |b<sup>-></sup>| * cos(φ) *-> φ Is angle between the two vectors*
	- When φ is pi/2 the whole equation is 0 as cos(pi/2) = 0
- a<sup>-></sup> x b<sup>-></sup> = |a<sup>-></sup>| * |b<sup>-></sup>| * sin(φ) *-> φ Is angle between two vectors*
	- | | means the vector loses it's arrow and becomes regular
