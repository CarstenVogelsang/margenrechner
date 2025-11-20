"""
Settings - Globale Konfiguration und Konstanten

Dieses Modul enthält ALLE Konfigurationswerte und Konstanten der Anwendung.
KEINE Magic Numbers im Code - alle Werte hier zentral definieren.
"""

# ==============================================================================
# MEHRWERTSTEUER
# ==============================================================================

MWST_STANDARD = 19.0
"""Standard-Mehrwertsteuersatz in Deutschland (19%)"""

MWST_ERMAESSIGT = 7.0
"""Ermäßigter Mehrwertsteuersatz in Deutschland (7%)"""

MWST_OPTIONEN = [
    {"label": "19% (Standard)", "value": 19.0},
    {"label": "7% (ermäßigt)", "value": 7.0},
    {"label": "0% (steuerfrei)", "value": 0.0},
]
"""Verfügbare MwSt-Optionen für Dropdown"""


# ==============================================================================
# AMPEL-SCHWELLWERTE (Rohertrag-Bewertung)
# ==============================================================================

AMPEL_SCHWELLE_ROT = 20.0
"""Schwelle für rote Ampel: Rohertrag < 20% = rot"""

AMPEL_SCHWELLE_GELB = 35.0
"""Schwelle für gelbe Ampel: Rohertrag 20-35% = gelb, > 35% = grün"""


# ==============================================================================
# AMPEL-FARBEN (Flet-kompatible Farben)
# ==============================================================================

AMPEL_FARBE_ROT = "red"
"""Farbe für rote Ampel (schlechte Marge)"""

AMPEL_FARBE_GELB = "amber"
"""Farbe für gelbe Ampel (mittlere Marge)"""

AMPEL_FARBE_GRUEN = "green"
"""Farbe für grüne Ampel (gute Marge)"""


# ==============================================================================
# RABATT-MODI
# ==============================================================================

RABATT_MODUS_ADDIERT = "addiert"
"""Rabatte werden addiert (5% + 10% = 15%)"""

RABATT_MODUS_NACHGELAGERT = "nachgelagert"
"""Rabatte werden nacheinander angewendet (kaufmännisch korrekt)"""

RABATT_MODI_OPTIONEN = [
    {"label": "Addiert (5% + 10% = 15%)", "value": RABATT_MODUS_ADDIERT},
    {"label": "Nachgelagert (kaufmännisch)", "value": RABATT_MODUS_NACHGELAGERT},
]
"""Verfügbare Rabattmodi für Dropdown"""


# ==============================================================================
# UI-KONFIGURATION
# ==============================================================================

APP_TITEL = "Margen-Rechner"
"""Titel der Anwendung"""

APP_BREITE_MIN = 600
"""Minimale Fensterbreite in Pixeln"""

APP_HOEHE_MIN = 400
"""Minimale Fensterhöhe in Pixeln"""

EINGABE_BREITE = 300
"""Breite der Eingabefelder in Pixeln"""

SPACING_STANDARD = 10
"""Standard-Abstand zwischen UI-Elementen"""

PADDING_STANDARD = 20
"""Standard-Innenabstand in Containern"""


# ==============================================================================
# VALIDIERUNG
# ==============================================================================

MAX_RABATT_PROZENT = 100.0
"""Maximaler Rabatt in Prozent"""

MIN_RABATT_PROZENT = 0.0
"""Minimaler Rabatt in Prozent"""

MAX_ANZAHL_RABATTE = 20
"""Maximale Anzahl von Rabatten die hinzugefügt werden können"""


# ==============================================================================
# API-KONFIGURATION (für zukünftige Features)
# ==============================================================================

API_PRODUKTDATEN_BASE_URL = "https://api.produktdaten.org/v1"
"""Base-URL für produktdaten.org API (Platzhalter)"""

API_PRODUKTDATEN_KEY = None
"""API-Key für produktdaten.org (wird später aus Benutzereinstellungen geladen)"""

API_TIMEOUT_SEKUNDEN = 10
"""Timeout für API-Anfragen in Sekunden"""


# ==============================================================================
# BARCODE-KONFIGURATION (für zukünftige Features)
# ==============================================================================

BARCODE_MIN_LAENGE = 8
"""Minimale Länge eines gültigen Barcodes"""

BARCODE_MAX_LAENGE = 14
"""Maximale Länge eines gültigen Barcodes (EAN-13 + Prüfziffer)"""


# ==============================================================================
# MARKETPLACE-STRATEGIEN (für zukünftige Features)
# ==============================================================================

AMAZON_GEBUEHR_PROZENT = 15.0
"""Durchschnittliche Amazon-Verkaufsgebühr in Prozent (Platzhalter)"""

EBAY_GEBUEHR_PROZENT = 12.5
"""Durchschnittliche eBay-Verkaufsgebühr in Prozent (Platzhalter)"""


# ==============================================================================
# INTERNATIONALISIERUNG
# ==============================================================================

SPRACHE_STANDARD = "de"
"""Standard-Sprache der Anwendung"""

VERFUEGBARE_SPRACHEN = ["de", "en"]
"""Liste verfügbarer Sprachen"""


# ==============================================================================
# FORMATIERUNG
# ==============================================================================

DEZIMALSTELLEN_PROZENT = 2
"""Anzahl Dezimalstellen für Prozentangaben"""

DEZIMALSTELLEN_EURO = 2
"""Anzahl Dezimalstellen für Euro-Beträge"""

WAEHRUNGSSYMBOL = "€"
"""Währungssymbol für Preisangaben"""
