#Napisz prosty kalkulator umożliwiający wykonywanie działań (dodawanie, odejmowanie, mnożenie, dzielenie całkowite) na liczbach całkowitych.

import tkinter as tk

class Kalkulator(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.liczba1 = tk.StringVar()
        
        self.liczba2 = tk.StringVar()
        
        self.liczba1 = tk.Entry(self,width = 30, textvariable=self.liczba1)        
        self.liczba1.grid(column = 0, row = 0, columnspan = 4)
        
        self.liczba2 = tk.Entry(self,width = 30, textvariable=self.liczba2)         
        self.liczba2.grid(column = 0, row = 1, columnspan = 4)  
        
        self.przycisk = tk.Button(self, text = '+', command = self.dodawanie)
        self.przycisk.grid(column =0, row= 2, sticky = tk.E + tk.W)
        
        self.przycisk = tk.Button(self, text = '-', command = self.odejmowanie)
        self.przycisk.grid(column =1, row= 2, sticky = tk.E + tk.W)
        
        self.przycisk = tk.Button(self, text = '*', command = self.mnozenie)
        self.przycisk.grid(column =2, row= 2, sticky = tk.E + tk.W)
                        
        self.przycisk = tk.Button(self, text = '/', command = self.dzielenie)
        self.przycisk.grid(column =3, row= 2, sticky = tk.E + tk.W) 
        
        self.etykieta_wynik = tk.Label(self, text = 'Wynik: ')
        self.etykieta_widok = tk.Label(self)
        
        self.etykieta_wynik.grid(column = 0, row = 3, columnspan = 2)
        self.etykieta_widok.grid(column = 2, row = 3, columnspan = 2)
        
    def dodawanie(self):
        try:    
            a = self.liczba1.get()
            b = self.liczba2.get()        
            wynik = int(a) + int(b)
            self.etykieta_widok.config(text = wynik)
        except ValueError:
            self.etykieta_widok.config(text = 'Error')

    def odejmowanie(self):
        try:
            a = self.liczba1.get()
            b = self.liczba2.get()        
            wynik = int(a) - int(b)
            self.etykieta_widok.config(text = wynik)
        except ValueError:
            self.etykieta_widok.config(text = 'Error')

    def mnozenie(self):
        try:    
            a = self.liczba1.get()
            b = self.liczba2.get()        
            wynik = int(a) * int(b)
            self.etykieta_widok.config(text = wynik)
        except ValueError:
            self.etykieta_widok.config(text = 'Error')

    def dzielenie(self):
        try:
            a = self.liczba1.get()
            b = self.liczba2.get()        
            wynik = int(a) / int(b)
            self.etykieta_widok.config(text = wynik)
        except (ValueError, ZeroDivisionError):
            self.etykieta_widok.config(text = 'Error')
            
def main():
    okno_glowne = tk.Tk()
    okno_glowne('Kalkulator')
    ramka = Kalkulator(okno_glowne)
    ramka.grid()
    okno_glowne.mainloop()
    
if __name__ == '__main__':
    main()

    