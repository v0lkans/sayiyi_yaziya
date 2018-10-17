# -*-coding:utf8;-*-

from degeri_bol import degeri_bol


class sayi2yazi():
    def __init__(self, sayi, ARALIK=' '):
        self.SIFIR = 'sıfır'
        self.BIRLER = {'0': '',
                       '1': 'bir',
                       '2': 'iki',
                       '3': 'üç',
                       '4': 'dört',
                       '5': 'beş',
                       '6': 'altı',
                       '7': 'yedi',
                       '8': 'sekiz',
                       '9': 'dokuz'}

        self.ONLAR = {'0': '',
                      '1': 'on',
                      '2': 'yirmi',
                      '3': 'otuz',
                      '4': 'kırk',
                      '5': 'elli',
                      '6': 'altmış',
                      '7': 'yetmiş',
                      '8': 'seksen',
                      '9': 'doksan'}

        self.YUZLER = {'0': '',
                       '1': 'yüz',
                       '2': 'ikiyüz',
                       '3': 'üçyüz',
                       '4': 'dörtyüz',
                       '5': 'beşyüz',
                       '6': 'altıyüz',
                       '7': 'yediyüz',
                       '8': 'sekizyüz',
                       '9': 'dokuzyüz', }

        BIN_EK = 'bin'
        MILYON_EK = 'milyon'
        MILYAR_EK = 'milyar'
        TRILYON_EK = 'trilyon'
        KATRILYON_EK = 'katrilyon'
        KENTILYON_EK = 'kentilyon'
        SEKSILYON_EK = 'seksilyon'
        SEPTILYON_EK = 'septilyon'
        OKTILYON_EK = 'oktilyon'
        NONILYON_EK = 'nonilyon'
        DESILYON_EK = 'desilyon'
        UNDESILYON_EK = 'undesilyon'
        DODESILYON_EK = 'dodesilyon'
        TREDESILYON_EK = 'tredesilyon'
        KATORDESILYON_EK = 'katordesilyon'
        KENDESILYON_EK = 'kendesilyon'
        SEKDESILYON_EK = 'seksdesilyon'
        SEPTENDESILYON_EK = 'septendesilyon'
        OKTODESILYON_EK = 'oktodesilyon'
        NOVEMDESILYON_EK = 'novemdesilyon'
        VIGINTILYON_EK = 'vigintilyon'

        self.SIRA = [self.BIRLER, self.ONLAR, self.YUZLER]
        self.EKLER_SIRA = [
            BIN_EK,
            MILYON_EK,
            MILYAR_EK,
            TRILYON_EK,
            KATRILYON_EK,
            KENTILYON_EK,
            SEKSILYON_EK,
            SEPTILYON_EK,
            OKTILYON_EK,
            NONILYON_EK,
            DESILYON_EK,
            UNDESILYON_EK,
            DODESILYON_EK,
            TREDESILYON_EK,
            KATORDESILYON_EK,
            KENDESILYON_EK,
            SEKDESILYON_EK,
            SEPTENDESILYON_EK,
            OKTODESILYON_EK,
            NOVEMDESILYON_EK,
            VIGINTILYON_EK]

        self.SAYI_YAZIYA_CEVRILMIS = []
        self.sayi = int(sayi)
        self.ARALIK = ARALIK

        # Sayiyi 3'lü olarak ayırır.
        self.bolunmus_sayi = degeri_bol(self.sayi, 3)

    def rakamlari_duzenlenmis(self):
        """Sayı listesini yazıya doğru çevirmek için düzenler"""
        duzenlenmis = []

        for BOLUNMUS in self.bolunmus_sayi:

            # Rakamları tek tek almak için listeye çevir.
            BOLUNMUS = list(BOLUNMUS)

            if len(BOLUNMUS) < 3:
                for L in range(3 - len(BOLUNMUS)):
                    # Rakam listesinin uzunluğunu...
                    # ...3 yapmak ve için boş eleman ekler. (Değer önemli değil)
                    BOLUNMUS.insert(0, None)

            # if x is 0 or x is '0':
            #     print(x)
            # else:
            #     break

            duzenlenmis.append(BOLUNMUS)
        return duzenlenmis

    def rakamlari_yaziya_cevirilmis(self):
        cevirilmis = []

        for x in self.rakamlari_duzenlenmis():
            # print(x, self.rakamlari_duzenlenmis())

            YUZLER_SAYI_RAKAM = x[0]  # Basamaklarına ayırır.
            ONLAR_SAYI_RAKAM = x[1]  # Basamaklarına ayırır.
            BIRLER_SAYI_RAKAM = x[2]  # Basamaklarına ayırır.

            # Sayıların yazıya çevirilmiş hâlini listeye ekler.
            # Basamak eksikse, eksik basamak yerine None değerini ekler.
            cevirilmis.append([self.YUZLER.get(YUZLER_SAYI_RAKAM),
                               self.ONLAR.get(ONLAR_SAYI_RAKAM),
                               self.BIRLER.get(BIRLER_SAYI_RAKAM)])

            for x in cevirilmis:
                # cevirilmis.append() bloğunda oluşan None değerini siler.
                # print(x)

                for a in range(len(x)):
                    if None in x:
                        #  cevirilmis listesinde basamak değeri None ise siler.
                        del cevirilmis[cevirilmis.index(x)][x.index(None)]

        return cevirilmis  # Listeyi

    def ek_eklenmis(self):
        # ek_eklenmis = []
        liste = self.rakamlari_yaziya_cevirilmis()
        liste_uzunluk = len(self.rakamlari_yaziya_cevirilmis())

        # Ek ekler.
        for i in range(liste_uzunluk):
            if i is not 0:
                liste[::-1][i].append(self.EKLER_SIRA[i-1])

        # "bir bin" ifadesini, "bir"i silerek düzeltir.
        if len(str(self.sayi)) == 4:
            if str(self.sayi)[0] == '1':
                    del liste[0][0]

        # 'liste' içindeki listeleri birleştir ve tek liste yapar.

        x = [x for y in liste for x in y if x is not '']

        return self.ARALIK.join(x)

    # def hatalar_duzeltilmis(self):
    #     if len(str(self.sayi)) == 4:
    #         if str(self.sayi)[0] == '1':
    #             return self.ek_eklenmis()[4:]
    #     return self.ek_eklenmis()

    def __str__(self):
        return self.ek_eklenmis()
        # return self.hatalar_duzeltilmis()


if __name__ == '__main__':
    print(sayi2yazi('123', ARALIK=' '))
