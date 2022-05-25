from datetime  import date, datetime, timedelta

naam1 = input("Geef je naam in ")
sh = datetime.today().hour
sm = datetime.today().minute

if sh < 10:
    print(f"""
    Naam: {naam1}
    starttijd in uur: {sh}
    starttijd in minuten: {sm}
    
    Ongeldige invoer""")

else:
    naam2 = input("Geef je naam in ")
    eh = datetime.today().hour
    em = datetime.today().minute

    if eh >= 22:
        print(f"""
            Naam: {naam1}
            starttijd in uur: {sh}
            starttijd in minuten: {sm}
            eindtijd in uur: {eh}
            eindtijd in minuten: {em}
            
            Ongeldige invoer""")

    else:
        start = datetime.strptime(f'{sh}{sm}', '%H%M')
        stop = datetime.strptime(f'{eh}{em}', '%H%M')

        if sh < 16:
            if eh < 16:
                voormiddag = stop - start
                namiddag = timedelta(0)
            else:
                voormiddag = datetime.strptime('1600', '%H%M') - start
                namiddag = stop - datetime.strptime('1600', '%H%M')
        else:
            voormiddag = datetime.strptime('0000', '%H%M')
            namiddag = stop - datetime.strptime('1600', '%H%M')

        loonvm = (voormiddag.seconds / 3600) * 15
        loonnm = (namiddag.seconds / 3600) * 20
        loontot = loonvm + loonnm

        print("Naam: {} \n"
          "starttijd in uur: {} \n"
          "starttijd in minuten: {} \n"
          "eindtijd in uur: {} \n"
          "eindtijd in minuten: {} \n"
          "\n"
          "{}, op {} heb je gewerkt van {}:{} tot {}:{}. \n"
          "\n"
          "Loonberekening: \n"
          "{} uur voor 16 uur à 15 €/u = {} \n"
          "{} uur tss. 16-22u à 20 €/u = {} \n"
          "\n"
          "Je totaalverdiende dagloon bedraagt: {} euro.".format(naam1, sh, sm, eh, em, naam1, date.today(),sh, sm, eh, em,
                                                                 round((voormiddag.seconds/3600), 2), round(loonvm, 2), round((namiddag.seconds/3600), 2), round(loonnm, 2), round(loontot,2)))


'''print(f""" 
Naam: {naam1}
starttijd in uur: {sh}
starttijd in minuten: {sm}
eindtijd in uur: {sh}
eindtijd in minuten: {sm}

{naam1}, op {date.today()} heb je gewerkt van {sh}:{sm} tot {eh}:{em}.

Loonberekening:
{voormiddag} uur voor 16 uur à 15 €/u = {loonvm}
{namiddag} uur tss. 16-22u à 20 €/u = {loonnm}

Je totaalverdiende dagloon bedraagt: {loontot} euro.
""".)
'''

