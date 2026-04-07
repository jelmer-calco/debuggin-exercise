# ============================================================
# PYTHON DEBUG-OPDRACHTENSET V3
# Thema: bugs in loops herkennen en debuggen
# Focus:
# - bugs zichtbaar IN de loop
# - veel afwisseling in context/verhaal
# - if/else, for, while, index, mutatie, logische fouten
# - geschikt voor ongeveer 60 minuten debuggen
# ============================================================

# INSTRUCTIE
# - Zet breakpoints precies op de aangegeven plekken.
# - Kijk tijdens het debuggen steeds naar:
#   - de loopvariabele
#   - de huidige waarde
#   - het type van de waarde
#   - of de conditie echt doet wat je denkt
# - Fix niet meteen alles tegelijk.
# - Zoek eerst uit WAAR het fout gaat, dan PAS waarom.

# ============================================================
# OPDRACHT 1 — BIOSCOOPTICKETS TELLEN
# Thema: bug in for-loop
# ============================================================

print("\\n--- OPDRACHT 1: BIOSCOOPTICKETS ---")

tickets = ["volwassene", "kind", "kind", "volwassene", "student"]

# hier zou je stepout kunnen gebruiken 
def tel_betaalde_tickets(tickets):
    aantal = 0
    for ticket in tickets:
        if ticket == "volwassene" or "student":    # <-- Breakpoint A
            aantal += 1
    return aantal

# step into je komt ergens anders uit dan bij steopver 
# doe je Step Into om in tel_betaalde_tickets te komen.
aantal_betaald = tel_betaalde_tickets(tickets)

print("Aantal betaalde tickets:", aantal_betaald)

# DEBUGVRAGEN
# - Waarom wordt bijna alles meegeteld?
# - Wat geeft de conditie echt terug?
# - Welke waarden van ticket zie je tijdens de loop?


# ============================================================
# OPDRACHT 2 — CHATBERICHTEN FILTEREN
# Thema: lijst muteren tijdens loop
# ============================================================

print("\\n--- OPDRACHT 2: CHATFILTER ---")

berichten = ["hoi", "spam", "welkom", "spam", "tot morgen", "spam"]

def verwijder_spam(berichten):
    for bericht in berichten:
        if bericht == "spam":
            berichten.remove(bericht)              # <-- Breakpoint A
    return berichten

schone_berichten = verwijder_spam(berichten)
print("Schone berichten:", schone_berichten)

# DEBUGVRAGEN
# - Waarom blijft er soms spam staan?
# - Wat gebeurt er met de lijst terwijl je erdoorheen loopt?
# - Welke waarde wordt overgeslagen?


# ============================================================
# OPDRACHT 3 — WACHTWOORDCONTROLE
# Thema: return op verkeerde plek in loop
# ============================================================

print("\\n--- OPDRACHT 3: WACHTWOORDCONTROLE ---")

wachtwoord = "School2024!"

def heeft_speciaal_teken(wachtwoord):
    speciale_tekens = "!@#$%&*"
    for letter in wachtwoord:
        if letter in speciale_tekens:
            return True
        else:
            return False                          # <-- Breakpoint A

print("Speciaal teken gevonden:", heeft_speciaal_teken(wachtwoord))

# DEBUGVRAGEN
# - Waarom stopt de functie veel te vroeg?
# - Hoeveel letters bekijkt de loop nu echt?
# - Wat moet er pas na de loop gebeuren?


# ============================================================
# OPDRACHT 4 — QUIZ ANTWOORDEN NAKIJKEN
# Thema: indexfout in loop
# ============================================================

print("\\n--- OPDRACHT 4: QUIZ NAKIJKEN ---")

goede_antwoorden = ["A", "C", "B", "D"]
gegeven_antwoorden = ["A", "C", "B"]

