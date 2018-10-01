import sys
import os
from num2word import num2word
# sys.path.append(r'C:\Users\user\Desktop\Gereksiz\Python')

# for i in range((999)+1):
#     a = num2word('asd0').bastir()
#     print(a)


class bu():
    def __init__(self):
        os.system('cls||clear')
        print('Sayı: ', end='')
        while True:
            self.sayi = str(input())
            print('\x1b[4B', end='')
            self.temizle(5)

            self.okunus = num2word(self.sayi).bastir()
            try:
                self.sayiAyrilmis = format(int(self.sayi.replace('.', '')), ',')
            except ValueError:
                bu()

            self.taslak = "Sayı: \n{}\n{}".format(
                self.sayiAyrilmis, self.okunus)

            print(self.taslak)
            print('      \x1b[6A', end='')

    def temizle(self, tkrr):
        for i in range(tkrr):
            print('\x1b[1A', end='')
            print('\x1b[2K', end='')


bu()
