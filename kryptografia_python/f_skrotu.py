#Agnieszka Kampa WCY21KY1S1 zadanie 2a

import hashlib
import hmac
import binascii
import random

#wspolny klucz tajny K
K = "123ABC"

#procedura losowania rand_a
#wejście - brak
#wyjście Rand_A - randomwoa liczba wybrana przez strone A

def strona_A():
    Rand_A = random.randint(2, 20)
    return Rand_A

#procedura losowania rand_b
#wejście - brak
#wyjście - Rand_A - randomwoa liczba wybrana przez strone B

def strona_B():
    Rand_B = random.randint(2, 20)
    return Rand_B

#procedura liczaca funkcje skrotu HMAC
#wejscie - rand_a, rand_b, nr strony protokołu, tajny klucz K
#wyjście - funkcja skrótu
#używany jest też wspólny klucz

def H_MAC(Rand_A, Rand_B, strona, K):
    keyh = binascii.unhexlify(K)
    liczba = str(Rand_A) + str(Rand_B) + str(strona)
    hhmac= hmac.new(keyh,liczba.encode(),hashlib.sha3_512)
    hhmacout = hhmac.hexdigest()
    return str(hhmacout)

#procedura liczaca funkcje skrotu HMAC
#wejscie - rand_b, nr strony protokołu, tajny klucz K
#wyjście - funkcja skrótu
#używany jest też wspólny klucz

def H_MAC2(Rand_B, strona, K):
    keyh = binascii.unhexlify(K)
    liczba = str(Rand_B) + str(strona)
    hhmac= hmac.new(keyh,liczba.encode(),hashlib.sha3_512)
    hhmacout = hhmac.hexdigest()
    return str(hhmacout)

#procedura sprawdzajaca czy skroty sa takie same
#wejscie - skroty policzone przez obydwie strony
def sprawdzenie(skrot_A, skrot_B):
    if skrot_A == skrot_B:
        print("klucze sie zgadzaja")
    else:
        print("klucze sa rozne")

#funkcja glowna main realizujaca protokol

def main():
    print ("realizacja protokolu: ")
    print ("KROK 1 ")
    print("wartosci wygenerowane w kroku 1: ")
    Rand_A = strona_A()
    print("wartosc losowa A: ", Rand_A)
    print("\n")
    
    print ("KROK 2 ")
    print("wartosci wygenerowane w kroku 2: ")
    Rand_B = strona_B()
    print("wartosc losowa B: ",Rand_B)

    skrot_B = H_MAC(Rand_A, Rand_B, 2, K)
    print("skrot policzony przez strone B: ", skrot_B)
    print("\n")
    
    print ("KROK 3 ")
    print("wartosci wygenerowane w kroku 3: ")
    skrot_A = H_MAC(Rand_A, Rand_B, 2, K)
    print("skrot policzony przez strone A: ", skrot_A)
    print("\n")
    sprawdzenie(skrot_A, skrot_B)
    print("\n")
    skrot_A2 = H_MAC2(Rand_B, 1, K)
    print("skrot policzony przez strone A: ", skrot_A2)
    print("\n")
    
    print ("KROK 4 ")
    print("wartosci wygenerowane w kroku 4: ")
    skrot_B2 = H_MAC2(Rand_B, 1, K)
    print("skrot policzony przez strone B: ", skrot_B2)
    print("\n")
    sprawdzenie(skrot_A2, skrot_B2)
main()