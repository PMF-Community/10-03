#trocifrenBroj = tB
tB = int(input())
#srediti imena varijabli, tj skratiti
if tB >=100 & tB <=999:
    zadnjaCifra=tB%10
    dvocifrenBroj=tB//10
    predzadnjaCifra=dvocifrenBroj%10
    prvaCifraTrocifrenogBroja=dvocifrenBroj//10

rezultatMnozenjaCifara = zadnjaCifra * predzadnjaCifra * prvaCifraTrocifrenogBroja

print(rezultatMnozenjaCifara)
