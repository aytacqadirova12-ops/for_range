metn = input("Söz və ya cümlə daxil edin: ")

saitler = "aəeıioöuüAƏEİOÖUÜ"

say = 0

for i in metn:
  if i in saitler:
    say += 1

print("Mətndəki saitlərin sayı:", say)