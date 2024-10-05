# Monotonicity
- Exponents and logs behave the same
	- a is base (a != 1)
	- Rosnie for a > 1
	- Maleje for 0 < a < 1

# Ograniczenie
- Can be established by isolating n
	- n > x, n < x etc
- Ograniczony z dolu
	- Equation >= m
	- Find a true statement out of this
	- Can use definition of natural numbers n >= m
- Ograniczony z gory
	- Do equation <= M
- Ograniczony
	- Do m <= a<sub>n</sub> <= M
- For all of these can do Equation (with M in it) > 0
	- M - 3 > 0
	- 2 - M > 0
	- If both of these are true ogr exists, etc

# Finding Monotonicity
- Wskaz rosnacy via a<sub>n</sub> < a<sub>n+1</sub>
- Wskaz malejacy via a<sub>n</sub> > a<sub>n+1</sub>
- Can add <= to indicate the opposite nie (nierosnacy, niemalejacy)
- Find a truth out of this to show it's monotonic
- To check monotonicity of a function do a<sub>n</sub> != a<sub>n+1</sub> 
	- If first equation is always greater then maleje
	- If second equation is always greater then rosnie
	- Otherwise it's not monotonic

# Limits
- 1 / n -> 0
- 1 / ∞ -> 0
- ∞ / 0 -> 0
- n / 0 -> ∞
- -n / 0 -> -∞
- 0 / ∞ -> 0

# Symbole Nieoznaczone
- \[∞ / ∞]
- \[0 / 0]
- \[∞ - ∞]
- \[0 \* ∞]
- \[1<sup>∞</sup>]
- \[∞<sup>0</sup>]
- \[0<sup>0</sup>]

# Calculating Limits
- For a non n exponent calculate what's inside and remove exponent
	- Alternatively calcualate what's inside and apply exponent after
- If you have a root covering a division or multiplication, distribute the root and solve

# Infinite Addition
- Replace 1 + 2 ... + n with -> n(n + 1) / 2
- Replace 1 + 4 + ... + n<sup>2</sup> with -> n(n + 1)(2n + 1) / 6
- Replace 1 + 8 + ... + n<sup>3</sup> -> (n(n+1) / 2)<sup>2</sup>

# Limit to 0
- Any limited (ograniczony) sequence multiplied by a sequence that limits to 0 will also be 0
- Use this to calculate the limit of a sequence that has cos, sin etc
- eg (1 / n) \* cos(x)
- Sometimes need to manipulate expression to get OGR * ZBIEZNY DO 0 

# Square Root Limits
- If you need to find the limit of a function with a root and addition
- Multiply by the inverse conjugate / inverse conjugate
- Remember (a + b)(a - b) = a<sup>2</sup> - b<sup>2</sup>

# Exponent Limits (n)
- Solve inside
	- If inside is > 1 then limit is infinite
	- If inside is < 1 then limit is 0 (Yes even negative)
	- If you have a<sup>n</sup> + b<sup>n</sup> then you can factorise it to a<sup>n</sup>(a/b)<sup>n</sup> 
	- This is because (a/b)<sup>n</sup> = (a<sup>n</sup>/b<sup>n</sup>)

# Infinite Sequences
- Can be replaced with some sort of n expression (you have to find it yourself)
- For geometric sequences
	- a<sub>1</sub> = First Term
	- r = a<sub>2</sub> / a<sub>1</sub>
	- S<sub>n</sub> = a<sub>1</sub>(1 - r<sup>n</sup>) / 1 - r
	- Use this sequence to find the limit

# For n<sup>n</sup>, n!
- lim n -> ∞ \[abs(a<sub>n+1</sub> / a<sub>n</sub>)] = q
- q > 1 means a<sub>n</sub> = +∞
- q < 1 means a<sub>n</sub> = 0
- If the ratio of the absolute terms is > 1 limit is +∞
- If the ratio of the absolute terms is < 1 limit is 0
- Used for n<sup>n</sup>, n!

# For n'th root of a + b (Trzy ciagi)
- If you can find equivalent limits for a smaller and greater sequence your sequence's limit is that
- For the lower one you can almost always replace smallest number with 0
- For the larger one you can replace smaller numbers with your greatest number
- 5<sup>n</sup> + 0 <= 5<sup>n</sup> + 3<sup>n</sup> <= 5<sup>n</sup> + 5<sup>n</sup>
	- n'th root cancels out n'th exponent
	- For the right side change to 2 \* 5<sup>n</sup>
	- Then distribute root
	- REMEMBER limit of n'th root of n or any number -> 1 (even negatives, except 0 which is 0)
	- Also works 2n<sup>2</sup> (exponent doesn't matter if it's not n, if it is the limit is inf as root cancels)
- For sin(n) replace with 1 as it's always greater or equal to sin(n)

# Euler's Limit
- lim n -> ∞ (1 + x/n)<sup>n</sup> = e<sup>x</sup> 
- lim n -> ∞ (1 + 1 / f(n))<sup>f(n)</sup> = e
- f(n) musi zbiegiac do +∞
- To solve multiply power by f(n) and the inverse of f(n) *-> For division*
	- Then you can declare the inside zbiega do e
	- Calculate the limit of the outside and then do e<sup>outside</sup>
