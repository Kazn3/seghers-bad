def palindroom(woord):
    s = woord[::-1]
    return s

woord = input("Geef je woord in: ")
s = palindroom(woord)

while woord != s:
    print("Dit is geen palindroom, probeer opnieuw!")
    woord = input("Geef je woord in: ")
    s = palindroom(woord)


print(f"""{str.capitalize(woord)} is een palindroom""")

