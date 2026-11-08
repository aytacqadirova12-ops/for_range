temperatures = [-3, 2, 8, 15, 22, 27, 31]
gun = 1

for temp in temperatures:
  if temp < 0:
    print(f"{gun}. gün: {temp}° → Şaxta")
  elif temp <= 9:
    print(f"{gun}. gün: {temp}° → Soyuq")
  elif temp <= 19:
    print(f"{gun}. gün: {temp}° → Mülayim")
  elif temp <= 29:
    print(f"{gun}. gün: {temp}° → İsti")
  else:
    print(f"{gun}. gün: {temp}° → Çox isti")

  gun += 1