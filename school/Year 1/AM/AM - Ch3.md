# Kryterium Porownawcze
- Warunek Konieczny
	- Treat szereg like a sequence
	- lim<sub>i</sub> -> ∞ = 0
	- Szereg moze byc zbiezny
- If warunek konieczny is met find a similar greater or smaller szereg that is zbiezny
- Na mocy kryterium porownawczej szereg jest zbiezny

# Szereg Harmoniczny
- Rzad a > 1 -> Zbiezny
- Rzad a <= 1 -> Rozbiezny
- Jako szereg rzadu alpha a = x szereg jest zbiezny
- 1 / 3n -> Still count as szerege harmoniczny

# Szereg Geometryczny
- aq<sup>n</sup>
- q < 1 -> Szereg zbiezny
- q >= 1 -> Szereg rozbiezny
- Jako szereg geometryczny o ilorazie q < x szereg jest zbiezny

# Useful Properties
- lim<sub>n</sub> sin(x/n) / (x / n) = 1
- sin(x) < x < tg(x)
	- sin(x) < x
	- tg(x) > x
	- x / 2 < sin(x)
	- Useful for szeregi finding harmonic szeregi
- log<sub>a</sub> < n
- ln(1 + n) < n
- 2sinxcosx = sin(2x)

# Trig Functions
- For small values can approximate sin(x) = x, tan(x) = x
- Use for szereg geometryczny or harmoniczny
- You know cos(x) is always less than 1

# For n<sup>n</sup>, n! (d'Alembert)
- lim<sub>n -> ∞</sub>  a<sub>n+1</sub> / a<sub>n</sub>
- If ratio is less than 1 -> a<sub>n</sub> zbiezny
- If ratio is greater than 1 -> a<sub>n</sub> rozbiezny

# For n'th root / n<sup>n</sup> / iloczyn exponents (Cauchy)
- lim<sub>n -> ∞</sub> n'th root (a<sub>n</sub>)
- Cover your formula in the n'th root and distribute
- If limit is < 1 -> a<sub>n</sub> zbiezny
- If limit is > 1 -> a<sub>n</sub> rozbiezny

# For (-1)<sup>n</sup> (Leibniz)
- Remove (-1)<sup>n</sup> from equation
- a<sub>n+1</sub> - a<sub>n</sub> <= 0 *-> Ciag maleje, can also check if there's only one negative sign in a fraction*
	- Stad ciag jest nierosnacy
- lim<sub>n -> ∞</sub> = 0
- If both conditions are met szereg is zbiezny

# Bezwzgledna Zbieznosc
- Cover szereg in abs()
- If this is zbiezne without using Leibniz szereg is bezwzglednie zbiezny
	- Na mocy kryterium bezwzlegdnej zbieznosci szereg jest bezwzglednie zbiezny
- If this is only zbiezne using Leibniz szereg is warunkowo zbiezny
- If this is rozbiezne no matter what szereg is rozbiezny
- Can remove (-1)<sup>n</sup> after covering