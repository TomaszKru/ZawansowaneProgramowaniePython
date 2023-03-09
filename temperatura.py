#Napisz program używający graficznego interfejsu użytkownika umożliwiający przeliczanie temperatur ze stopni Celsjusza na Fahrenheita i na odwrót.

import tkinter as tk

class Temperatura(tk.Frame):
    
    def __init__(self, root):
        super().__init__(root)
        
        self.celciusza = tk.StringVar()
        
        self.fahrenheita = tk.StringVar()
        
        
        self.celcjusz_pole = tk.Entry(self,width = 7, textvariable=self.celciusza)        
        self.celcjusz_pole.grid(column = 0, row = 0, rowspan=2, sticky = tk.N + tk.S)
        
        self.fahrenheita_pole = tk.Entry(self,width = 7, textvariable=self.fahrenheita)         
        self.fahrenheita_pole.grid(column = 3, row =0, rowspan=2, sticky = tk.N + tk.S)  
        
        
        self.przycisk = tk.Button(self, text = 'stopnie Celciusza na stopnie Fahrenheita ->', command = self.cel_na_fahre)
        self.przycisk.grid(column =1, row= 0)
        
        self.przycisk2 = tk.Button(self, text = '<- stopnie Fahrenheita na stopnie Celciusza ', command = self.fahre_na_cel)
        self.przycisk2.grid(column =1, row= 1)
        
    def cel_na_fahre(self):
        temp_cel=float(self.celciusza.get())
        if temp_cel<-273.15:
            tk.messagebox.showinfo('Uwaga!',"Temperatura poniżej zera bezwzględnego.")
            return
        temp_fahr=round((32+((9/5)*temp_cel)),2)
        self.fahrenheita.set(temp_fahr)
    
    def fahre_na_cel(self):
        temp_fahre=float(self.fahrenheita.get())
        if temp_fahre<-459.67:
            tk.messagebox.showinfo('Uwaga!',"Temperatura poniżej zera bezwzględnego.")
            return
        temp_celc=round(((5/9)*(temp_fahre-32)),2)
        self.celciusza.set(temp_celc)
    
    
def main():
    okno_glowne=tk.Tk()
    okno_glowne.title('Konwersja temperatur')
    ramka=Temperatura(okno_glowne)
    ramka.pack()
    okno_glowne.mainloop()
if __name__=='__main__':
    main()

