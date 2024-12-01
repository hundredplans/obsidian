Θ (Theta / =)
O (Big O / <=)
o (Small o / <)
Ω (Omega / >=)
ω (Omega / >)

Useful for comparing which functions grow faster
# Theta
Rosnie w tym samym tempie
Θ(g(n)) = {f(n): ∃c<sub>1</sub> c<sub>2</sub> > 0 ∃ n<sub>0</sub> ∈ N ∀<sub>n>=n<sub>0</sub></sub>  0 <= c<sub>1</sub> • g(n) <= f(n) <= c<sub>2</sub> • g(n)}

f(n) jest ograniczone przez c1, c2 • g(n)
Wybieramy stale c1, c2, n0

n<sub>0</sub> to numer ktory dziala dla ograniczenia c1, c2

3n<sup>2</sup> + 5 = Θ(n<sup>2</sup>)
2n + 4 = Θ(n)

# Big O
O(g(n)) = {f(n): ∃c > 0 ∃ n<sub>0</sub> ∈ N ∀<sub>n>=n<sub>0</sub></sub>  0 <= f(n) <= c • g(n)}
Rosnie nie szybciej niz g(n)

2n + 3 = O(n)
2n + 3 = O(n<sup>2</sup>)
log(n) = O(n)

# Big Omega
Rosnie szybciej lub rowno g(n)
Ω(g(n)) = {f(n): ∃c > 0 ∃ n<sub>0</sub> ∈ N ∀<sub>n>=n<sub>0</sub></sub>  0 <= c • g(n) <= f(n)}

5n<sup>2</sup> + 2 = Ω(n)
2n + 3 = Ω(1)
2n + 3 = Ω(log(n))

# Small o
Wolnej niz g(n)
o(g(n)) = {f(n): ∀<sub>c > 0</sub> ∃<sub>n<sub>0</sub> ∈ N</sub> ∀<sub>n>=n<sub>0</sub></sub>  0 <= f(n) < c • g(n)}

5n + 5 = o(n<sup>2</sup>)
lim<sub>n -> 0</sub> f(n) / g(n) = 0 (Definicja)
eg -> lim<sub>n -> 0</sub> 5n + 5 / n<sup>2</sup> = 0

# Small Omega
Rosnie szybciej niz g(n)
ω(g(n)) = {f(n): ∀<sub>c > 0</sub> ∃<sub>n<sub>0</sub> ∈ N</sub> ∀<sub>n>=n<sub>0</sub></sub>  0 <= c • g(n) < f(n)}

lim<sub>n -> 0</sub> f(n) / g(n) = ∞ (Definicja)
n<sup>3</sup> = ω(n<sup>2</sup>)

# Liczenie Granicy
L = lim<sub>n -> ∞</sub> f(n) / g(n)

![[algorithm_venn.png|Jezeli policzysz granice f(n) to mozesz wiedziec do ktorej funkcji dojsc]] 

# Zadania
## Zad 1
f(n) = 10n
g(n) = 77n<sup>2</sup>
h(n) = 6n<sup>2</sup> + n<sup>2</sup>log(n)
i(n) = 10n<sup>4</sup> 

ZROB WLASNA TABELE

n<sup>2</sup>log(n) rosnie szybciej niz n<sup>2</sup> bo
- 1 < log(n) < n
- n<sup>2</sup> < n<sup>2</sup>log(n) < n<sup>3</sup> 

## Zad 2
lg(n) = log<sub>2</sub>(n)
Prawda czy falsz

Trzeba uproscic do latwiejszych funkcji
a) n<sup>2</sup> = Ω(2<sup>nlg(n)</sup>) Falsz (2<sup>nlg(n)</sup> = n<sup>n</sup>) -> n<sup>2</sup> = Ω(n<sup>n</sup>)
b) n<sup>3</sup> = Ω(2<sup>lg(n)</sup>) Prawda (n<sup>3</sup> = Ω(n))
c n! = O(2<sup>lg(n)</sup>) Falsz (2<sup>lgn</sup> = n) -> n! = O(n)
d) 3<sup>n + 2</sup> = Θ(3<sup>n</sup>) Prawda (lim<sub>n -> ∞</sub> 3<sup>n + 2</sup> / 3<sup>n</sup> = 3<sup>2</sup> = 9)
e) 3<sup>n</sup> = Θ(2<sup>n</sup>) Falsz (lim<sub>n -> ∞</sub> 3<sup>n</sup> / 2<sup>n</sup> = (3/2)<sup>n</sup> = ∞)


## Zad 3
Rozwiaz tabele
f(n) | g(n) | f(n) = o(g(n)) | f(n) = Θ(g(n)) | f(n) = ω(g(n))
2<sup>n</sup> | 3<sup>n</sup>
log(n) | lg(n)
2n<sup>2</sup> | n
nlgn | n<sup>2</sup> 