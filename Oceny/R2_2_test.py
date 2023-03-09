import unittest
from R2_1_class_Tomasz_Krukowski import Uczen

class UczenTest(unittest.TestCase):
    
    def test_init_imie(self):
        u1=Uczen('Anna', 'Nowak')
        self.assertEqual(u1.imie, 'Anna')

    def test_init_nazwisko(self):
        u1=Uczen('Anna', 'Nowak')
        self.assertEqual(u1.nazwisko, 'Nowak')
    
    def test_init_poprawnosc_imie(self):
        with self.assertRaises(ValueError):
            Uczen(20,'Nowak')
            
    def test_init_poprawnosc_nazwisko(self):
        with self.assertRaises(ValueError):
            Uczen('Anna',20)
    
    def test_do_odczytu_imie(self):
        with self.assertRaises(AttributeError):
            u1=Uczen('Anna','Nowak')
            u1.imie='Zofia'
            
    def test_do_odczytu_nazwisko(self):
        with self.assertRaises(AttributeError):
            u1=Uczen('Anna','Nowak')
            u1.nazwisko='Kowlaska' 
            
    def test_do_odczytu_ocena_koncowa(self):
        with self.assertRaises(AttributeError):
            u1=Uczen('Anna','Nowak')
            u1.ocena_koncowa=5
    
    def test_wstawiane_oceny(self):
        with self.assertRaises(TypeError):
            u1=Uczen('Anna','Nowak')
            u1.wstaw_ocene(4)
            u1.wstaw_ocene(4)
            u1.wystaw_ocene_koncowa()
            u1.wstaw_ocene(2)
    
    def test_wystaw_ocene(self):
        u1=Uczen('Anna', 'Nowak')
        u1.wstaw_ocene(3)
        self.assertEqual(u1.oceny, [3])
        
        
    def test_klasyfikacja_nie(self):
        u1=Uczen('Anna', 'Nowak')
        self.assertFalse(u1.czy_klasyfikowany())
    
    def test_klasyfikacja_tak(self):
        u1=Uczen('Anna', 'Nowak')
        u1.wstaw_ocene(5)
        self.assertTrue(u1.czy_klasyfikowany())
        
    def test_wystaw_ocene_koncowa_pozytywna(self):
        u1=Uczen('Anna','Nowak')
        u1.wstaw_ocene(4)
        u1.wstaw_ocene(4)
        u1.wystaw_ocene_koncowa()
        self.assertEqual(u1.ocena_koncowa, 4)
        
    def test_wystaw_ocene_koncowa_negatywna(self):
        u1=Uczen('Anna','Nowak')
        u1.wystaw_ocene_koncowa()
        self.assertEqual(u1.ocena_koncowa, 'Uczeń nieklasyfikowany')
         
    def test_podwyzsz_ocene_koncowa_4(self):
        u1=Uczen('Anna','Nowak')
        u1.wstaw_ocene(4)
        u1.wstaw_ocene(4)
        u1.wystaw_ocene_koncowa()
        u1.podwyzsz_ocene()
        self.assertEqual(u1.ocena_koncowa, 5)
        
    def test_podwyzsz_ocene_koncowa_6(self):
        with self.assertRaises(TypeError):
            u1=Uczen('Anna','Nowak')
            u1.wstaw_ocene(6)
            u1.wstaw_ocene(6)
            u1.wystaw_ocene_koncowa()
            u1.podwyzsz_ocene()
        
    def test_podwyzsz_ocene_koncowa_nieklasyfikowany(self):
        with self.assertRaises(TypeError):
            u1=Uczen('Anna','Nowak')
            u1.wystaw_ocene_koncowa()
            u1.podwyzsz_ocene()
            
if __name__ == "__main__":
    unittest.main()   