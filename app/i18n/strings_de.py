"""
Deutsche UI-Texte

Alle UI-Texte der Anwendung in deutscher Sprache.
KEINE UI-Texte dürfen hardcodiert sein - immer aus dieser Datei laden.
"""

# ==============================================================================
# ALLGEMEIN
# ==============================================================================

APP_TITEL = "Margen-Rechner"
APP_UNTERTITEL = "Berechnung von Händler-Margen"


# ==============================================================================
# EINGABEFORMULAR
# ==============================================================================

FORMULAR_TITEL = "Preiseingabe"

LABEL_EK_NETTO = "Einkaufspreis netto (EK)"
HINT_EK_NETTO = "z.B. 100,00"
PREFIX_EK_NETTO = "€"

LABEL_VK_BRUTTO = "Verkaufspreis brutto (VK)"
HINT_VK_BRUTTO = "z.B. 150,00"
PREFIX_VK_BRUTTO = "€"

LABEL_MWST = "Mehrwertsteuer"
HINT_MWST = "Standard: 19%"

LABEL_RABATT_MODUS = "Rabatt-Modus"
HINT_RABATT_MODUS = "Wie werden Rabatte berechnet?"

LABEL_RABATTE = "Rabatte"
BUTTON_RABATT_HINZUFUEGEN = "+ Rabatt hinzufügen"
HINT_RABATT = "z.B. 5,0"
SUFFIX_RABATT = "%"
BUTTON_RABATT_ENTFERNEN = "Entfernen"

MAX_RABATTE_ERREICHT = "Maximale Anzahl Rabatte erreicht"


# ==============================================================================
# RABATT-MODI
# ==============================================================================

MODUS_ADDIERT_LABEL = "Addiert (5% + 10% = 15%)"
MODUS_NACHGELAGERT_LABEL = "Nachgelagert (kaufmännisch)"


# ==============================================================================
# MEHRWERTSTEUER
# ==============================================================================

MWST_19_LABEL = "19% (Standard)"
MWST_7_LABEL = "7% (ermäßigt)"
MWST_0_LABEL = "0% (steuerfrei)"


# ==============================================================================
# ERGEBNISANZEIGE
# ==============================================================================

ERGEBNIS_TITEL = "Ergebnis"

LABEL_VK_NETTO_BERECHNET = "VK netto"
LABEL_EFFEKTIVER_EK = "Effektiver EK"
LABEL_GESAMTRABATT = "Gesamtrabatt"
LABEL_ROHERTRAG_EURO = "Rohertrag"
LABEL_ROHERTRAG_PROZENT = "Rohertrag %"
LABEL_BEWERTUNG = "Bewertung"


# ==============================================================================
# AMPEL-STATUS
# ==============================================================================

AMPEL_ROT_TEXT = "Niedrige Marge"
AMPEL_ROT_BESCHREIBUNG = "< 20% - nicht empfohlen"

AMPEL_GELB_TEXT = "Mittlere Marge"
AMPEL_GELB_BESCHREIBUNG = "20-35% - akzeptabel"

AMPEL_GRUEN_TEXT = "Gute Marge"
AMPEL_GRUEN_BESCHREIBUNG = "> 35% - sehr gut"


# ==============================================================================
# FEHLERMELDUNGEN
# ==============================================================================

FEHLER_UNGUELTIGE_EINGABE = "Ungültige Eingabe"
FEHLER_NEGATIVE_WERTE = "Negative Werte sind nicht erlaubt"
FEHLER_RABATT_ZU_HOCH = "Rabatt darf nicht über 100% liegen"
FEHLER_BERECHNUNG = "Fehler bei der Berechnung"


# ==============================================================================
# TOOLTIPS / HILFE
# ==============================================================================

TOOLTIP_EK_NETTO = "Der Netto-Einkaufspreis ohne Mehrwertsteuer"
TOOLTIP_VK_BRUTTO = "Der Brutto-Verkaufspreis inklusive Mehrwertsteuer"
TOOLTIP_MWST = "Der anzuwendende Mehrwertsteuersatz"
TOOLTIP_RABATT_MODUS = "Addiert: Rabatte werden summiert\nNachgelagert: Rabatte werden nacheinander angewendet (kaufmännisch korrekt)"
TOOLTIP_RABATTE = "Beliebig viele Rabatte können hinzugefügt werden"


# ==============================================================================
# BARCODE-SCANNER (für zukünftige Features)
# ==============================================================================

BUTTON_BARCODE_SCANNEN = "Barcode scannen"
LABEL_EAN_EINGABE = "EAN/Barcode"
HINT_EAN_EINGABE = "z.B. 4012345678901"


# ==============================================================================
# API-INTEGRATION (für zukünftige Features)
# ==============================================================================

BUTTON_ARTIKEL_LADEN = "Artikel laden"
STATUS_LADE_ARTIKEL = "Lade Artikeldaten..."
FEHLER_ARTIKEL_NICHT_GEFUNDEN = "Artikel nicht gefunden"
FEHLER_API_VERBINDUNG = "Verbindung zur API fehlgeschlagen"


# ==============================================================================
# BENUTZEREINSTELLUNGEN (für zukünftige Features)
# ==============================================================================

MENU_EINSTELLUNGEN = "Einstellungen"
LABEL_SPRACHE = "Sprache"
LABEL_THEME = "Design"
BUTTON_SPEICHERN = "Speichern"
BUTTON_ABBRECHEN = "Abbrechen"
