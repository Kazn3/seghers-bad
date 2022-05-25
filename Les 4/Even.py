som = 0

def isEven(som):
    if som  % 2 ==0:
        print(f"""{som} is even""")


while som != 11:
    isEven(som)
    som += 1