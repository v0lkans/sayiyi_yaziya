# -*-coding:utf8;-*-

import time
import sys
import os
sys.path.append('C://Users//user//Desktop//Gereksiz//Python')
from deger__ebol import degeribol as db

birler = binler = milyonlar = milyarlar = trilyonlar = katrilyonlar = kentilyonlar = seksilyonlar = septilyonlar =\
    oktilyonlar = nonilyonlar = desilyonlar = undesilyonlar = dodesilyonlar = tredesilyonlar = katordesilyonlar = \
    kendesilyonlar = seksdesilyonlar = septendesilyonlar = oktodesilyonlar = novemdesilyonlar = vigintilyonlar = \
    {'0': '',
     '1': 'bir',
     '2': 'iki',
     '3': 'üç',
     '4': 'dört',
     '5': 'beş',
     '6': 'altı',
     '7': 'yedi',
     '8': 'sekiz',
          '9': 'dokuz', }


onlar = onbinler = onmilyonlar = onmilyarlar = ontrilyonlar = onkatrilyonlar = onkentilyonlar = onseksilyonlar = \
    onseptilyonlar = onoktilyonlar = onnonilyonlar = ondesilyonlar = onundesilyonlar = ondodesilyonlar = \
    ontredesilyonlar = onkatordesilyonlar = onkendesilyonlar = onseksdesilyonlar = onseptendesilyonlar = \
    onoktodesilyonlar = onnovemdesilyonlar = onvigintilyonlar = \
    {'0': '',
          '1': 'on',
          '2': 'yirmi',
          '3': 'otuz',
          '4': 'kırk',
          '5': 'elli',
          '6': 'altmış',
          '7': 'yetmiş',
          '8': 'seksen',
          '9': 'doksan', }


yüzler = yüzbinler = yüzmilyonlar = yüzmilyarlar = yüztrilyonlar = yüzkatrilyonlar = yüzkentilyonlar = \
    yüzseksilyonlar = yüzseptilyonlar = yüzoktilyonlar = yüznonilyonlar = yüzdesilyonlar = yüzundesilyonlar = \
    yüzdodesilyonlar = yüztredesilyonlar = yüzkatordesilyonlar = yüzkendesilyonlar = yüzseksdesilyonlar = \
    yüzseptendesilyonlar = yüzoktodesilyonlar = yüznovemdesilyonlar = yüzvigintilyonlar = \
    {'0': '',
          '1': 'yüz',
          '2': 'ikiyüz',
          '3': 'üçyüz',
          '4': 'dörtyüz',
          '5': 'beşyüz',
          '6': 'altıyüz',
          '7': 'yediyüz',
          '8': 'sekizyüz',
          '9': 'dokuzyüz', }


bin_ek = 'bin'
milyon_ek = 'milyon'
milyar_ek = 'milyar'
trilyon_ek = 'trilyon'
katrilyon_ek = 'katrilyon'
kentilyon_ek = 'kentilyon'
seksilyon_ek = 'seksilyon'
septilyon_ek = 'septilyon'
oktilyon_ek = 'oktilyon'
nonilyon_ek = 'nonilyon'
desilyon_ek = 'desilyon'
undesilyon_ek = 'undesilyon'
dodesilyon_ek = 'dodesilyon'
tredesilyon_ek = 'tredesilyon'
katordesilyon_ek = 'katordesilyon'
kendesilyon_ek = 'kendesilyon'
sekdesilyon_ek = 'seksdesilyon'
septendesilyon_ek = 'septendesilyon'
oktodesilyon_ek = 'oktodesilyon'
novemdesilyon_ek = 'novemdesilyon'
vigintilyon_ek = 'vigintilyon'


