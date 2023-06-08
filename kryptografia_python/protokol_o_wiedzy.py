#Kampa Agnieszka WCY21KY1S1 zad 7.
#protokol dowodu o wiedzy dotyczacy znajomosci logarytmu dyskretnego

#dlugosc b charakterystyki p ciala Fp
bl = 15

#procedura generujaca parametry potrzebne do protokolu
#wejscie - dlugosc charakterystyki b w bitach
#wyjscie - liczba pierwsza p, a, b, tajne x
def generowanie_parametrow(bl):
    p = 0
    while(is_prime(p) == False):
        p = getrandbits(bl)
    F = GF(p)
    a = F.primitive_element()
    x = 10000000000000
    while (gcd(x, p - 1) != 1):
        x = F.random_element()
    b = (a**x) % p

    return p, a, b, x

#procedura generujaca potrzebne do portokolu wartosci(ze strony A)
#wejscie - liczba p i a
#wyjscie - h i r
def krok1(p, a):
    r = randint(1, p - 1)
    h = a ** r
    return h, r

#procedura losujaca losowy bit k
#wyjscie - losowy bit k
def krok2():
    k = randint(0, 1)
    return k

#procedura liczaca wartosc s potrzebna do potwierdzenia wiedzy(ze strony A)
#wejscie - r, k, x, p
#wyjscie - liczba s
def krok3(r, k, x, p):
    s = mod(r + k * x, p - 1)
    return s

#procedura potwierdzajaca ze obliczenia sa prawdilowe i ze A ma ta wiedze(ze strony B)
#wejwcie - a, s, h, b, k, p - wszystkie wartosci po za tajnym x, ktorego znajomosc udowadnia A
def krok4(a, s, h, b, k, p):
    lewa = power_mod(a, s, p)
    prawa = mod(power_mod(b, k, p) * h, p)
    if prawa == lewa:
        return 1
    else:
        return -1

#procedura realizujaca poszczegolne kroki protokolu
def main():
    udane = 0 #dane potrzebne do zliczania poprawnych i niepoprawnych odpowiedzi
    nieudane = 0
    p, a, b, x = generowanie_parametrow(bl)
    t = 100 #wartosc okreslajaca ilosc prob

    print("wygenerowane parametry:")
    print("a:", a, "b:", b, "p:", p, "x:", x)


    for i in range(t):
        print("\n")
        print("krok 1:")
        h, r = krok1(p, a)
        print("h:", h, "r:", r, "przesylam te wartosci do B")

        print("krok 2:")
        k = krok2()
        print("k:", k)

        print("krok 3:")
        s = krok3(r, k, x, p)
        print("s:", s, "przesylam ta wartosc do B")

        print("krok 4:")
        werdykt = krok4(a, s, h, b, k, p)
        if werdykt == 1:
            print("wszystko sie zgadza, potwierdzam")
            udane = udane + 1
        else:
            print("nie zgadza sie")
            nieudane = nieudane + 1
    print("\n")
    print("ilosc udanych prob:", udane, "/", nieudane + udane)

main()