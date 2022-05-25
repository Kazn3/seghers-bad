from random import randint

a, b, c = randint(1, 10), randint(1, 10), randint(1, 10)

if a == b == c:
    print(f"""
De 3 getallen zijn {a} {b} {c}
Hoera, gewonnen!""")

elif a == b != c or a == c != b or b == c != a:
    print(f"""
De 3 getallen zijn {a} {b} {c}
Bijna gewonnen!""")

else:
    print(f"""
De 3 getallen zijn {a} {b} {c}
Spijtig, verloren.""")



