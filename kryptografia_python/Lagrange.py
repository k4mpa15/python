#Kampa Agnieszka WCY21KY1S1 zadanie 3a
import random

#funkcja main relizujaca obsluge protokolu

def main():
    #krok 1
    print("krok 1")
    print("\twybieram liczbe pierwsza p, spelniajaca zalozenia: ")
    n = 5 #liczba osob
    k = 5
    M = 123456 #tajemnica M
    p = 0
    while (is_prime(p) and p > M and p > n) == False:
        p = randint(2,2000000)
    print("\t", p)
    print("\ttajemnica:", M)
    #krok 2 i 3
    punkty = generowanie_cieni(M, n, k, p)

    #krok 4
    print("krok 4")
    print("\twysylanie cieni: ")
    for _ in range(n):
        print("\twysylam do", _ + 1 ,"osoby: punkt -", punkty[_], "\tliczba p -", p)

    tajemnica = odzyskiwanie_tajemnicy(punkty, p, k, n)
    print("\todzyskana tajemnica:", tajemnica)

#funkcja generujaca cienie
#wejscie - tajemnica M, ilosc uczestnikow n, ilosc cieni k
#wyjscie - cienie

def generowanie_cieni(M, n, k, p):
    #krok 2
    print("krok 2")
    print("\tgenerowanie wielomianu")
    C = GF(p) #ciao
    wspolczynniki = []#tablicawspolczynnikow
    for i in range(5):
        wspolczynniki.append(C.random_element())

    wspolczynniki[0] = M #nadpisanie tajemnica wyrazu wolnego

    P.<x>=C[] #generowanie pierscienia wielomianow nad cialem C

    f = wspolczynniki[4]*x**4 + wspolczynniki[3]*x**3 + wspolczynniki[2]*x**2 + wspolczynniki[1]*x**1 + wspolczynniki[0] #deklaracja wielomianu
    wspolczynniki = [] #wspolczynniki sa zapominane
    print("\twygenerwany wielomian:")
    print("\t", f)
    print("krok 3")
    print("\tgenerowanie cieni")

    punkty = []
    print("\twygenerowane 5 cieni: ")
    for i in range(1, n + 1):
        y = f(i)
        print("\t", y)
        punkty.append(y)
    return punkty

#odzyskiwanie tajemnicy
#wejscie- cienie, ilosc uczestnikow n, ilosc cieni k, liczba pierwsza p
#wyjscie - tajemnica

def odzyskiwanie_tajemnicy(cienie, p, k, n):
    #krok 5
    print("krok 5")
    print("\todzyskiwanie tajemnicy")
    C = GF(p) #ciało
    P.<x> = C[] #pierścień wielomianów nad ciałem C

    tajemnica = 0
    for i in range(len(cienie)):
        licznik = 1
        for j in range(len(cienie)):
            if i != j:
                licznik *= (x - (j + 1)) / ((i + 1) - (j + 1))
        tajemnica += cienie[i].lift() * licznik
        wiadomosc = tajemnica(0)
    return wiadomosc

main()