'''
Napisz klasę Data reprezentującą datę (rok, miesiąc, dzień) w kalendarzu gregoriańskim (czyli używanym przez nas obecnie).

Obiekty typu Data można konstruować podając w argumentach właśnie rok, miesiąc i dzień jako argumenty nazwane (nazwy argumentów to rok, miesiac i dzien). Zadane argumenty muszą opisywać poprawną datę (załóż, że numeracja lat zaczyna się od 1). Jeżeli argumenty nie są poprawne to wyrzucany jest odpowiedni wyjątek (TypeError lub ValueError)
W klasie zdefiniowane mają być następujące metody:

__eq__ — porównanie dat,

__repr__ — zwraca napis w postaci 'Data(rok=1990, miesiac=10, dzien=5)',

__str__ — zwraca napis w formacie rrrr-mm-dd, np. '1990-10-05' (rok zawsze wyświetlany jest z użyciem czterech cyfr, a miesiąc i dzień — dwóch, liczby uzupełniane są w razie potrzeby od lewej strony zerami)

reprezentacja — zwraca napis w formacie zadanym argumentami separator i od_roku; argument logiczny od_roku przekazuje informację o tym, czy data ma być wyświetlona w kolejności rok–miesiąc–dzień (wartość domyślna – True) czy odwrotnej (czyli dzień–miesiąc–rok); argument separator oznacza napis rozdzielający elementy daty; elementy również wyświetlane są odpowiednio z użyciem czterech (rok) lub dwóch (miesiąc, dzień) cyfr

dzien_roku — zwraca numer dnia w roku,

dzien_tygodnia — zwraca napis określający dzień tygodnia, np. 'poniedziałek', 'wtorek', ...; przydatne wzory można znaleźć tutaj,
nastepny_dzien — zwraca kolejny dzień (jako obiekt typu Data);

poprzedni_dzien — analogicznie do poprzedniej metody, ale zwraca dzień poprzedzający; dla obiektu reprezentującego 1 stycznia 1 roku metoda zgłasza wyjątek ValueError.
'''

