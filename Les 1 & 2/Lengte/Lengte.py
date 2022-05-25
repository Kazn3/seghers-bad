naam, cmeter = str(input("Geef je naam in:")), int(input("Geef je lengte in:"))

meter, centi = cmeter // 100, cmeter % 100

print(naam.strip() + ", je bent " + str(meter) + " meter en " + str(centi) + " centimeter lang.")

