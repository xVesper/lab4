# plik = open(nazwa,tryb_otwarcia,bufor)
# plik = open("C:/Users/Admin/Desktop/lab4.txt","r")
#
# znaki = plik.read(10)
#
# linia = plik.readline()
#
# linie = plik.readlines()
#
# plik.close()
#
# print(znaki)
#
# print(linia)
#
# print(type(linie))

# plik = open("dane.txt","w+",encoding="utf8")
#
# dane = input("podaj kierunek studniow rok i specjalizacje")
# plik.write(dane)
#
# plik.close()
#
# lista = []
# for a in range(6):
#     lista.append(a)
#
# plik = open("dane.txt","e+",encoding="utf8")
#
# plik.writelines(str(lista))
#
# plik.close()

# with open("lab4.txt","r") as plik:
#     for linia in plik:
#         print(linia,end="")

# class PierwszaKlasa():
#     """Jest to pierwsza klasa w pytonie"""
#     atrybut = 54321
#     def pierwsza_metoda(self):
#         return "Teraz działa pierwsza metoda"
#
# obiekt = PierwszaKlasa()
# print(obiekt.atrybut)
# print(obiekt.pierwsza_metoda())
#
# obiekt.tekst = "abcde"
# print(obiekt.tekst)
#
# nowy_obiekt = PierwszaKlasa
# print(nowy_obiekt.atrybut)

# class Ksztalt():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.opis = "To będzie dla ogólnych kształtów"
#
#     def pole(self):
#         return self.x * self.y
#
#     def obwod(self):
#         return 2 * self.x + 2 * self.y
#
#     def dodaj_opis(self, czynnik):
#         self.x = self.x * czynnik
#         self.y = self.y * czynnik
#
#     def zmieniam_tekst(self, tekst):
#         tekst += "to jest"
#         return tekst
#
# prostokat = Ksztalt(10, 30)
# print(prostokat.pole())
# print(prostokat.obwod())
# print(prostokat.opis)
#
# prostokat.dodaj_opis("Prostokat")
# print(prostokat.opis)
#
# prostokat.skalowanie(0.5)
# print(prostokat.x)
# print(prostokat.y)
#
# print(prostokat.pole())
#
# print(prostokat.__zmiena_prywatna__)
#
# prostokat.__zmiena_prywatna__ = "aaaa"
# print(prostokat.__zmiena_prywatna__)
#
# print(prostokat.zmieniam_tekst(prostokat.__zmiena_prywatna__))