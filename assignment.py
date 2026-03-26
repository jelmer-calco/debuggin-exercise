# ============================================================
# PYTHON DEBUG OPDRACHT (VERDIEPING)
# Onderwerp: robuust omgaan met slechte data
# Doel: leren omgaan met echte fouten in data
# ============================================================

# OPDRACHT
# Je hebt een boodschappenlijst met producten en prijzen.
# Maar de data is niet betrouwbaar (zoals in echte systemen).
#
# Het programma moet:
# 1) Producten tonen
# 2) Totale prijs berekenen
# 3) Duurste product vinden
# 4) Korting toepassen boven €20
#
# Alleen: de data bevat fouten → het programma crasht.

# ============================================================
# FOUTE DATA (REALISTISCHER)
# ============================================================

producten = ["brood", "melk", "eieren", "kaas", "sap"]

prijzen = [2.50, "3.20", None, 5, "abc"]


# ============================================================
# FOUTE CODE (EXPRES)
# ============================================================

def totaal_berekenen(prijzen):
    totaal = 0
    for prijs in prijzen:
        totaal = totaal + prijs  # <-- BREAKPOINT
    return totaal


def duurste_prijs(prijzen):
    duurste = 0
    for p in prijzen:
        if p > duurste:
            duurste = p
    return duurste


def korting_toepassen(totaal):
    if totaal > 20:
        totaal = totaal * 0.9
    return totaal


print("Producten:")
for i in range(len(producten)):
    print(i + 1, producten[i], "€", prijzen[i])


# <-- BREAKPOINT 1
totaal = totaal_berekenen(prijzen)
print("Totaalprijs:", totaal)

# <-- BREAKPOINT 2
duurste = duurste_prijs(prijzen)
print("Duurste prijs:", duurste)

totaal_met_korting = korting_toepassen(totaal)
print("Totaal met korting:", totaal_met_korting)


# ============================================================
# BREAKPOINTS
# ============================================================

# Breakpoint 1
# - Wat zit er in prijzen?
# - Welke types zie je?
# - Welke waarden zijn problematisch?

# Breakpoint 2
# - Werkt vergelijken (>) met alle types?
# - Wat gebeurt er bij None of "abc"?

# ============================================================
# HINTS
# ============================================================

# Hint 1
# Niet alle waarden zijn bruikbaar als getal

# Hint 2
# Denk aan:
# - isinstance()
# - float() proberen
# - try/except

# Hint 3
# Sommige fouten zie je pas in de tweede functie

# ============================================================
# DOEL
# ============================================================

# Maak het programma zo dat:
# - Het NOOIT crasht
# - Foute data wordt overgeslagen of gecorrigeerd
# - De output klopt

# ============================================================
# EXTRA CHALLENGE
# ============================================================

# 1) Zet strings zoals "3.20" automatisch om naar float
# 2) Negeer None waarden netjes
# 3) Geef een lijst van foutieve prijzen aan het einde
# 4) Bereken ook de gemiddelde prijs