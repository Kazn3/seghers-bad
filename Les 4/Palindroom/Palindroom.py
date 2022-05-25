def palindroom(woord):
    return woord[::-1]

woord = input("Geef je woord in: ")
s = palindroom(woord)

while woord != s:
    woord = input("Dit is geen palindroom, probeer opnieuw!\nGeef je woord in: ")
    s = palindroom(woord)

print(f"""{str.capitalize(woord)} is een palindroom""")

