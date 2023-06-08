#Kampa Agnieszka WCY21KY1S1 zadanie 4
#procedura generujaca klucze
#wyjscie - klucze prywatny: x i publiczny: X, liczba pierwsza p

def generowanie_kluczy():
    p = 0
    while (is_prime(p)) == False:
        p = randint(2,2000000)
    C = GF(p)
    g = C.primitive_element()
    x = 1000000000000000
    while (gcd(x, p - 1) != 1):
        x = randint(1, p - 1)
    X = (g^x) % p
    return p, g, x, X

#procedura generacji podpisu
#wejscie - wiadomosc m, klucz prywatny x, liczba pierwsza p
#wyjscie - podpis z

def generacja_podpisu(m, x, p):
    z = m^x % p
    return z

#procedura weryfikacji podpisu
#wejscie - liczba pierwsza p, wiadomosc m, g, podpisy x i X
#wyjscie - brak(werdykt czy poprawny podpis)

def weryfikacja_podpisu(p, m, g, x, X):
    a, b, c = stronaB_krok1(p, m, g)
    s1, s2, q = stronaA_krok1(p, g, c, x)
    print("\t3. Tu B, wysyłam a i b do A: ", a, b)
    print("\t4. Tu A, wysyłam q do B: ", q)
    s_1, s_2 = stronaB_krok2(c, g, a, b, q, p, m, X, x)
    print("\t   Tu B, obliczylem: s_1, s_2: ", s_1, s_2)
    print("sprawdzanie poprawnosci podpisu...")
    if(s1 == s_1 and s2 == s_2):
        print("podpis poprawny")
    else:
        print("podpis nie jest poprawny")

#procedura realizujaca krok pierwszy protokolu weryfikacji podpisu ze strony A
#wejscie - p, g, c i x, wyliczone w kroku ze strony B
#wyjscie - obliczone wartosci weryfikujace s1, s2 oraz q

def stronaA_krok1(p, g, c, x):
    q = randint(2, p)
    s1 = c * g^q % p
    s2 = (c * g^q)^x % p
    print("\t2. wysylam s1 i s2:", s1, s2, " do B")
    return s1, s2, q

#procedura realizujaca krok pierwszy protokolu weryfikacji podpisu ze strony B
#wejscie - p, g, m, czyli liczba pierwsaz, g oraz wiadomosc m
#wyjscie - wylosowane wartosci a, b oraz policzone c, potrzebne do weryfikacji podpisu

def stronaB_krok1(p, m, g):
    a = randint(2, p)
    b = randint(2, p)
    c = m^a * g^b % p
    print("\t1. wysylam c:", c, " do A")
    return a, b, c

#procedura realizujaca krok drugi protokolu weryfikacji podpisu ze strony B
#wejscie - wszystkie wartosci potrzebne do wyliczenia wartosci weryfikujacych, tj: a, g, a, b, q, p, m, X, x
#wyjscie - s_1 i s_2 czyli wartosci potem weryfikujace podpis

def stronaB_krok2(c, g, a, b, q, p, m, X, x):
    z = m^x % p
    s_1 = c * g^q % p
    s_2 = (X)^(b+q) * z^a % p
    return s_1, s_2

#procedura realizaujaca obsluge protokolu

def main():
    #krok 1 
    print("krok 1, generowanie kluczy\n")
    m = 123456 #tajemnica m
    p, g, x, X = generowanie_kluczy()
    print("\tp: ", p)
    print("\tnwd x i", p - 1, "=", gcd(x, p - 1)) #nwd liczb wylosowanych
    print("\tx: ", x)
    print ("\tX: ", X, "\n")

    #krok 2
    print("krok 2, generowanie podpisu\n")
    z = generacja_podpisu(m, x, p)
    print ("\tpodpis z:", z, "\n")

    #krok 3
    print("krok 3, weryfikacja podpisu\n")
    weryfikacja_podpisu(p, m, g, x, X)

main()