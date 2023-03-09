class Uczen:
    def __init__(self, imie, nazwisko):
        if not (isinstance(imie, str) and isinstance(nazwisko, str)): #sprawdzenie czy imie i nazwisko jest napisem
            raise ValueError('Imie i nazwisko nie są tekstem')
        self.__imie=imie
        self.__nazwisko=nazwisko
        self.oceny=[]
        self.__ocena_koncowa=None #uczeń nie ma jeszcze wystawionej oceny
    
    #imie , nazwisko i ocena końcowa tylko do odczytu, użytkownik nie może sam jej zmienić 
    @property
    def imie(self):
        return self.__imie
    
    @property
    def nazwisko(self):
        return self.__nazwisko
    
    @property
    def ocena_koncowa(self):
        return self.__ocena_koncowa
    
    #wstawianie ocen uczniowi    
    def wstaw_ocene(self, nowa_ocena):
        if self.ocena_koncowa==None: #sprawdzenie czy uczeń nie ma wystawionej oceny 
            self.oceny.append(nowa_ocena)
        else:
            raise TypeError('Nie możan wstawić oceny, gdy jest wystawiona ocena końcowa')
    
    #obliczanie redniej z wstawionych ocen
    def srednia(self):
        return sum(self.oceny)/len(self.oceny)
    
    #sprawdzenie czy uceń jest klasyfikowany
    def czy_klasyfikowany(self):
        return self.oceny!=[] #uczeń jest nieklasyfikowany gdy nie ma ocen 
    
    #wystawienie uczniowi oceny na podstawie redniej z ocen 
    def wystaw_ocene_koncowa(self):
        if self.oceny==[]:
            self.__ocena_koncowa='Uczeń nieklasyfikowany'
        else: #jeli oceny nie są puste to program wystawi ocenę uczniowi ze sredniej
            self.__ocena_koncowa=int(round((sum(self.oceny)/len(self.oceny)),0))
    
    def podwyzsz_ocene(self):
        if self.__ocena_koncowa>=1 and self.__ocena_koncowa<6: #sprwdzenie czy ocena końcowa jest większa od 1 i mniejsza od 6
            if int(round((sum(self.oceny)/len(self.oceny)),0)) == self.__ocena_koncowa: #sprawdzenie czy ocena nie była wczeniej podwyższona 
                self.__ocena_koncowa=self.__ocena_koncowa + 1
            else:
                raise ValueError('Nie można podwyższyć 6')
        else:
            raise TypeError('Nie możan podwyższyć oceny uczniowi nieklasyfikowanemu')

class Przedmiot(Uczen):
    def __init__(self, przedmiot):
        self.uczen={}
        self.przedmiot=przedmiot
    
    def zapisz_ucznia(self, imie, nazwisko):
        a=len(self.uczen)+1 # nadanie następnego numeru uczniowi
        u=imie + ' ' + nazwisko #połączneie imienia i nazwiska w jeden napis
        self.uczen[a]= u #doadnie ucznia do słownika
                
    def info(self, numer): #odczytanie z numeru imienia i nazwiska
        return self.uczen[numer] 
            

        