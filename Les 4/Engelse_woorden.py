Getallen = [1, 2, 3, 4, 5, 6]
Nederlands = ["dochter", "moeder", "zoon", "vader", "stiefvader", "stop"]
Engels = ["daughter", "mother", "son", "father", "stepfather"]


print(f"""Engelse woorden oefenen

{Getallen[0:1][0]} = {Nederlands[0:1][0]}
{Getallen[1:2][0]} = {Nederlands[1:2][0]}
{Getallen[2:3][0]} = {Nederlands[2:3][0]}
{Getallen[3:4][0]} = {Nederlands[3:4][0]}
{Getallen[4:5][0]} = {Nederlands[4:5][0]}
{Getallen[5:6][0]} = {Nederlands[5:6][0]}
""")

print("Maak je keuze, 6 = stop: ", end =' ')
nummer = int(input())
while nummer != 6: 
    try:
        print(Nederlands[nummer-1], "in het engels is:", end = ' ')
        woord = str(input())
        if woord == Engels[nummer-1]:
            print("Juist!")
            print("Maak je keuze, 6 = stop: ", end =' ')
            nummer = int(input())

        else:
            print("Fout, het engelse woord is:", Engels[nummer-1])
            print("Maak je keuze, 6 = stop: ", end =' ')
            nummer = int(input())

    except:
        print("Foutieve ingave, probeer opnieuw")
        print("Maak je keuze, 6 = stop: ", end =' ')
        nummer = int(input())




