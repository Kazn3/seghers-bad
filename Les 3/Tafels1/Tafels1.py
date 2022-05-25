print(f"""Tafels van de vermenigvuldiging""")
getal = int(input("Geef de gewenste tafel: "))
maal = 1
while maal != 11:
    tafel = maal * getal
    print(f"""{maal} * {getal} = {tafel}""")
    maal += 1

