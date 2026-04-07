# ============================================================
# ROBUUSTE UITWERKING: omgaan met slechte data
# ============================================================

# Lijst met producten
producten = ["brood", "melk", "eieren", "kaas", "sap"]

# Prijzen bevatten expres fouten:
# - string die wel een getal is ("3.20")
# - None (ontbrekende waarde)
# - string die geen getal is ("abc")
prijzen = [2.50, "3.20", None, 5, "abc"]


def maak_getal(waarde):
    """
    Probeert een waarde om te zetten naar een float.

    Waarom nodig?
    In echte data kun je verschillende types tegenkomen:
    - int (5)
    - float (2.5)
    - string ("3.20")
    - None
    - onzin ("abc")

    Deze functie zorgt ervoor dat:
    - geldige waarden → float worden
    - ongeldige waarden → None worden
    """

    try:
        # None is sowieso geen geldig getal
        if waarde is None:
            return None

        # Probeer alles om te zetten naar float
        return float(waarde)

    except (ValueError, TypeError):
        # ValueError → bijv. "abc"
        # TypeError → bijv. rare types
        return None


def geldige_prijzen_verzamelen(prijzen):
    """
    Splitst de lijst prijzen in:
    - geldige prijzen (floats)
    - foutieve waarden (originele input)

    Dit voorkomt dat de rest van het programma moet dealen met slechte data.
    """

    geldige_prijzen = []
    foutieve_prijzen = []

    for prijs in prijzen:
        schone_prijs = maak_getal(prijs)

        # Als omzetting mislukt → foutieve data
        if schone_prijs is None:
            foutieve_prijzen.append(prijs)
        else:
            geldige_prijzen.append(schone_prijs)

    return geldige_prijzen, foutieve_prijzen


def totaal_berekenen(prijzen):
    """
    Bereken het totaal van alle prijzen.

    Belangrijk:
    Deze functie gaat ervan uit dat alle prijzen geldig zijn.
    Daarom doen we hier GEEN extra checks meer.
    """

    totaal = 0.0

    for prijs in prijzen:
        totaal += prijs  # veilig, want alleen floats

    return totaal


def duurste_prijs(prijzen):
    """
    Zoek de hoogste prijs in de lijst.

    Edge case:
    Als de lijst leeg is (bijv. alles was fout),
    dan kunnen we geen duurste bepalen.
    """

    if not prijzen:
        return None

    # Start met eerste waarde als referentie
    duurste = prijzen[0]

    for prijs in prijzen:
        if prijs > duurste:
            duurste = prijs

    return duurste


def korting_toepassen(totaal):
    """
    Pas 10% korting toe als totaal boven €20 ligt.
    """

    if totaal > 20:
        return totaal * 0.9

    return totaal


def gemiddelde_prijs(prijzen):
    """
    Bereken gemiddelde prijs.

    Let op:
    Voorkom delen door 0 als lijst leeg is.
    """

    if not prijzen:
        return 0

    return totaal_berekenen(prijzen) / len(prijzen)


# ============================================================
# DATA OPSCHONEN (BELANGRIJKSTE STAP)
# ============================================================

# Hier fixen we de rommelige data voordat we gaan rekenen
geldige_prijzen, foutieve_prijzen = geldige_prijzen_verzamelen(prijzen)


# ============================================================
# OUTPUT PRODUCTEN
# ============================================================

print("Producten:")

for i in range(len(producten)):
    originele_prijs = prijzen[i]
    schone_prijs = maak_getal(originele_prijs)

    # Als prijs niet geldig is → duidelijk melden
    if schone_prijs is None:
        print(i + 1, producten[i], "-> ongeldige prijs:", originele_prijs)
    else:
        print(i + 1, producten[i], "€", schone_prijs)


# ============================================================
# BEREKENINGEN (NU VEILIG)
# ============================================================

# Breakpoint 1 zou hier zitten:
# → geldige_prijzen bevat ALLEEN floats

totaal = totaal_berekenen(geldige_prijzen)
print("Totaalprijs:", totaal)


# Breakpoint 2:
# → geen crashes meer bij vergelijken

duurste = duurste_prijs(geldige_prijzen)

if duurste is None:
    print("Duurste prijs: geen geldige prijzen")
else:
    print("Duurste prijs:", duurste)


totaal_met_korting = korting_toepassen(totaal)
print("Totaal met korting:", totaal_met_korting)


gemiddelde = gemiddelde_prijs(geldige_prijzen)
print("Gemiddelde prijs:", gemiddelde)


# ============================================================
# DEBUG / ANALYSE
# ============================================================

# Hier zie je welke data stuk was
print("Foutieve prijzen:", foutieve_prijzen)
