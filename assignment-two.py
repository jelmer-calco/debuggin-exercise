# ============================================================
# PYTHON DEBUG-OPDRACHTENSET
# Onderwerp: debuggen met breakpoints, types, loops, functies,
#            slechte data, indexfouten en logische fouten
# Doel: leerlingen 45-90 minuten laten oefenen met echt debuggen
# ============================================================

# INSTRUCTIE
# - Werk opdracht voor opdracht.
# - Zet steeds breakpoints op de aangegeven plekken.
# - Gebruik je debugger om variabelen te bekijken.
# - Fix eerst de bug, verbeter daarna pas de code.
# - Schrijf eventueel per opdracht op:
#   1) wat er fout ging
#   2) waarom het fout ging
#   3) hoe je het hebt opgelost

# ============================================================
# OPDRACHT 1 — TYPEFOUT IN TOTAALBEREKENING
# Thema: str tussen getallen
# Leerdoel: type bekijken in debugger
# ============================================================

print("\\n--- OPDRACHT 1 ---")

producten_1 = ["brood", "melk", "eieren", "kaas"]
prijzen_1 = [2.50, 1.20, 3.00, "4.75"]

def totaal_berekenen_1(prijzen):
    totaal = 0
    for prijs in prijzen:
        totaal = totaal + prijs   # <-- Breakpoint A
    return totaal

def duurste_prijs_1(prijzen):
    duurste = 0
    for prijs in prijzen:
        if prijs > duurste:       # <-- Breakpoint B
            duurste = prijs
    return duurste

print("Producten:")
for i in range(len(producten_1)):
    print(i + 1, producten_1[i], "€", prijzen_1[i])

# <-- Breakpoint C
totaal_1 = totaal_berekenen_1(prijzen_1)
print("Totaalprijs:", totaal_1)

duurste_1 = duurste_prijs_1(prijzen_1)
print("Duurste prijs:", duurste_1)

# VRAGEN
# - Welke waarde veroorzaakt de crash?
# - Wat is type(prijs) op het moment dat het misgaat?
# - Kan de functie duurste_prijs ook stuklopen?


# ============================================================
# OPDRACHT 2 — NONE EN ONGELDIGE DATA
# Thema: onbetrouwbare data
# Leerdoel: stap voor stap door loops heen gaan
# ============================================================

print("\\n--- OPDRACHT 2 ---")

producten_2 = ["brood", "melk", "eieren", "kaas", "sap", "yoghurt"]
prijzen_2 = [2.50, None, 3.20, "abc", 4.80, "1.99"]

def gemiddelde_prijs_2(prijzen):
    totaal = 0
    aantal = 0

    for prijs in prijzen:
        totaal += prijs           # <-- Breakpoint A
        aantal += 1

    return totaal / aantal       # <-- Breakpoint B

gemiddelde_2 = gemiddelde_prijs_2(prijzen_2)
print("Gemiddelde prijs:", gemiddelde_2)

# OPDRACHT
# Maak deze functie zo dat:
# - None wordt overgeslagen
# - strings zoals "1.99" worden omgezet naar float
# - ongeldige strings zoals "abc" worden genegeerd
# - het programma nooit crasht
# - de functie ook kan vertellen welke invoer fout was
#
# EXTRA VRAGEN
# - Wat gebeurt er met aantal?
# - Tel je nu alleen geldige prijzen mee of ook foute?


# ============================================================
# OPDRACHT 3 — INDEXFOUT TUSSEN PRODUCTEN EN PRIJZEN
# Thema: lijsten met ongelijke lengte
# Leerdoel: IndexError begrijpen
# ============================================================

print("\\n--- OPDRACHT 3 ---")

producten_3 = ["brood", "melk", "eieren", "kaas", "boter"]
prijzen_3 = [2.50, 1.20, 3.00]

for i in range(len(producten_3)):
    print(producten_3[i], "kost €", prijzen_3[i])   # <-- Breakpoint A

