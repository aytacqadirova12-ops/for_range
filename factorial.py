s=int(input("Ədəd daxil edin: "))
if s<0:
    print("Mənfi ədədin faktorialı yoxdur")
else:
    fakt=1
    for i in range(1,s +1):
        fakt=fakt*i
    print("Faktorial:", fakt)