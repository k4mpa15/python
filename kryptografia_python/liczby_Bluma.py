#Agnieszka Kampa WCY21KY1S1 zadanie 5.

#liczby bitow p i q
b1 = 10
b2 = 20

#procedura generujaca liczby Bluma oraz liczby p i q
#wejscie - liczba bitow b1 i b2 odpowiadajce liczbie bitow p i q
#wyjscie - liczby pierwsez p i q oraz liczba Bluma n
def generowanie_liczb_Bluma(b1, b2):
    p = 0
    q = 0
    while (is_prime(p) and is_prime(q) and q % 4 == 3 and p % 4 ==3) == False: #sprawdzenie czy liczby p i n sa pierwsze
        p = getrandbits(b1)
        q = getrandbits(b2)
    print("\tp:", p)
    print("\tq:", q)
    n = p * q
    print("\tn:", n)
    return p, q, n

#procedura generujaca losowa liczbe x wzglednie pierwsza z n
#wejscie - liczba n
#wyjscie - liczba losowa x
def generowanie_x(n):
    x = 0
    while (gcd(n, x) != 1):
        x = randint(2, n)
    print("\tx:", x)
    return x

#procedura obliczajaca x1 i x2
#wejscie - liczba losowa x i n
#wyjscie - liczby x0 i x1 obliczone z pomoca x i n potrzebne do dalszego dzilania
def obliczenie_x(x, n):
    x0 = (x^2) % n
    x1 = (x0^2) % n
    print("\tx0:", x0)
    print("\tx1:", x1)
    return x0, x1
#procedura w krotej B zgaduje parzystosc x0 na podstawie x1
#wejscie - x2
#wyjscie - okreslenie parzystosci
def zgadniecie_B(x1):
    if x1 % 2 == 0:
        return "parzysta"
    else:
        return "nieparzysta"

#procedura ktora oblicza ze strony B liczbę Bluma n oraz x0 i x1 aby sprawdzic czy wszystko sie zgadza
#wejscie - liczby p, q, n, x, x0 i x1 w celu weryfikacji tych liczb
#wyjscie - werdykt czy wszystko sie zgadza
def obliczenia_B(p, q, n, x, x0, x1):
    n_B = p * q
    werdykt = ""
    if n_B == n:
        print("\tn jest liczba calkowita Bluma")
    else:
        print("\tn nie jest liczba calkowita Bluma")
        werdykt = "liczby sie nie zgadzaja"

    x0_B = (x^2) % n
    x1_B = (x0_B^2) % n
    if x0_B == x0 and x1_B == x1:
        print("\tx1 i x0 sie zgadza")
        werdykt = "liczby sie zgadzaja"
    else:
        print("\tliczby sie nie zgadzaja")
        werdykt = "liczby sie nie zgadzaja"

    return werdykt

#procedura wybierajaca strone na podstawie tego czy B odgadlo dobrze parzystosc
#wejscie - faktyczna liczba x0 i zgadniecie B
#wyjscie - wybor orla lub reszki
def wybor_strony(zgadniecie, x0):
    rzeczywista_wersja = ""
    if x0 % 2 == 0:
        rzeczywista_wersja = "parzysta"
    else:
        rzeczywista_wersja = "nieparzysta"

    if zgadniecie == rzeczywista_wersja:
        return "orzel"
    else:
        return "reszka"

#funkcja realizujaca poszczegolne kroki protokolu
def main():
    print("krok 1")
    print("\tuzytkownik A generuje liczbę Bluma n: ")
    p, q, n = generowanie_liczb_Bluma(b1, b2)
    print("\tuzytkownik A generuje liczbe x wzglednie pierwsza z n: ")
    x = generowanie_x(n)


    print("krok 2")
    print("\tuzytkownik A oblicza x0 i x1:")
    x0, x1 = obliczenie_x(x, n)
    print("\tprzesylam n:", n, "oraz x1:", x1, "do B")


    print("krok 3")
    print("\tuzytkownik B odgaduje czy x0 jest parzyste czy nie:")
    zgadniecie = zgadniecie_B(x1)
    print("\tuzytkownik B odgadl:", zgadniecie)


    print("krok 4")
    print("\tuzytkownik A przesyla do B wartosci x:", x, "i x0:", x0)


    print("krok 5")
    print("\tuzytkownik A przekazuje B parametry p:", p, "oraz q:", q)
    print("\tB oblicza sam liczbe n, oraz sprawdza poprawnosc x0, x1:")

    werdykt = obliczenia_B(p, q, n, x, x0, x1)

    print("\t",werdykt)

    print("\n")

    if werdykt == "liczby sie zgadzaja":
        wybor = wybor_strony(zgadniecie, x0)
        print("\twylosowano: ",wybor)
        print("\n")
        print("pomyslnie zakonczono losowanie")
    else:
        print("losowanie nalezy rozpoczac jeszcze raz")


#wywolanie funkcji main
main()