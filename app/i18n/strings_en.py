"""
English UI Texts (Placeholder)

All UI texts in English.
Currently stubs for future internationalization.
"""

# ==============================================================================
# GENERAL
# ==============================================================================

APP_TITEL = "Margin Calculator"
APP_UNTERTITEL = "Calculate dealer margins"


# ==============================================================================
# INPUT FORM
# ==============================================================================

FORMULAR_TITEL = "Price Input"

LABEL_EK_NETTO = "Purchase price net"
HINT_EK_NETTO = "e.g. 100.00"
PREFIX_EK_NETTO = "€"

LABEL_VK_BRUTTO = "Sales price gross"
HINT_VK_BRUTTO = "e.g. 150.00"
PREFIX_VK_BRUTTO = "€"

LABEL_MWST = "VAT"
HINT_MWST = "Default: 19%"

LABEL_RABATT_MODUS = "Discount Mode"
HINT_RABATT_MODUS = "How are discounts calculated?"

LABEL_RABATTE = "Discounts"
BUTTON_RABATT_HINZUFUEGEN = "+ Add discount"
HINT_RABATT = "e.g. 5.0"
SUFFIX_RABATT = "%"
BUTTON_RABATT_ENTFERNEN = "Remove"

MAX_RABATTE_ERREICHT = "Maximum number of discounts reached"


# ==============================================================================
# DISCOUNT MODES
# ==============================================================================

MODUS_ADDIERT_LABEL = "Additive (5% + 10% = 15%)"
MODUS_NACHGELAGERT_LABEL = "Sequential (commercial)"


# ==============================================================================
# VAT
# ==============================================================================

MWST_19_LABEL = "19% (Standard)"
MWST_7_LABEL = "7% (Reduced)"
MWST_0_LABEL = "0% (Tax-free)"


# ==============================================================================
# RESULTS DISPLAY
# ==============================================================================

ERGEBNIS_TITEL = "Result"

LABEL_VK_NETTO_BERECHNET = "Sales price net"
LABEL_EFFEKTIVER_EK = "Effective purchase price"
LABEL_GESAMTRABATT = "Total discount"
LABEL_ROHERTRAG_EURO = "Gross profit"
LABEL_ROHERTRAG_PROZENT = "Gross profit %"
LABEL_BEWERTUNG = "Rating"


# ==============================================================================
# TRAFFIC LIGHT STATUS
# ==============================================================================

AMPEL_ROT_TEXT = "Low margin"
AMPEL_ROT_BESCHREIBUNG = "< 20% - not recommended"

AMPEL_GELB_TEXT = "Medium margin"
AMPEL_GELB_BESCHREIBUNG = "20-35% - acceptable"

AMPEL_GRUEN_TEXT = "Good margin"
AMPEL_GRUEN_BESCHREIBUNG = "> 35% - very good"


# ==============================================================================
# ERROR MESSAGES
# ==============================================================================

FEHLER_UNGUELTIGE_EINGABE = "Invalid input"
FEHLER_NEGATIVE_WERTE = "Negative values are not allowed"
FEHLER_RABATT_ZU_HOCH = "Discount cannot exceed 100%"
FEHLER_BERECHNUNG = "Calculation error"


# ==============================================================================
# TOOLTIPS / HELP
# ==============================================================================

TOOLTIP_EK_NETTO = "The net purchase price without VAT"
TOOLTIP_VK_BRUTTO = "The gross sales price including VAT"
TOOLTIP_MWST = "The applicable VAT rate"
TOOLTIP_RABATT_MODUS = "Additive: Discounts are summed\nSequential: Discounts are applied one after another (commercial)"
TOOLTIP_RABATTE = "Any number of discounts can be added"


# ==============================================================================
# BARCODE SCANNER (for future features)
# ==============================================================================

BUTTON_BARCODE_SCANNEN = "Scan barcode"
LABEL_EAN_EINGABE = "EAN/Barcode"
HINT_EAN_EINGABE = "e.g. 4012345678901"


# ==============================================================================
# API INTEGRATION (for future features)
# ==============================================================================

BUTTON_ARTIKEL_LADEN = "Load article"
STATUS_LADE_ARTIKEL = "Loading article data..."
FEHLER_ARTIKEL_NICHT_GEFUNDEN = "Article not found"
FEHLER_API_VERBINDUNG = "API connection failed"


# ==============================================================================
# USER SETTINGS (for future features)
# ==============================================================================

MENU_EINSTELLUNGEN = "Settings"
LABEL_SPRACHE = "Language"
LABEL_THEME = "Theme"
BUTTON_SPEICHERN = "Save"
BUTTON_ABBRECHEN = "Cancel"
