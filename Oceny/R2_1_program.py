from R2_1_class_Tomasz_Krukowski import Uczen
from R2_1_class_Tomasz_Krukowski import Przedmiot

plik_dane=input('Proszę podaj nazwę pliku z danymi uczniów: ')
dane=open(plik_dane, 'r')
plik_oceny=input('Proszę podaj nazwę pliku w którym zanjdują się oceny: ')
oceny=open(plik_oceny, 'r')
plik_wynik=input('Proszę podaj nazwę pliku gdzie mam zapisać oceny końcowe: ')
with open(plik_wynik, 'w') as wyniki:
    nazwa_przedmiot=oceny.readline() #pobranie nazwy przedmiotu z pliku
    nazwa_przedmiot=Przedmiot(nazwa_przedmiot) #stworzenie klasy przedmiot
    linia=dane.readline()
    while linia!='':
        linia=linia.split()
        numer=linia[0]
        imie=linia[1]
        nazwisko=linia[2]
        uczen_klasa=Uczen(imie, nazwisko) # stworzenie klasy uczeń 
        uczen_przedmiot=nazwa_przedmiot.zapisz_ucznia(imie, nazwisko) #dodanie ucznia do przedmiotu
        wszystkie_oceny=oceny.readline() #podrabie ocen ucznia z pliku
        wszystkie_oceny=wszystkie_oceny[2:] #odczytanie ocen bez numerku ucznia
        wszystkie_oceny=wszystkie_oceny.rstrip() #usunięcie znaku następnej lini
        wszystkie_oceny=wszystkie_oceny.split(',') #konwersja ocen z str do listy 
        oceny_konw=[]
        for i in wszystkie_oceny: # zmiana np 1+ na 1.5
            if i==' 1+':
                oceny_konw.append(1.5)
            elif i==' 2+':
                oceny_konw.append(2.5)
            elif i==' 3+':
                oceny_konw.append(3.5)
            elif i==' 4+':
                oceny_konw.append(4.5)
            elif i==' 5+':
                oceny_konw.append(5.5)
            elif i=='':
                oceny_konw=[]
            else:
                oceny_konw.append(float(i)) #konwersja pozostał○ych ocen z str na float
        for x in oceny_konw: #dodanie oceny do klasy 
            uczen_klasa.wstaw_ocene(x) 
        
        print(uczen_klasa.imie + ' ' + uczen_klasa.nazwisko)
        uczen_klasa.wystaw_ocene_koncowa() #wystawienie uczniowi oceny
        print('Wypada ocena: ',uczen_klasa.ocena_koncowa)
        if isinstance(uczen_klasa.ocena_koncowa,int) and uczen_klasa.ocena_koncowa<6:
            ocena_wyzej=input('Czy chcesz poprawić ocenę? [tak/nie]: ')
            if ocena_wyzej=='tak': #podwyższenie oceny
                uczen_klasa.podwyzsz_ocene()
            print('Wystawiona ocena: ', uczen_klasa.ocena_koncowa)
        
        klawisz=input('Nacinij Enter ....')
        if uczen_klasa.czy_klasyfikowany()==True: #zapis do pliku
            print(numer, uczen_klasa.imie, uczen_klasa.nazwisko+',', 'ocena końcowa:',uczen_klasa.ocena_koncowa, file=wyniki)
        else:
             print(numer, uczen_klasa.imie, uczen_klasa.nazwisko+',', uczen_klasa.ocena_koncowa, file=wyniki)
        linia=dane.readline()    
dane.close()
oceny.close()

