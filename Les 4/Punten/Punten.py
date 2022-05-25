def aantalvakken():
    try:
        return int(input("Hoeveel vakken heb je?"))

    except:
        vakken()

num = aantalvakken()

print()
print("Geef je vakken in")

vakken = {f'Vak {i+1}': input(f'Vak {i + 1}: ') for i in range(num)}

def ingave():
    try :
        return {vak: float(input(f'{vak}: ')) for vak in vakken.values()}

    except:
        print('Foutieve ingave, geef al je punten opnieuw in')
        ingave()

print()
print("Geef je punten in voor")

punten = ingave()

gemiddelde = sum(punten.values()) / num
print()
print(f'Je gemiddelde bedraagt {round(gemiddelde, 2)}%')
print(f'Je behaalde met {round(max(punten.values()), 2)} % de meeste punten voor het vak ' + {value: key for key, value in punten.items()}[max(punten.values())]) 

