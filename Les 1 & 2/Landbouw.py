stukken, kist, pallet = int(input("Geef het aantal opgehaalde stukken in:")), int(input("Hoeveel stukken gaan in een kist?")), int(input("Hoeveel kisten passen op een pallet?"))

kisten = stukken // 200
pallets = kisten // 50

restkist, reststuk = 100 - kisten, stukken - kisten * 200
print()
print(f'Aantal gevulde kisten = {kisten}')
print(f'Aantal gevulde pallets = {pallets}')
print()
print(f'Aantal resterende kisten = {restkist}')
print(f'Aantal resterende stukken = {reststuk}')
