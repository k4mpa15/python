#Kampa Agnieszka WCY21KY1S1 6.1


#parametry wejsciowe:
#b - dlugosc modulu RSA n w bitach
b = 20

#procedura generujaca klucze
#wyjscie - klucz (d, n) i (e, n) oraz wartosci p i q
def generowanie_kluczy_RSA():
    p = 0
    q = 0
    while ((is_prime(p) and is_prime(q) and p.bit_length() - q.bit_length() < 3) == False):
        p = randint(2**(b//2 - 1), 2**(b//2))
        q = randint(2**(b//2 - 1), 2**(b//2))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 1000000000000000
    while gcd(e, phi) != 1:
        e = randint(1, phi)

    d = power_mod(e, -1, phi)
    return p, q, n, d, e

#procedura wybierajaca losowa wartosc k
#wejscie - n
#wyjscie - k
def wybor_losowy(n):
    k = randint(1, n)
    return k

#procedura zaciemnaiajaca wiadomosc
#wejscie - wiadomosc m, k, klucz (e, n)
#wyjscie - cien t
def zaciemnienie_wiadomosci(m, k, e, n):
    t = (m * power_mod(k, e, n)) % n
    print("przesylam", t, "uzytkownikowi B")
    return t

#procedura geenrujaca podpis
#wejscie - t, klucz (d, n)
#wyjscie - podpis r
def podpis_B(t, d, n):
    r = power_mod(t, d, n)
    print("wysylam r:", r, " do A")
    return r

#procedura dajaca s czyli faktyczny podpis
#wejscie - r, k i n
#wyjscie - podpis s
def usuniecie_zaciemnienia(r, k, n):
    s = (r * power_mod(k, -1, n)) % n
    return s

#procedura weryfikacji podpisu
#wejscie - wiadomosc m, s, klucz (e, n)
#wyjscie - werdykt
def weryfikacja_podpisu(m, s, e, n):
    t = power_mod(s, e, n)
    print("Obliczone t:", t)
    if t == m:
        return True
    else:
        return False

#funkcja main
def main():

    m = 123456 #wiadomosc m

    p, q, n, d, e = generowanie_kluczy_RSA()
    print("wartosci p i q oraz klucze uzytkownika B:")
    print("p:", p, "q:", q, "n:", n, "d:", d, "e:", e)
    print("\n")

    #krok 1
    print("krok 1:")

    k = wybor_losowy(n)
    print("wylosowane k przez A:", k)
    print("\n")

    #krok 2
    print("krok 2:")
    t = zaciemnienie_wiadomosci(m, k, e, n)
    print("zaciemniona wiadomosc m, jako t:", t)
    print("\n")

    #krok 3
    print("krok 3:")
    r = podpis_B(t, d, n)
    print("\n")

    #krok 4
    print("krok 4:")
    s = usuniecie_zaciemnienia(r, k, n)
    print("podpis pod wiadomoscia m to s:", s)

    #weryfikacja podpisu
    print("weryfikacja podpisu:")
    werdykt = weryfikacja_podpisu(m, s, e, n)
    if werdykt == True:
        print("podpis poprawny")
    else:
        print("podpis niepoprawny")

#wywolanie funkcji main
main()