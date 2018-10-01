def degeribol(bolunecek, kaca):
    if type(bolunecek) == list:
        bolunecek = bolunecek

    else:
        bolunecek = str(bolunecek)

    bolunmusDeger = []
    bolunecekUzunluk = len(bolunecek)

    a = -kaca
    b = 0

    for i in range((bolunecekUzunluk // kaca)+1):
        if i == 0:
            # bolunmusDeger.insert(0,bolunecek[a:])
            bolunmusDeger.append(bolunecek[a:])
        else:
            # bolunmusDeger.insert(0,bolunecek[a:b])
            bolunmusDeger.append(bolunecek[a:b])

        a -= kaca
        b -= kaca

        if bolunmusDeger[i] == '':
            del bolunmusDeger[i]

    bolunmusDeger = bolunmusDeger[::-1]
    if [] in bolunmusDeger:
        del bolunmusDeger[0]

    return bolunmusDeger


print(degeribol('12345678', 3))