# OPDRACHT
# Zorg dat:
# - het programma niet crasht
# - ontbrekende prijzen netjes worden gemeld
# - je aan het einde ziet voor welke producten geen prijs was
#
# EXTRA CHALLENGE
# - Geef ook een waarschuwing als er meer prijzen dan producten zijn


# ============================================================
# OPDRACHT 4 — LOGISCHE FOUT BIJ KORTING
# Thema: code draait wel, maar uitkomst klopt niet
# Leerdoel: logische bugs debuggen
# ============================================================

print("\\n--- OPDRACHT 4 ---")

prijzen_4 = [4.00, 5.00, 6.00, 7.00]

def totaal_berekenen_4(prijzen):
    totaal = 0
    for prijs in prijzen:
        totaal += prijs
    return totaal

def korting_toepassen_4(totaal):
    if totaal >= 20:
        korting = 0.10
    else:
        korting = 0
    totaal = totaal - korting    # <-- Breakpoint A
    return totaal

totaal_4 = totaal_berekenen_4(prijzen_4)
totaal_met_korting_4 = korting_toepassen_4(totaal_4)

print("Totaal:", totaal_4)
print("Totaal met korting:", totaal_met_korting_4)

# OPDRACHT
# Hier crasht niets, maar de uitkomst is fout.
# Zoek uit:
# - Wat hoort de uitkomst te zijn?
# - Wat doet de code nu echt?
# - Welke variabele bevat een percentage en welke een bedrag?


# ============================================================
# OPDRACHT 5 — VERKEERDE STARTWAARDE BIJ DUURSTE PRODUCT
# Thema: negatieve prijzen / refunds / edge cases
# Leerdoel: nadenken over startwaarden
# ============================================================

print("\\n--- OPDRACHT 5 ---")

prijzen_5 = [-3.00, -1.50, -9.20, -0.99]

def duurste_prijs_5(prijzen):
    duurste = 0                    # <-- Breakpoint A
    for prijs in prijzen:
        if prijs > duurste:
            duurste = prijs
    return duurste

print("Duurste prijs:", duurste_prijs_5(prijzen_5))

# OPDRACHT
# De code crasht niet, maar de uitkomst klopt niet.
# Zoek uit waarom.
#
# DENK AAN
# - Wat betekent 'duurste' als alle prijzen negatief zijn?
# - Is 0 hier een goede startwaarde?


# ============================================================
# OPDRACHT 6 — FUNCTIES WERKEN LOS, MAAR SAMEN GAAT HET MIS
# Thema: verkeerde return values
# Leerdoel: flow tussen functies volgen
# ============================================================

print("\\n--- OPDRACHT 6 ---")

prijzen_6 = [2.50, 3.50, 4.00]

def totaal_berekenen_6(prijzen):
    totaal = 0
    for prijs in prijzen:
        totaal += prijs
    print("Totaal in functie:", totaal)
    # return totaal              # <-- hier ontbreekt iets

def korting_toepassen_6(totaal):
    if totaal > 10:               # <-- Breakpoint A
        return totaal * 0.9
    return totaal

totaal_6 = totaal_berekenen_6(prijzen_6)
eindbedrag_6 = korting_toepassen_6(totaal_6)

print("Eindbedrag:", eindbedrag_6)

# OPDRACHT
# - Waarom crasht dit pas later?
# - Welke functie veroorzaakt het echte probleem?
# - Welke waarde komt er uit totaal_berekenen_6?


# ============================================================
# OPDRACHT 7 — MUTEREN VAN DATA OP DE VERKEERDE MANIER
# Thema: lijst aanpassen tijdens iteratie
# Leerdoel: begrijpen waarom loops gek gedrag geven
# ============================================================

print("\\n--- OPDRACHT 7 ---")

prijzen_7 = [2.50, None, 3.00, None, 4.20, "5.00", "abc"]

def opschonen_7(prijzen):
    for prijs in prijzen:
        if prijs is None or prijs == "abc":
            prijzen.remove(prijs)   # <-- Breakpoint A
    return prijzen

