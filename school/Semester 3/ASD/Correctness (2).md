# To calculate n!

Wejscie: n, n ∈ N
Wyjscie: n!


```
int suma = 1
for (int i = 1, i <= n, i++) {
	suma *= i	
}
```

{P} = Wejscie
{Q} = Wyjscie

{P} prog {Q}
{n ∈ N} suma = 1 ; for (i = 1; i <= n; i++) suma \*= 1 {suma = n!}

# Czescowa Poprawnosc
Jezeli program prog uruchomiony w stanie spelniajacym pre-warunek P zakonczy swoje dzialanie to spelniony jest post-warunek Q.

α -> Spelniajacy pre-warunek P
β -> Program sie skonczy
γ -> Spelniony jest post-warunek Q
(α ^ β) => γ

Jezeli program sie nie skonczy program nadal jest czesciowo poprawny
![[truth_table.png|g=γ]]

Wyprowadzenia warunkowiami
Przeslanki, Wnioski

Partial Correctness -> If a value is returned it's valid
Full Correctness -> A value is returned and is valid