def score_berekenen(goede_antwoorden, gegeven_antwoorden):
    score = 0
    for i in range(len(goede_antwoorden)):
        if gegeven_antwoorden[i] == goede_antwoorden[i]:    # <-- Breakpoint A
            score += 1
    return score

score = score_berekenen(goede_antwoorden, gegeven_antwoorden)
print("Score:", score)

# DEBUGVRAGEN
# - Op welk moment gaat het mis?
# - Welke lijst is korter?
# - Moet je over alle goede antwoorden loopen of over de overlap?


# ============================================================
# OPDRACHT 5 — VOORRAAD BIJWERKEN
# Thema: verkeerde update in while-loop
# ============================================================

print("\\n--- OPDRACHT 5: VOORRAAD BIJWERKEN ---")

leveringen = [3, 2, 5]
voorraad = 10

def verwerk_leveringen(voorraad, leveringen):
    i = 0
    while i < len(leveringen):
        voorraad += leveringen[i]
        voorraad += 1                               # <-- Breakpoint A
    return voorraad

nieuwe_voorraad = verwerk_leveringen(voorraad, leveringen)
print("Nieuwe voorraad:", nieuwe_voorraad)

# DEBUGVRAGEN
# - Waarom stopt de loop niet?
# - Welke variabele had verhoogd moeten worden?
# - Hoe kun je dit in de debugger snel zien?


# ============================================================
# OPDRACHT 6 — AANWEZIGHEID CONTROLEREN
# Thema: else in loop verkeerd gebruikt
# ============================================================

print("\\n--- OPDRACHT 6: AANWEZIGHEID ---")

aanwezigen = ["Sam", "Noor", "Lina", "Milan"]

def is_aanwezig(naam, aanwezigen):
    for persoon in aanwezigen:
        if persoon == naam:
            return True
        else:
            return False                           # <-- Breakpoint A

print("Is Lina aanwezig?", is_aanwezig("Lina", aanwezigen))

# DEBUGVRAGEN
# - Waarom wordt alleen het eerste element echt gecontroleerd?
# - Wanneer hoort False pas teruggegeven te worden?


# ============================================================
# OPDRACHT 7 — TEMPERATUURWAARSCHUWINGEN
# Thema: if/elif volgorde fout in loop
# ============================================================

print("\\n--- OPDRACHT 7: TEMPERATUURWAARSCHUWINGEN ---")

temperaturen = [8, 19, 28, 35]

def geef_label(temp):
    if temp > 15:
        return "warm"
    elif temp > 30:
        return "heet"
    else:
        return "koud"

for temp in temperaturen:
    label = geef_label(temp)                       # <-- Breakpoint A
    print(temp, "graden ->", label)

# DEBUGVRAGEN
# - Waarom krijgt 35 niet het label "heet"?
# - Welke conditie wordt eerst geraakt?
# - Hoe moet de volgorde van if/elif eruitzien?


# ============================================================
# OPDRACHT 8 — WACHTLIJST AFHANDELEN
# Thema: element overslaan door verkeerde index-update
# ============================================================

print("\\n--- OPDRACHT 8: WACHTLIJST ---")

wachtlijst = ["Eva", "Tom", "Sara", "Bram"]
plaatsen_vrij = 2

def haal_mensen_van_wachtlijst(wachtlijst, plaatsen_vrij):
    geplaatsten = []
    i = 0

    while i < len(wachtlijst) and plaatsen_vrij > 0:
        geplaatsten.append(wachtlijst[i])
        wachtlijst.pop(i)                          # <-- Breakpoint A
        plaatsen_vrij -= 1
        i += 1

    return geplaatsten, wachtlijst

geplaatsten, over = haal_mensen_van_wachtlijst(wachtlijst, plaatsen_vrij)
print("Geplaatst:", geplaatsten)
print("Over op wachtlijst:", over)

# DEBUGVRAGEN
# - Waarom wordt niet de eerste twee mensen geplaatst?
# - Wat gebeurt er met indexes na pop(i)?
# - Moet i hier wel omhoog?


