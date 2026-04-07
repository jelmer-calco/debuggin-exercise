# ============================================================
# PYTHON DEBUG UITWERKINGEN
# ============================================================

# ============================================================
# OPDRACHT 1 — BIOSCOOPTICKETS
# FIX: OR-conditie verkeerd gebruikt
# ============================================================

def tel_betaalde_tickets(tickets):
    aantal = 0
    for ticket in tickets:
        if ticket == "volwassene" or ticket == "student":
            aantal += 1
    return aantal


# ============================================================
# OPDRACHT 2 — CHATFILTER
# FIX: niet muteren tijdens iteratie
# ============================================================

def verwijder_spam(berichten):
    schone_lijst = []
    for bericht in berichten:
        if bericht != "spam":
            schone_lijst.append(bericht)
    return schone_lijst


# ============================================================
# OPDRACHT 3 — WACHTWOORDCONTROLE
# FIX: return buiten de loop
# ============================================================

def heeft_speciaal_teken(wachtwoord):
    speciale_tekens = "!@#$%&*"
    for letter in wachtwoord:
        if letter in speciale_tekens:
            return True
    return False


# ============================================================
# OPDRACHT 4 — QUIZ
# FIX: over overlap loopen
# ============================================================

def score_berekenen(goede_antwoorden, gegeven_antwoorden):
    score = 0
    lengte = min(len(goede_antwoorden), len(gegeven_antwoorden))
    for i in range(lengte):
        if gegeven_antwoorden[i] == goede_antwoorden[i]:
            score += 1
    return score


# ============================================================
# OPDRACHT 5 — VOORRAAD
# FIX: index verhogen
# ============================================================

def verwerk_leveringen(voorraad, leveringen):
    i = 0
    while i < len(leveringen):
        voorraad += leveringen[i]
        i += 1
    return voorraad


# ============================================================
# OPDRACHT 6 — AANWEZIGHEID
# FIX: False NA de loop
# ============================================================

def is_aanwezig(naam, aanwezigen):
    for persoon in aanwezigen:
        if persoon == naam:
            return True
    return False


# ============================================================
# OPDRACHT 7 — TEMPERATUUR
# FIX: volgorde if/elif
# ============================================================

def geef_label(temp):
    if temp > 30:
        return "heet"
    elif temp > 15:
        return "warm"
    else:
        return "koud"


# ============================================================
# OPDRACHT 8 — WACHTLIJST
# FIX: index niet verhogen na pop
# ============================================================

def haal_mensen_van_wachtlijst(wachtlijst, plaatsen_vrij):
    geplaatsten = []
    i = 0

    while i < len(wachtlijst) and plaatsen_vrij > 0:
        geplaatsten.append(wachtlijst[i])
        wachtlijst.pop(i)
        plaatsen_vrij -= 1

    return geplaatsten, wachtlijst


# ============================================================
# OPDRACHT 9 — BUSSTOPS
# FIX: < i.p.v. <=
# ============================================================

def toon_haltes(haltes):
    i = 0
    while i < len(haltes):
        print("Volgende halte:", haltes[i])
        i += 1


# ============================================================
# OPDRACHT 10 — SCORES
# FIX: type check / conversie
# ============================================================

def hoogste_score(scores):
    hoogste = 0
    for score in scores:
        try:
            score = int(score)
            if score > hoogste:
                hoogste = score
        except:
            continue
    return hoogste


# ============================================================
# OPDRACHT 11 — EMAILS
# FIX: juiste indentatie
# ============================================================

def tel_geldige_emails(emails):
    geldig = 0
    for email in emails:
        if "@" in email:
            geldig += 1
    return geldig


# ============================================================
# OPDRACHT 12 — ESCAPEROOM
# ROBUUSTE OPLOSSING
# ============================================================

def geldige_code(code):
    return isinstance(code, str) and code.startswith("OK")


def verwerk_scores(spelers, tijden, codes):
    geslaagd = []
    niet_geslaagd = []
    ongeldige_tijden = []
    ongeldige_codes = []

    i = 0

    while i < len(spelers):
        speler = spelers[i]
        tijd = tijden[i]
        code = codes[i]

        # Check code
        if not geldige_code(code):
            ongeldige_codes.append(speler)
            i += 1
            continue

        # Check tijd
        try:
            if tijd is None:
                raise ValueError("None tijd")

            tijd = float(tijd)

        except:
            ongeldige_tijden.append(speler)
            i += 1
            continue

        # Score bepalen
        if tijd < 60:
            geslaagd.append(speler)
        else:
            niet_geslaagd.append(speler)

        i += 1

    rapport = {
        "geslaagd": geslaagd,
        "niet_geslaagd": niet_geslaagd,
        "ongeldige_tijden": ongeldige_tijden,
        "ongeldige_codes": ongeldige_codes,
        "totaal": len(spelers)
    }

    return rapport


# ============================================================
# TEST RUN (optioneel voor trainees)
# ============================================================

if __name__ == "__main__":

    print("\n--- TESTS ---")

    print(tel_betaalde_tickets(["volwassene", "kind", "student"]))

    print(verwijder_spam(["hoi", "spam", "ok"]))

    print(heeft_speciaal_teken("abc!"))

    print(score_berekenen(["A","B"], ["A"]))

    print(verwerk_leveringen(10, [1,2,3]))

    print(is_aanwezig("Lina", ["Sam","Lina"]))

    print([geef_label(t) for t in [10,20,35]])

    print(haal_mensen_van_wachtlijst(["A","B","C"], 2))

    toon_haltes(["A","B"])

    print(hoogste_score([10,"20","x"]))

    print(tel_geldige_emails(["a@a.nl","b.nl"]))

    rapport = verwerk_scores(
        ["Ana", "Bo", "Cy", "Di"],
        ["45", 52, None, "abc"],
        ["OK-1", "FOUT", "OK-2", "OK-3"]
    )

    print("\nESCAPEROOM RAPPORT:")
    for k, v in rapport.items():
        print(k, ":", v)