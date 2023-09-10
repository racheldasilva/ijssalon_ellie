from algemene_functies import mijn_functie_2

def aanbieding_1():
    prijzen = {
        "smaak": "aardbei",
        "prijs": 4,
        "korting": 0.1
    }
    aanbieding = prijzen["prijs"] * (1 - prijzen["korting"])
    aanbieding_str = f"{aanbieding:.2f}".replace('.', ',')
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {prijzen['smaak']}, van {prijzen['prijs']} euro voor {aanbieding_str} euro"
print(aanbieding_1())



def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
dagelijkse_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(dagelijkse_inkomsten, 0.09))



def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return[laagste, hoogste]
dagelijkse_inkomsten = [220, 440, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(dagelijkse_inkomsten)
print(f"De laagste waarde is: {resultaat[0]} en de hoogste waarde is: {resultaat[1]}")



def inkomsten_gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal_elementen = len(mijn_lijst)
    gemiddelde = totaal / aantal_elementen
    return gemiddelde
dagelijkse_inkomsten = [220, 440, 125, 160, 205, 90, 345]
print(f"De gemiddelde inkomsten deze week zijn {inkomsten_gemiddelde(dagelijkse_inkomsten):.2f} euro")



def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
getallen = [5, 10, 3, 6, 4, 12]
resultaat = meervoudig(getallen)
print(f"De laagste waarde is: {resultaat[0]} en de hoogste waarde is: {resultaat[1]}")


def combinatie(invoer_lijst_2):
    return meervoudig(invoer_lijst_2)
korte_lijst = combinatie(getallen)
resultaat_2 = mijn_functie_2(korte_lijst[0], korte_lijst[1])
print(resultaat_2)
