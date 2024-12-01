# Liczby Zespolone

## Equations
z = a + bi
z̄ = a - bi

z̄ + ī = a - (b + 1)i

Split real and imaginary -> So (a + b) + i(a + b) = 0
Then take the inside of a + b, i(a + b) = 0
You can substitute a value you get from one side to the other
You solve for a and b then write z = a + bi (with actual values)

When equation = 0 then can remove divider
When you have (a / b) = (c / d) then cross multiply

If you can't find the actual value you can keep z = a or z = bi, for example when a = -2 then b is any imaginary number so bi

Write zeR if it's any real number
For the two z's on either side first find what it's equal to when divided and equal to 1 then add n degrees based on the power

## Postac Trigonometryczna
Find |z| = sqrt(a<sup>2</sup> + b<sup>2</sup>)
cos(φ) = a / |z|
sin(φ) = b / |z|
α = From table
φ = a + czwiartka
z = |z|(cos(φ) + isin(φ))

## De'Moivre
Calculate what's inside then apply power after
(|z|(cos(φ) + isin(φ)))<sup>n</sup> = |z|\* n (cos(nφ) + isin(nφ))
Remember to solve the value all the way

## Pierwiastki
Find value inside root
<sup>n</sup>sqrt(|w|) = (cos(φ + 2πk / n) + isin(φ + 2πk / n)) dla k = 0, 1,..,n - 1
Remember sqrt(4) just means a = 4, b = 0i
3rd root of 8 is 2 (To what power must you raise 2 to get 8)

When you have an unsolvable equation you change it into z = (2 + 4i) \* nth root of 1 and solve 1

## Helpful
sqrt(-4) = 2i
sqrt(-1) = i

Sin
- Positive 0 -> PI
- Negative PI -> 2PI

Cos
- Positive 0 -> PI / 2
- Negative PI / 2 -> 3PI / 2
- Positive 3PI / 2 -> 2PI

cos(a) = cos(-a)
sin(a) = -sin(-a)

When you can't simplify sin, cos you can leave it in that form

# Wielomiany
Remember to change W(x) to W(z) if we're solving for z
W/I(x) = Result of P(x) : Q(x)
R(x) = Remainder

## Pierwiastki
Znajdz pierwiastki wielomianow rzecywistych
x<sub>2</sub> = Sprezenie x<sub>1</sub> 
x<sub>3</sub> = Multiply (x - x<sub>1</sub>)(x - x<sub>2</sub>) then divide that by original wielomian then finally W(x) = 0 to find last

Means you can display wielomian as (x - x<sub>1</sub>)(x - x<sub>2</sub>)(x - x<sub>3</sub>)
You know the total amount of pierwiastkow by the highest power

## Schemat Hornera
Write down the coefficients of each x, and a factor of x to it's left
Bring down the first value and multiply by the factor and place to the right and up
Value above + value below to the right and bring down
Multiply the next value by factor and repeat

At the end the bottom values are your P(x) and the last value is R(x) - Reszta

Next collect your P(x) and do W(x) = (x - x<sub>1</sub>)P(x) where x<sub>1</sub> is left empty
Finally repeat the process for P(x) with x<sub>2</sub> as a factor (remember sprezenie)
Your result should look like x<sup>3</sup> = +-sqrt(value)

## Pierwiastki
sqrt(-16) = 4i
When given 4 factors and need to find 6 multiply all together

## Przedstaw w postaci iloczynu dwumianow
- (z - z<sub>1</sub>)(z - z<sub>2</sub>)
For z<sup>2</sup> find delta and roots then write in form (z - z<sub>1</sub>)(z - z<sub>2</sub>) with the values filled
For z<sup>3</sup> guess a root that equals 0 then long divide original equation by z - root and then solve for delta and place in equation (z - z<sub>1</sub>)(z - z<sub>2</sub>)(z - z<sub>3</sub>)

For z<sup>4</sup> replace with t<sup>2</sup> then find roots of that and replace back with z and do
(z - z<sub>1</sub>)(z - z<sub>2</sub>)(z - z<sub>3</sub>)(z - z<sub>4</sub>)
Remember sqrt(-2) = sqrt(2)\*i


## Przedstaw w postaci iloczynu nierozkladalnych
- Manipulate equation to be in a form you want
- Remember you can add or minus to get to the form you want

a<sup>2</sup> - b<sup>2</sup> = (a - b)(a + b)
a<sup>2</sup> + b<sup>2</sup> = (a - bi)(a + bi)

(a - b)<sup>2</sup> = a<sup>2</sup> - 2ab + b<sup>2</sup>
(a + b)<sup>2</sup> = a<sup>2</sup> + 2ab + b<sup>2</sup>

a<sup>3</sup> - b<sup>3</sup> = (a - b)(a<sup>2</sup> + ab + b<sup>2</sup>)
a<sup>3</sup> + b<sup>3</sup> = (a + b)(a<sup>2</sup> - ab + b<sup>2</sup>)
Flip the second sign ^

For x<sup>4</sup> replace with t<sup>2</sup> and find what value when added makes it into the form a<sup>2</sup> + 2a + b =(a +/- b)<sup>2</sup> then take root of the remainder coefficient and place into (a + b)(a - b)

## Rozloz na ulamki
z<sup>2</sup> / (z-1)(z + 2)(z + 3) = A / (z - 1) + B / (z + 2) + C / (z + 3)
Then multiply everything by all the bottoms
For easy ones can fill in so the other terms equal 0
For hard ones sort each by the highest term and solve equations

Square on outside repeat z / (z - 1)<sup>2</sup> = A / z - 1 + B / (z - 1)<sup>2</sup> 
Square on inside means z / z<sup>2</sup> - 1 = Az + B / z<sup>2</sup> - 1
If both then obviously do for both

Remember when multiplying with square on outside to not double multiply
When finished place values back in equation
Always make sure you can't factorize further
# Macierze
Multiply - First row by second column

f(x) for A -> Replace x's with A (eg x<sup>2</sup> + 2, A = macierz, 2 replaced with 2I)

Uklad rownan -> 2 equations provided, make one equation variable = the minus of the other and solve for X

X<sup>T</sup> -> Rows become columns, first row = first column, second row = second column

Replace X with \[a, b, c, d] macierz
Remember you can change \[a, b, c, d] = \[macierz] into rownanie if they are same size then solve for each variable independently

# Wyznaczniki
1x1 = a
2x2 = ad - bc
3x3 = Multiply each diagonal and add then minus multiplying every diagonal from other side

## Laplace (For 4x4)
Only works for squares
Cover one row
Multiply (-1) by power of value of row + column
Multiply by value chosen for that row
Multiply by wyznacznik of the macierz minus that row + col
Repeat for each column of the hidden row and add result
Formula: (-1)<sup>r+c</sup> a<sub>rc</sub> detA<sub>rc</sub> 

## Przekstalcenia Elementarne
- Add to a row another row multiplied by a static number
- Swap the places of two rows (Changes to negative)
- Multiply a row by non 0 -> Multiplies the entire matrix by C

You want to get to the form a bottom or top triangle (all 0's)