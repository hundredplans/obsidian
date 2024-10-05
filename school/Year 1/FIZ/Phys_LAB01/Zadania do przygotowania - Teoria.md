
#### Dynamika ruchu obrotowego bryły sztywnej

**Bryła sztywna** - Ciało fizyczne, którego elementy (punkty materialne) nie mogą się względem siebie przemieszczać nazywamy bryłą sztywną. *(W skrócie; dosłownie sztywne, nie plastyczne ciało).*


Gdy taka bryła **obraca się wokół jakiejś osi**, każdy punkt materialny (oprócz tego bezpośrednio na osi) porusza się po **okręgu** pod kątem prostopadłym do osi.
Środki tych okręgów leżą na osi obrotu.
![[DynamikaRuchuObrotowego.png|300]]
* Excuse the black on black, but im too lazy to recolour.

Promienie wodzące (wektor łączący punkt na obwodzie okręgu z osią obrotu, tu $r_i$) punktów bryły zakreślają w zadanym przedziale czasu **takie same kąty**, a więc ***prędkość kątowa i przyspieszenie kątowe są dla wszystkich punktów bryły jednakowe.***

------------------------
#### Moment bezwładności

Do opisu ruchu obrotowego bryły sztywnej służą m.in. moment bezwładności.

Moment bezwładności; co zmienia w zależności od jego wartości:
- **Wysoka wartość** momentu bezwładności powoduje, że *ciężko jest zmienić* ruch obrotowy danego ciała wokół osi.
- **Niska wartość** momentu bezwładności pozwoli w *łatwy sposób* zmieniać jego prędkość w ruchu obrotowym wokół tej osi.


Moment bezwładności to stosunek długości i masy, opisywany literką `I`
$$I = \sum_{i=1}^{n} m_ir_i^2 $$
W powyższym wzorze $m_i$ oznaczają masę fragmentów ciała oddalonych od osi obrotu o $r_i$.
*W skrócie; moment bezwładności to stosunek masy razy długość.*

------------------------
#### Twierdzenie Steinera
Eng. Parallel axis theorem/Steiner's theorem

Pozwala wyliczyć moment bezwładności obiektu względem osi równoległej.

`Moment bezwładności względem osi równoległej do osi przechodzącej przez środek masy jest sumą momentu bezwładności względem osi przechodzącej przez środek masy oraz iloczynu masy i kwadratu odległości pomiędzy osiami:`
i.e:
$I_o$ - moment bezwładności osi przechodzącej przez środek masy
$I_r$ - moment bezwładności osi równoległej do osi $I_o$
$m$ - masa bryły
$d$ - odległość między osiami $I_o$ i $I_r$ 
$$I_o = I_r + md^2 $$
[Przykład wykorzystania twierdzenia Steinera](https://www.dobrykorepetytor.pl/wiedza/twierdzenie-steinera/#przyklad-wykorzystania-twierdzenia-steinera)

------------------------
#### Wahadło fizyczne - równanie ruchu, okres drgań, długość zredukowana wahadła
###### Równanie ruchu
$$I \frac{d^20}{dt^2} + mgd sin0 = 0$$
$I$ - [[Zadania do przygotowania - Teoria#Moment bezwładności|Moment Bezwładności]]
$\frac{d^20}{dt^2}$ - Przyspieszenie kątowe (na rysunku $\omega$ - szybkość zmiany prędkości ruchu obrotowego)
![[Pasted image 20240425123944.png|300]]
$m$ - masa wahadła
$g$ - przyspieszenie grawitacyjne
$d$ - odległość od górnej części wahadła do środka masy
$0$ - pionowe przemieszczenie kątowe

Dla małych kątów $\sin(0) \approx 0$, więc można go pominąć.

###### Okres drgań
`Wyznaczanie okresu drgań wahadła matematycznego polega na zmierzeniu czasu trwania kilku lub kilkudziesięciu wahnięć i podzieleniu wyniku tego pomiaru przez liczbę wahnięć.`
$$T = \frac{t_n}{n}$$
$n$ - liczba wahnięć.
$t_n$ - czas trwania n ilości wahnięć.

Wyprowadzenie wzoru na okres drgań:

*Warto wspomnieć że* $\omega = \frac{2\pi}{T}$ *i określa jak szybko (w radianach) wahadło fizycznie się porusza*
oraz: $\omega^2 = \frac{mgd}{I}$
stąd:
$$I \frac{d^20}{dt^2} + \omega^2 = 0$$

a więc okres drgań ruchu, po podstawieniu $\omega = \frac{2\pi}{T}$ będzie wynosił:
$$T = 2\pi \sqrt{\frac{I}{mgd}}$$
$I$ - [[Zadania do przygotowania - Teoria#Moment bezwładności|Moment Bezwładności]]
$m$ - masa wahadła
$g$ - przyspieszenie grawitacyjne
$d$ - odległość od górnej części wahadła do środka masy

###### Długość zredukowana wahadła

`Długość zredukowana L wahadła fizycznego jest równa takiej długości wahadła matematycznego, które posiada ten sam okres drgań co dane wahadło fizyczne`

$$L = \frac{I}{md}$$
$I$ - [[Zadania do przygotowania - Teoria#Moment bezwładności|Moment Bezwładności]]
$m$ - masa wahadła
$d$ - odległość od górnej części wahadła do środka masy

Okres drgań wahadła matematycznego:
$$T = 2\pi\sqrt{\frac{L}{g}}$$
$L$ - Długość wahadła
$g$ - przyspieszenie grawitacyjne

Okres drgań wahadła fizycznego: [[Zadania do przygotowania - Teoria#Okres drgań|Click]]

------------------------
**[[school/Year 1/FIZ/Phys_LAB01/Resources]]**

[[Wahadło Rewersyjne - MAIN PDF.pdf|Main source of these notes]]