class num2word():
    def __init__(self, sayi):
        self.sira = [birler, onlar, yüzler,
                     binler, onbinler, yüzbinler,
                     milyonlar, onmilyonlar, yüzmilyonlar,
                     milyarlar, onmilyarlar, yüzmilyarlar,
                     trilyonlar, ontrilyonlar, yüztrilyonlar,
                     katrilyonlar, onkatrilyonlar, yüzkatrilyonlar,
                     kentilyonlar, onkentilyonlar, yüzkentilyonlar,
                     seksilyonlar, onseksilyonlar, yüzseksilyonlar,
                     septilyonlar, onseptilyonlar, yüzseptilyonlar,
                     oktilyonlar, onoktilyonlar, yüzoktilyonlar,
                     nonilyonlar, onnonilyonlar, yüznonilyonlar,
                     desilyonlar, ondesilyonlar, yüzdesilyonlar,
                     undesilyonlar, onundesilyonlar, yüzundesilyonlar,
                     dodesilyonlar, ondodesilyonlar, yüzdodesilyonlar,
                     tredesilyonlar, ontredesilyonlar, yüztredesilyonlar,
                     katordesilyonlar, onkatrilyonlar, yüzkatordesilyonlar,
                     kendesilyonlar, onkendesilyonlar, yüzkendesilyonlar,
                     seksdesilyonlar, onseksdesilyonlar, yüzseksdesilyonlar,
                     septendesilyonlar, onseptendesilyonlar, yüzseptendesilyonlar,
                     oktodesilyonlar, onoktodesilyonlar, yüzoktodesilyonlar,
                     novemdesilyonlar, onnovemdesilyonlar, yüznovemdesilyonlar,
                     vigintilyonlar, onvigintilyonlar, yüzvigintilyonlar]

        # self.ekler_sira = [milyon_ek, milyar_ek, trilyon_ek, katrilyon_ek, kentilyon_ek, seksilyon_ek,
        #                    septilyon_ek, oktilyon_ek]

        self.ekler_sira = \
            [bin_ek,
             milyon_ek,
             milyar_ek,
             trilyon_ek,
             katrilyon_ek,
             kentilyon_ek,
             seksilyon_ek,
             septilyon_ek,
             oktilyon_ek,
             nonilyon_ek,
             desilyon_ek,
             undesilyon_ek,
             dodesilyon_ek,
             tredesilyon_ek,
             katordesilyon_ek,
             kendesilyon_ek,
             sekdesilyon_ek,
             septendesilyon_ek,
             oktodesilyon_ek,
             novemdesilyon_ek,
             vigintilyon_ek]

        try:
            sayi = str(sayi).replace('.', '')
            self.sayi = int(sayi)
            # self.sayi = str(sayi).replace('.','')
            # print(self.sayi)
        except ValueError:
            print('değer hatalı!', end='')
            sys.exit()
        else:
            self.sayi = str(self.sayi)

        self.sayiUzunluk = len(self.sayi)
        if self.sayiUzunluk >= len(self.sira)+1:
            print('sayı çok uzun! (sayı uzunluğu > {})'.format(
                str(len(self.sira)+1)), end='')
            sys.exit()
        self.ayir = []
        # self.sayi = self.sayi[::-1]
        self.sayiOkunusu = []
        self.sayiUzunlukMenzil = range(len(self.sayi))
        self._3ebol()

    def sayi_okunusu(self, _3ebolunmusSayi):
        # Sıranın doğru olması için
        tga = 0
        acvbn = 0
        for üceBölünenSayinin in _3ebolunmusSayi:
            for a in range(len(üceBölünenSayinin)):
                if int(self.sayi) == 0:  # Eğer sayı sıfırsa:
                    self.sayiOkunusu = ['sıfır']  # 'sıfır' bastır

                if acvbn == 3:
                    if üceBölünenSayinin == '000':
                        pass
                    elif üceBölünenSayinin == '001' or üceBölünenSayinin == '01' or üceBölünenSayinin == '1':
                        self.sayiOkunusu.insert(0, (bin_ek))
                    else:
                        self.sayiOkunusu.insert(0, (bin_ek))
                        self.sayiOkunusu.insert(
                            0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 6:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (milyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 9:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (milyar_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 12:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (trilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 15:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (katrilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 18:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (kentilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 21:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (seksilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 24:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (septilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 27:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (oktilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 30:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (nonilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 33:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (desilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 36:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (undesilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 39:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (dodesilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 42:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (tredesilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 45:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (katordesilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 48:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (kendesilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 51:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (sekdesilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 54:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (septendesilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 57:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (oktodesilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 60:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (novemdesilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                elif acvbn == 63:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(0, (vigintilyon_ek))
                    self.sayiOkunusu.insert(
                        0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                else:
                    if üceBölünenSayinin == '000' or üceBölünenSayinin == '00' or üceBölünenSayinin == '0':
                        pass
                    else:
                        self.sayiOkunusu.insert(
                            0, (self.sira[acvbn][üceBölünenSayinin[::-1][a]]))

                acvbn += 1
            # print([üceBölünenSayinin[::-1]]
        self.bastir()

    def bastir(self):
        self.SAYI_OKUNUSU = ''
        for asd in db(self.sayiOkunusu, 3):
            for dsa in asd:
                # "Sıfır" da oluşan fazla boşluğu silme
                end = ' '
                if dsa == '':
                    end = ''
                self.SAYI_OKUNUSU = self.SAYI_OKUNUSU + dsa + end
        return self.SAYI_OKUNUSU[:-1]

    def _3ebol(self):
        self._3lüsayi = db(self.sayi, 3)
        self._3lüsayi = self._3lüsayi[::-1]

        self.sayi_okunusu(self._3lüsayi)


# for i in range(8888):
#     App(i)
