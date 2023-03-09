#apisz program, który wyświetli informację o tym ile plików z zadanego przez użytkownika katalogu ma jakie rozszerzenie. Pliki bez rozszerzenia i katalogi są pomijane.

import os
import os.path

katalog= input('Podaj nazwę katalogu: ')
lista_roz={}

for plik in os.listdir(katalog):
    if not os.path.isdir(plik):
        rozszerzenie = os.path.splitext(plik)[1]
        if rozszerzenie:
            if rozszerzenie in lista_roz:
                lista_roz[rozszerzenie] +=1
            else:
                lista_roz[rozszerzenie]=1
print(lista_roz)