schone_prijzen_7 = opschonen_7(prijzen_7)
print("Schone prijzen:", schone_prijzen_7)

# OPDRACHT
# Deze code lijkt soms te werken, maar is gevaarlijk.
# Zoek uit:
# - Welke waarden worden overgeslagen?
# - Waarom is verwijderen tijdens iteratie tricky?
# - Hoe kun je dit veiliger oplossen?


# ============================================================
# OPDRACHT 8 — COMPLEETE EINDOPDRACHT
# Thema: alles combineren
# Leerdoel: robuust debuggen en verbeteren
# ============================================================

print("\\n--- OPDRACHT 8 ---")

producten_8 = ["brood", "melk", "eieren", "kaas", "sap", "pasta", "rijst"]
prijzen_8 = [2.50, "3.20", None, 6, "abc", -1.00, "4,75"]

def toon_producten_8(producten, prijzen):
    print("Overzicht:")
    for i in range(len(producten)):
        print(i + 1, producten[i], "€", prijzen[i])   # <-- Breakpoint A

def maak_getal_8(prijs):
    return float(prijs)   # <-- Breakpoint B

def totaal_berekenen_8(prijzen):
    totaal = 0
    for prijs in prijzen:
        totaal += maak_getal_8(prijs)   # <-- Breakpoint C
    return totaal

def duurste_prijs_8(prijzen):
    duurste = 0
    for prijs in prijzen:
        prijs = maak_getal_8(prijs)
        if prijs > duurste:
            duurste = prijs
    return duurste

def gemiddelde_prijs_8(prijzen):
    totaal = totaal_berekenen_8(prijzen)
    return totaal / len(prijzen)        # <-- Breakpoint D

def korting_toepassen_8(totaal):
    if totaal > 20:
        return totaal * 90 / 100
    return totaal

toon_producten_8(producten_8, prijzen_8)

totaal_8 = totaal_berekenen_8(prijzen_8)
duurste_8 = duurste_prijs_8(prijzen_8)
gemiddelde_8 = gemiddelde_prijs_8(prijzen_8)
eindtotaal_8 = korting_toepassen_8(totaal_8)

print("Totaalprijs:", totaal_8)
print("Duurste prijs:", duurste_8)
print("Gemiddelde prijs:", gemiddelde_8)
print("Totaal met korting:", eindtotaal_8)

# EINDDOEL
# Maak het programma zo dat:
# - het nooit crasht
# - "3.20" wordt omgezet naar float
# - "4,75" ook wordt herkend als 4.75
# - None wordt overgeslagen
# - ongeldige waarden zoals "abc" worden gemeld
# - negatieve prijzen apart als waarschuwing worden getoond
# - ontbrekende prijzen/producten netjes worden afgehandeld
# - gemiddelde alleen over geldige prijzen gaat
# - totaal op 2 decimalen wordt afgerond
# - er een lijst komt met foutieve invoer
#
# EXTRA CHALLENGE
# Maak een rapport zoals:
#
# Geldige prijzen: [...]
# Ongeldige prijzen: [...]
# Negatieve prijzen: [...]
# Ontbrekende prijzen: [...]
# Totaal: ...
# Gemiddelde: ...
# Duurste product: ...
# Totaal met korting: ...


# ============================================================
# BONUSOPDRACHT — ZELF TESTDATA BEDENKEN
# ============================================================

# Bedenk nu zelf 3 testsets:
#
# Testset A:
# - alleen geldige floats
#
# Testset B:
# - mix van ints, floats en strings
#
# Testset C:
# - expres kapotte data:
#   None, lege string, "abc", negatieve prijs, komma-getal
#
# Test per set:
# - totaal
# - gemiddelde
# - duurste
# - korting
# - foutmeldingen
#
# Schrijf erbij:
# - welke bug je verwachtte
# - wat er echt gebeurde
# - of je code robuust genoeg was
