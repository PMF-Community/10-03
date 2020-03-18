#!/usr/bin/env python
#-*-coding:utf-8 -*-
#uneseniBodovi = uB
uB1 = int(input('Unesi osvojene bodove na vjezbama: '))
uB2 = int(input('Unesi osvojene bodove na parcijalnim ispitima: '))
uB3 = int(input('Unesi osvojene bodove na zavrsnom ispitu: '))

#sumaBodova = sB
sB=uB1+uB2+uB2
#pitati starog zasto ne radi
#debug and add Bosnian characters
if sB >= 95 & sB <= 100:
    print('10')
elif sB >= 85 & sB <= 94:
    print('9')
elif sB >= 75 & sB <= 84:
    print('8')
elif sB >= 65 & sB <= 74:
    print('7')
elif sB >= 55 & sB <= 64:
    print('6')
else:
    print('5')
