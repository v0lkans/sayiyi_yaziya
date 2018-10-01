# -*-coding:utf8;-*-

import time
import sys
import os
from deger__ebol import degeribol as db
# sys.path.append('C://Users//user//Desktop//Gereksiz//Python')

birler = {'0': '',
          '1': 'bir',
          '2': 'iki',
          '3': 'üç',
          '4': 'dört',
          '5': 'beş',
          '6': 'altı',
          '7': 'yedi',
          '8': 'sekiz',
          '9': 'dokuz'}


onlar = {'0': '',
         '1': 'on',
         '2': 'yirmi',
         '3': 'otuz',
         '4': 'kırk',
         '5': 'elli',
         '6': 'altmış',
         '7': 'yetmiş',
         '8': 'seksen',
         '9': 'doksan'}


yüzler = {'0': '',
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
        self.sira = [birler, onlar, yüzler]

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
