getal = 1
maal = 1
while getal != 11:
    print(f"De tafel van {getal}:")
    while maal != 11:
        tafel = maal * getal
        print(f"{maal} * {getal} = {tafel}")
        maal += 1

    getal += 1
    maal = 1

