p=input("Parol daxil edin: ")
upper=0
lower=0
digit=0
other=0
for i in p:
  if i.isupper():
    upper += 1
  elif i.islower():
    lower += 1
  elif i.isdigit():
    digit += 1
  else:
    other += 1

print("Böyük hərf:", upper)
print("Kiçik hərf:", lower)
print("Rəqəm:", digit)
print("Digər simvol:", other)

if len(p) > 8 and upper > 0 and lower > 0 and digit > 0 and other > 0:
  print("Şifrə güclüdür!")
else:
  print("Şifrə zəifdir!")