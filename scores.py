scores = [78, 92, 65, 88, 100, 54, 91, 73]
cem=0
for i in scores:
    cem+=i
print("Cəmi:", cem)

orta_bal=cem/len(scores)
print("Orta bal:", orta_bal)

say=0
for a in scores:
    if a>=90:
        say+=1
print("90 və yuxarı bal alanların sayı:", say)    

en_yuksek = scores[0] 
for x in scores:
  if x > en_yuksek:
    en_yuksek = x

print("Ən yüksək bal:", en_yuksek)