'''
Przed świętami trzeba zapakować prezenty. Potrzebny do tego jest papier i wstążka. Wszystkie prezenty zapakowane są w prostopadłościenne pudełka — do opisu ich wymiarów potrzebne są trzy liczby: szerokość, wysokość i długość w centymetrach.
Ilość papieru potrzebnego do zapakowania prezentu równa jest polu powierzchni pudełka powiększonej o powierzchnię najmniejszej ściany. Np. do zapakowania pudełka o wymiarach w centymetrach 2 x 3 x 4 ilość potrzebnego papieru wynosi 2 x (6 + 12 + 8) + 6 = 58 centymetrów kwadratowych.
Ilość wstążki potrzebnej do zawiązania prezentu równa jest obwodowi najmniejszej ściany. Dodatkowo trzeba zrobić kokardę. Liczba centymetrów potrzebna na kokardę równa liczbie centymetrów sześciennych objętości pudełka. Np. dla pudełka o wymiarach w centymetrach 2 x 3 x 4 ilość wstążki potrzebnej do zawiązania prezentu wynosi 2 x (2 + 3) = 10. Ilość wstążki potrzebnej na kokardę wynosi 2 x 3 x 4 = 24 centymetrów. Łącznie potrzebne są 34 centymetry wstążki.
Napisz klasę Prezent ułatwiającą policzenie ilości potrzebnego papieru i wstążki. Klasa ma następujące składowe:

metoda __init__ — podczas tworzenia obiektu potrzebna jest jego nazwa (napis) oraz szerokość, wysokość i długość wyrażone w centymetrach. Jeżeli nie zostanie podana długość, to jest ona równa wysokości, a jeżeli nie zostanie podana również wysokość, to jest ona równa szerokości.

pola nazwa, szerokosc, wysokosc oraz dlugosc,

właściwości papier i wstazka i dlugosc — wyłącznie do odczytu — zwracają odpowiednio ilość potrzebnych do opakowania prezentu papieru i wstążki.

metoda __repr__ — zwraca napis opisujący obiekt w postaci "Prezent('skarpety', 3, 4, 5)". W napisie tym uwzględnione są zawsze wysokość i długość niezależnie od tego, czy zostały one podane podczas tworzenia obiektu.

Napisz funkcję opakuj dostającą w kolejnych argumentach prezenty do opakowania (obiekty klasy Prezent). Dodatkowo funkcja może otrzymać dwa argumenty nazwane: papier i wstazka oznaczające odpowiednio ilość dostępnego papieru i wstążki. Jeżeli nie jest podana ilość papieru, to oznacza to, że dostępna jest dowolna jego ilość. Tak samo dla wstążki. Prezenty opakowywane są w kolejności przekazania ich w argumentach i opakowywane są dopóki wystarcza papieru i wstążki.
Funkcja zwraza trójelementową krotkę. Kolejne elementy krotki zawierają:

listę nazw opakowanych prezentów (w kolejności opakowywania),
ilość zużytego papieru
ilość zużytej wstążki

'''



class Prezent:
    def __init__(self, nazwa, szerokosc, wysokosc=None, dlugosc=None):
        if not isinstance(nazwa,str):
            raise ValueError('Zmienna nazwa nie jest napisem')
        self.nazwa=nazwa
        if dlugosc==None and wysokosc==None:
            dlugosc=szerokosc
            wysokosc=szerokosc
        elif dlugosc==None:
            dlugosc=wysokosc
        if not isinstance(szerokosc, (int,float)) and isinstance(wysokosc, (int,float))and isinstance(dlugosc, (int,float)):
            raise ValueError('Zmienna szerokosc, dlugosc i wysokosc musza byc typu float lub int')
        self.__dlugosc=dlugosc
        self.wysokosc=wysokosc
        self.szerokosc=szerokosc
        self.__papier=2*((self.dlugosc*self.wysokosc)+(self.wysokosc*self.szerokosc)+(self.szerokosc*self.dlugosc))+min((self.dlugosc*self.wysokosc),(self.wysokosc*self.szerokosc),(self.szerokosc*self.dlugosc))
        self.__wstazka=(2*(min(self.szerokosc,self.wysokosc)+min(self.wysokosc,self.dlugosc)))+(self.dlugosc*self.szerokosc*self.wysokosc)
    
    
        
    @property
    def papier(self):
        return self.__papier
    
    @property
    def wstazka(self):
        return self.__wstazka
       
    @property 
    def dlugosc(self):
        return self.__dlugosc
    
    def __repr__(self):
        return 'Prezent(%s, %s, %s, %s)' % (self.nazwa, self.szerokosc, self.wysokosc, self.dlugosc)
    
    
def opakuj(*prezenty, papier=None, wstazka=None):
    if papier==None and wstazka==None:
        pap=0
        wsta=0
        nazwa=[]
        for x in prezenty:
            pap=pap+x.papier
            wsta=wsta+x.wstazka
            nazwa.append(x.nazwa)
    elif not papier==None:
        pap=0
        wsta=0
        nazwa=[]
        for x in prezenty:
            if x.papier<=papier:
                pap=pap+x.papier
                wsta=wsta+x.wstazka
                papier=papier-x.papier
                nazwa.append(x.nazwa) 
    elif not wstazka==None:
            pap=0
            wsta=0
            nazwa=[]
            for x in prezenty:
                if x.wstazka<=wstazka:
                    pap=pap+x.papier
                    wsta=wsta+x.wstazka
                    wstazka=wstazka-x.wstazka
                    nazwa.append(x.nazwa) 
    elif wstazka!=None and papier!=None:
            pap=0
            wsta=0
            nazwa=[]
            for x in prezenty:
                if x.wstazka<=wstazka:
                    if x.papier<=papier:
                        pap=pap+x.papier
                        wsta=wsta+x.wstazka
                        wstazka=wstazka-x.wstazka
                        papier=papier-x.papier
                        nazwa.append(x.nazwa) 
    wynik=(list(nazwa), pap, wsta)
    return wynik