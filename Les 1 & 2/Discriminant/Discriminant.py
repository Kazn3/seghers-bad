from math import sqrt

print("ax² + bx + c = 0")

a, b, c = float(input("a =?")), float(input("b =?")), float(input("c =?"))

D = b ** 2 - 4 * a * c

if D > 0:
    opl1 = (-b + sqrt(D)) / (2 * a)
    opl2 = (-b - sqrt(D)) / (2 * a)

    print(f"""
De discriminant is: {D}
    
De vergelijking heeft 2 reële oplossingen:
x1 = {opl1}
x2 = {opl2}""")

elif D == 0:
    opl1 = -b / (2 * a)

    print(f"""
De discriminant is: {D}

De vergelijking heeft twee gelijke reële oplossingen:
x1 = x2 = {opl1}""")

elif D < 0:
    print(f""""
De discriminant is: {D}

De vergelijking heeft geen reële oplossingen.""")
