from random import randint

getal = int(input("Welk getal moet de computer raden tussen 1 en 100? "))

while getal > 100 or getal < 1:
    print(f"""Dit kan niet, gelieve opnieuw een getal in te geven tussen 1 en 100""")
    getal = int(input("Welk getal moet de computer raden tussen 1 en 100? "))

a = 1
b = 100
aantal = 1
gok = randint(a,b)
while gok != getal:
    print(f"""[{a},{b}] --> computer gokt {gok}""")
    if gok < getal:
        a = gok + 1
    else:
        b = gok - 1
    gok = randint(a,b)
    aantal += 1

if aantal == 1:
    print(f"""De computer had {aantal} poging nodig om het getal {getal} te raden.""")
else:
    print(f"""[{a},{b}] --> computer gokt {gok}
De computer had {aantal} pogingen nodig om het getal {getal} te raden.""")