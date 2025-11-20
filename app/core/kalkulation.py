"""
Kalkulation - Kernmodul für alle Berechnungen des Margen-Rechners

Dieses Modul enthält ALLE Berechnungslogik für:
- Rabattberechnungen (addiert und nachgelagert)
- Margen-/Rohertrag-Berechnungen
- MwSt-Berechnungen
- Ampel-Status-Ermittlung
"""

from typing import List, Dict
from enum import Enum


class RabattModus(Enum):
    """Definiert die beiden Rabatt-Berechnungsmodi"""
    ADDIERT = "addiert"
    NACHGELAGERT = "nachgelagert"


def berechne_vk_netto(vk_brutto: float, mwst_satz: float) -> float:
    """
    Berechnet den Verkaufspreis netto aus dem Bruttopreis.

    Args:
        vk_brutto: Verkaufspreis brutto in Euro
        mwst_satz: Mehrwertsteuersatz in Prozent (z.B. 19.0 für 19%)

    Returns:
        Verkaufspreis netto in Euro
    """
    if vk_brutto < 0:
        raise ValueError("VK brutto darf nicht negativ sein")
    if mwst_satz < 0:
        raise ValueError("MwSt-Satz darf nicht negativ sein")

    return vk_brutto / (1 + mwst_satz / 100)


def berechne_rabatt_addiert(rabatte: List[float]) -> float:
    """
    Berechnet den Gesamtrabatt im Modus ADDIERT.
    Die Rabatte werden einfach summiert.

    Args:
        rabatte: Liste von Rabatten in Prozent (z.B. [5.0, 10.0, 2.5])

    Returns:
        Gesamtrabatt in Prozent
    """
    return sum(rabatte)


def berechne_rabatt_nachgelagert(rabatte: List[float]) -> float:
    """
    Berechnet den effektiven Gesamtrabatt im Modus NACHGELAGERT.
    Die Rabatte werden kaufmännisch korrekt nacheinander angewendet.

    Beispiel: 10% + 5% = 14.5% (nicht 15%)
    - Nach 10%: 90% vom Originalpreis
    - Nach 5% auf 90%: 85.5% vom Originalpreis
    - Effektiver Rabatt: 14.5%

    Args:
        rabatte: Liste von Rabatten in Prozent (z.B. [10.0, 5.0])

    Returns:
        Effektiver Gesamtrabatt in Prozent
    """
    # Startwert: 100% (kein Rabatt)
    verbleibender_prozentsatz = 100.0

    # Jeden Rabatt nacheinander anwenden
    for rabatt in rabatte:
        if rabatt < 0 or rabatt > 100:
            raise ValueError(f"Rabatt {rabatt}% liegt außerhalb des gültigen Bereichs (0-100)")
        verbleibender_prozentsatz *= (1 - rabatt / 100)

    # Effektiver Rabatt = 100% - verbleibender Prozentsatz
    effektiver_rabatt = 100.0 - verbleibender_prozentsatz
    return effektiver_rabatt


def berechne_effektiven_ek(ek_netto: float, rabatte: List[float], modus: RabattModus) -> float:
    """
    Berechnet den effektiven Einkaufspreis nach Anwendung aller Rabatte.

    Args:
        ek_netto: Einkaufspreis netto in Euro
        rabatte: Liste von Rabatten in Prozent
        modus: Rabatt-Berechnungsmodus (ADDIERT oder NACHGELAGERT)

    Returns:
        Effektiver Einkaufspreis nach Rabatten in Euro
    """
    if ek_netto < 0:
        raise ValueError("EK netto darf nicht negativ sein")

    # Gesamtrabatt berechnen je nach Modus
    if modus == RabattModus.ADDIERT:
        gesamtrabatt = berechne_rabatt_addiert(rabatte)
    else:  # NACHGELAGERT
        gesamtrabatt = berechne_rabatt_nachgelagert(rabatte)

    # Effektiven EK berechnen
    effektiver_ek = ek_netto * (1 - gesamtrabatt / 100)
    return effektiver_ek


def berechne_rohertrag_euro(vk_netto: float, effektiver_ek: float) -> float:
    """
    Berechnet den Rohertrag (Bruttomarge) in Euro.

    Args:
        vk_netto: Verkaufspreis netto in Euro
        effektiver_ek: Effektiver Einkaufspreis in Euro

    Returns:
        Rohertrag in Euro
    """
    return vk_netto - effektiver_ek


def berechne_rohertrag_prozent(rohertrag_euro: float, vk_netto: float) -> float:
    """
    Berechnet den Rohertrag als Prozentsatz vom VK netto.

    Args:
        rohertrag_euro: Rohertrag in Euro
        vk_netto: Verkaufspreis netto in Euro

    Returns:
        Rohertrag in Prozent (bezogen auf VK netto)
    """
    if vk_netto == 0:
        return 0.0

    return (rohertrag_euro / vk_netto) * 100


def ermittle_ampel_status(rohertrag_prozent: float) -> str:
    """
    Ermittelt den Ampel-Status (Farbcode) basierend auf dem Rohertrag.

    Schwellwerte:
    - Rot: < 20%
    - Gelb: 20-35%
    - Grün: > 35%

    Args:
        rohertrag_prozent: Rohertrag in Prozent

    Returns:
        Ampel-Status: "rot", "gelb" oder "grün"
    """
    if rohertrag_prozent < 20:
        return "rot"
    elif rohertrag_prozent <= 35:
        return "gelb"
    else:
        return "grün"


def berechne_komplett(
    ek_netto: float,
    vk_brutto: float,
    mwst_satz: float,
    rabatte: List[float],
    modus: RabattModus
) -> Dict[str, float | str]:
    """
    Führt alle Berechnungen durch und liefert ein komplettes Ergebnis-Dictionary.

    Diese Funktion ist die Hauptschnittstelle für die UI-Komponenten.

    Args:
        ek_netto: Einkaufspreis netto in Euro
        vk_brutto: Verkaufspreis brutto in Euro
        mwst_satz: Mehrwertsteuersatz in Prozent
        rabatte: Liste von Rabatten in Prozent
        modus: Rabatt-Berechnungsmodus

    Returns:
        Dictionary mit allen Berechnungsergebnissen:
        {
            'vk_netto': float,
            'effektiver_ek': float,
            'gesamtrabatt_prozent': float,
            'rohertrag_euro': float,
            'rohertrag_prozent': float,
            'ampel_status': str
        }
    """
    # VK netto berechnen
    vk_netto = berechne_vk_netto(vk_brutto, mwst_satz)

    # Gesamtrabatt berechnen
    if modus == RabattModus.ADDIERT:
        gesamtrabatt = berechne_rabatt_addiert(rabatte)
    else:
        gesamtrabatt = berechne_rabatt_nachgelagert(rabatte)

    # Effektiven EK berechnen
    effektiver_ek = berechne_effektiven_ek(ek_netto, rabatte, modus)

    # Rohertrag in Euro berechnen
    rohertrag_euro = berechne_rohertrag_euro(vk_netto, effektiver_ek)

    # Rohertrag in Prozent berechnen
    rohertrag_prozent = berechne_rohertrag_prozent(rohertrag_euro, vk_netto)

    # Ampel-Status ermitteln
    ampel_status = ermittle_ampel_status(rohertrag_prozent)

    return {
        'vk_netto': vk_netto,
        'effektiver_ek': effektiver_ek,
        'gesamtrabatt_prozent': gesamtrabatt,
        'rohertrag_euro': rohertrag_euro,
        'rohertrag_prozent': rohertrag_prozent,
        'ampel_status': ampel_status
    }
