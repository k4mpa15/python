#Agnieszka Kampa WCY21KY1S1 zadanie 1a

from random import getrandbits


b = 50
#krok 1
#procedura generujaca parametry dziedziny
#wejscie: b - dlugosc w bitach
#wyjscie - p,n,g - parametry dziedziny

def generowanie_parametrow(b):
    p = 0 #zainicjowanie zmiennych, b to zmienna ktora zawiera dlugosc w bitach
    n = 0
    while (is_prime(p) and is_prime(n) and n > 3) == False: #sprawdzenie czy liczby p i n sa pierwsze
        p = getrandbits(b) #funkcja pozwalajaca wygenerowac liczbe o okreslonej dlugosci bitow
        n = int((p - 1)/2) #policzenie n dla sprawdzenia czy ejst pierwsze
    print("\tp: ", p, "n: ", n)
    F = GF(p) #iniciacja ciała F
    g = 0
    while g <= 0:
        while True:
            g = F.random_element() #wybranie randomowego elementu z ciala
            if g.multiplicative_order() == n: #rzad podgrupy
                break
    print("\tn: ", n)
    print("\tg^n: ", g^n)
    return p, n, g


#krok 2
#funkcja generujaca klucze
#wejscie - parametry dziedziny
#wyjscie - klucz publiczny i prywatny

def generowanie_kluczy(p, n, g):
    kpriv = randint(2, n - 1) #losuje liczbe z przedzialu 2 do n-1
    kpub = (g^kpriv)%p #generator do potegi kpriv modulo p
    return kpriv, kpub


#krok 3
#procedura wywolujaca generowanie kluczy dla strony A
#wejscie - parametry dziedziny p,n,g
#wyjscie - klucz publiczny i prywatny strony A

def stronaA(p, n, g):
    xa, KA = generowanie_kluczy(p, n, g)
    print("\txa: ", xa)
    print("\t\twysylam ", KA, " do strony B")
    return KA, xa


#procedura wywolujaca generowanie kluczy dla strony B
#wejscie - parametry dziedziny p,n,g
#wyjscie - klucz publiczny i prywatny strony B

def stronaB(p, n, g):
    xb, KB = generowanie_kluczy(p, n, g)
    print("\txb: ", xb)
    print("\t\twysylam ", KB, " do strony A")
    return KB, xb


#procedura liczaca klucz sesji ze strony A
#wejscie - klucz publiczny B i klucz prywatny A
#wyjscie - klucz sesji

def kluczA(KB, xa):
    K = KB^xa
    return K


#procedura liczaca klucz sesji ze strony B
#wejscie - klucz publiczny A i klucz prywatny B
#wyjscie - klucz sesji

def kluczB(KA, xb):
    K = KA^xb
    return K


#procedura sprawdzajaca czy klucze sa poprawne 
def sprawdzenie(K_testA, K_testB):
    if K_testA == K_testB:
        print("klucze sie zgadzaja")
    else:
        print("klucze sa rozne")



#funkcja glowna main realizujaca protokol

def main():
    print ("realizacja protokolu: ")
    print ("KROK 1 ")
    print("wartosci wygenerowane w kroku 1: ")
    p, n, g = generowanie_parametrow(b) #przypisanie wartosci zwroconych w funkcji
    print("KROK 2 ")
    print("wartosci wygenerowane w kroku 2 sa uzywane w kroku 3: ")
    print("KROK 3 ")
    KA, xa = stronaA(p, n, g)
    KB, xb = stronaB(p, n, g)
    print("klucze wygenerowane przez strony: ")
    K_testA = kluczA(KB, xa)
    print("\tK wygenerowane przez strone A: ", K_testA)
    K_testB = kluczB(KA, xb)
    print("\tK wygenerowane przez strone B: ", K_testB)
    print("sprawdzenie poprawnosci (czy klucze sa takie same):")
    sprawdzenie(K_testA, K_testB)
#wywolanie funkcji main
main()