class Data:
    def __init__(self, *,rok, miesiac, dzien):
        if not isinstance(rok,int) or not isinstance(miesiac,int) or not isinstance(dzien,int):
            raise ValueError('rok, miesiac i dzień muszą być typu int')
        if rok<1 or miesiac>12 or miesiac<1 or dzien<1:
            raise ValueError('błędna data')
        elif miesiac in [4,6,9,11] and dzien>30:
            raise ValueError('błędna data')
        elif miesiac in [1,3,5,7,8,10,12] and dzien>31:
            raise ValueError('błędna data')
        if rok%4==0 and miesiac==2 and dzien>29:
            if rok%100==0 and miesiac==2 and dzien>28:
                if rok%400==0 and miesiac==2 and dzien>29:
                    raise ValueError('błędna data')
                elif miesiac==2 and dzien>28:
                    raise ValueError('błędna data')
            elif miesiac==2 and dzien>29:
                raise ValueError('błędna data')
        elif miesiac==2 and dzien>28:
            raise ValueError('błędna data')
        
                
        self.__rok=rok
        self.__miesiac=miesiac
        self.__dzien=dzien
        
    @property
    def rok(self):
        return self.__rok
    @property
    def miesiac(self):
        return self.__miesiac
    @property
    def dzien(self):
        return self.__dzien
        
    def __eq__(self, dat):
        return self.rok == dat.rok and self.miesiac==dat.miesiac and self.dzien==dat.dzien
    
    def __repr__(self):
        return "Data(rok={}, miesiac={}, dzien={})".format(self.rok, self.miesiac, self.dzien)
   
    def __str__(self):
        return "{:04}-{:02}-{:02}".format(self.rok, self.miesiac, self.dzien)
    
    def reprezentacja(self, seperator='-', od_roku=True):
        if od_roku==False:
            print(str(self.dzien)+seperator+str(self.miesiac)+seperator+str(self.rok))
        else:
            print(str(self.rok)+seperator+str(self.miesiac)+seperator+str(self.dzien))
    
    def dzien_roku(self):
        i=range(self.miesiac)
        numer_dnia=0
        for x in i:
            if x in [4,6,9,11]:
                numer_dnia=numer_dnia+30
            elif x in [1,3,5,7,8,10,12]:
                numer_dnia=numer_dnia+31
            elif x==2:
                if self.rok % 4 == 0:
                    if self.rok % 100 == 0:
                        if self.rok % 400 == 0:
                            numer_dnia=numer_dnia+29
                        else:
                            numer_dnia=numer_dnia+28
                    else:
                        numer_dnia=numer_dnia+29
                else:
                    numer_dnia=numer_dnia+28
        numer_dnia+=self.dzien
        return numer_dnia
    
    def dzien_tygodnia(self):
        a=(14-self.miesiac)//12
        y=self.rok-a
        m=self.miesiac+12*a-2
        liczba_dnia=(self.dzien+y+(y//4)-(y//100)+(y//400)+((31*m)//12))%7
        if liczba_dnia==0:
            return 'niedziela'
        elif liczba_dnia==1:
            return 'poniedziałek'
        elif liczba_dnia==2:
            return 'wtorek'
        elif liczba_dnia==3:
            return 'środa'
        elif liczba_dnia==4:
            return 'czwartke'
        elif liczba_dnia==5:
            return 'piątek'
        elif liczba_dnia==6:
            return 'sobota'
        
    def nastepny_dzien(self):
        if self.miesiac in [4,6,9,11]:
            if self.dzien==30:
                d=1
                m=self.miesiac+1
            else:
                d=self.dzien+1
                m=self.miesiac
            return Data(rok=self.rok, miesiac=m, dzien=d)
        elif self.miesiac in [1,3,5,7,8,10]:
            if self.dzien==31:
                d=1
                m=self.miesiac+1
            else:
                d=self.dzien+1
                m=self.miesiac
            return Data(rok=self.rok, miesiac=m, dzien=d)
        elif self.miesiac==12:
            if self.dzien==31:
                d=1
                m=1
                r=self.rok+1
            else:
                d=self.dzien+1
                m=self.miesiac
                r=self.rok
            return Data(rok=r, miesiac=m, dzien=d)
        elif self.miesiac==2:
            if self.dzien<27:
                d=self.dzien+1
                m=self.miesiac
            elif self.dzien==28:
                if self.rok % 4 == 0:
                    if self.rok % 100 == 0:
                        if self.rok % 400 == 0:
                            d=1
                            m=self.miesiac
                        else:
                            d=1
                            m=self.miesiac+1
                    else:
                        d=1
                        m=self.miesiac
                else:
                    d=1
                    m=self.miesiac+1
            elif self.dzien==29:
                d=1
                m=self.miesiac+1
            return Data(rok=self.rok, miesiac=m, dzien=d)
        
    def poprzedni_dzien(self):
        if self.rok==1 and self.miesiac==1 and self.dzien==1:
            raise ValueError('Nie można wskazać porzedniego dnia')            
        elif self.miesiac in [2,4,6,8,9,11]:
            if self.dzien==1:
                d=31
                m=self.miesiac-1
            else:
                d=self.dzien-1
                m=self.miesiac
            return Data(rok=self.rok, miesiac=m, dzien=d)
        elif self.miesiac in [5,7,10,12]:
            if self.dzien==1:
                d=30
                m=self.miesiac-1
            else:
                d=self.dzien-1
                m=self.miesiac
            return Data(rok=self.rok, miesiac=m, dzien=d)
        elif self.miesiac==1:
            if self.dzien==1:
                d=31
                m=12
                r=self.rok-1
            else:
                d=self.dzien-1
                m=self.miesiac
                r=self.rok
            return Data(rok=r, miesiac=m, dzien=d)
        elif self.miesiac==3:
            if self.dzien!=1:
                d=self.dzien-1
                m=self.miesiac
            elif self.dzien==1:
                if self.rok % 4 == 0:
                    if self.rok % 100 == 0:
                        if self.rok % 400 == 0:
                            d=29
                            m=self.miesiac-1
                        else:
                            d=28
                            m=self.miesiac-1
                    else:
                        d=29
                        m=self.miesiac-1
                else:
                    d=28
                    m=self.miesiac-1
            return Data(rok=self.rok, miesiac=m, dzien=d)
            
        
    
                        
                        
                   
                
            