# ============================================================
# OPDRACHT 9 — BUSSTOPS TONEN
# Thema: off-by-one fout in while-loop
# ============================================================

print("\\n--- OPDRACHT 9: BUSSTOPS ---")

haltes = ["Centrum", "Station", "Park", "Ziekenhuis"]

def toon_haltes(haltes):
    i = 0
    while i <= len(haltes):                        # <-- Breakpoint A
        print("Volgende halte:", haltes[i])
        i += 1

toon_haltes(haltes)

# DEBUGVRAGEN
# - Welke waarde heeft i als het fout gaat?
# - Waarom is <= hier fout?
# - Wat is het verschil tussen < en <= in loops?


# ============================================================
# OPDRACHT 10 — GAME SCOREBORD
# Thema: string en int door elkaar in loop
# ============================================================

print("\\n--- OPDRACHT 10: GAME SCOREBORD ---")

scores = [10, "15", 8, "x", 12]

def hoogste_score(scores):
    hoogste = 0
    for score in scores:
        if score > hoogste:                        # <-- Breakpoint A
            hoogste = score
    return hoogste

print("Hoogste score:", hoogste_score(scores))

# DEBUGVRAGEN
# - Welke waarde laat de loop crashen?
# - Zijn alle scores wel getallen?
# - Wat gebeurt er bij "x"?


# ============================================================
# OPDRACHT 11 — E-MAILADRESSEN CONTROLEREN
# Thema: teller op verkeerde plek
# ============================================================

print("\\n--- OPDRACHT 11: E-MAILCHECK ---")

emails = ["a@school.nl", "b-school.nl", "c@school.nl", "dschool.nl"]

def tel_geldige_emails(emails):
    geldig = 0
    for email in emails:
        if "@" in email:
            pass
        geldig += 1                                 # <-- Breakpoint A
    return geldig

print("Aantal geldige e-mails:", tel_geldige_emails(emails))

# DEBUGVRAGEN
# - Waarom telt hij alles?
# - Bij welke indentatie hoort geldig += 1?
# - Hoe zie je dit terug tijdens de loop?


# ============================================================
# OPDRACHT 12 — EINDOPDRACHT: ESCAPEROOM-SYSTEEM
# Thema: veel bugs in verschillende loops en condities
# ============================================================

print("\\n--- OPDRACHT 12: ESCAPEROOM ---")

spelers = ["Ana", "Bo", "Cy", "Di"]
tijden = ["45", 52, None, "abc"]
codes = ["OK-1", "FOUT", "OK-2", "OK-3"]

def geldige_code(code):
    if code.startswith("OK"):
        return True
    else:
        return False

def verwerk_scores(spelers, tijden, codes):
    geslaagd = []
    fouten = []
    i = 0

    while i < len(spelers):
        speler = spelers[i]
        tijd = tijden[i]
        code = codes[i]

        if geldige_code(code):
            tijd = float(tijd)                      # <-- Breakpoint A
            if tijd < 60:
                geslaagd.append(speler)
            else:
                fouten.append(speler)
        else:
            fouten.append(speler)

        i += 1

    return geslaagd, fouten

geslaagd, fouten = verwerk_scores(spelers, tijden, codes)
print("Geslaagd:", geslaagd)
print("Fouten:", fouten)

# EINDDOEL
# Maak het systeem zo dat:
# - het nooit crasht
# - ongeldige tijden netjes worden opgevangen
# - None wordt herkend
# - alleen spelers met geldige code én tijd onder 60 slagen
# - foute invoer apart wordt gerapporteerd
# - je duidelijk ziet welke loopstap fout ging
#
# EXTRA CHALLENGE
# Voeg een rapport toe zoals:
# - geslaagde spelers
# - niet geslaagd
# - ongeldige tijden
# - ongeldige codes
# - totaal aantal verwerkte spelers
