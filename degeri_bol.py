def degeri_bol(BOL, KAC=3):
    if type(BOL) == list:
        # Listeyi str değerine çevirmemesi için
        pass
    else:
        BOL = str(BOL)

    bolunmus_deger = []
    BOL_UZUNLUK = len(BOL)

    for i in range((BOL_UZUNLUK // KAC)+1):
        bolunmus_deger.append(BOL[-KAC:])
        BOL = BOL[:-KAC]

        if bolunmus_deger[i] == '':
            del bolunmus_deger[i]
            # bolunmus_deger listesinin i. (i'inci) elemanı boş...
            # ...string ise boş stringi siler.

    bolunmus_deger = bolunmus_deger[::-1]  # Ters listeyi tekrar düz yapar.

    if type(BOL) == list:  # BOL liste ise
        if [] in bolunmus_deger:
            # bolunmus_deger listesinin 0. indexi boş liste ise boş listeyi sil.
            del bolunmus_deger[0]

    return bolunmus_deger
