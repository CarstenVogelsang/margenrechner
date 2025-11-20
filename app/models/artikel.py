"""
Artikel - Datenmodell für Produkte/Artikel

Dieses Modul definiert die Datenstruktur für Artikel,
die später z.B. via API geladen werden können.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Artikel:
    """
    Datenmodell für einen Artikel/Produkt.

    Wird später verwendet für:
    - API-Integration (produktdaten.org)
    - Barcode-Scanner-Integration
    - Artikel-Datenbank
    """

    ean: Optional[str] = None
    """EAN/GTIN Barcode (z.B. 4012345678901)"""

    name: Optional[str] = None
    """Produktname/Bezeichnung"""

    beschreibung: Optional[str] = None
    """Produktbeschreibung"""

    kategorie: Optional[str] = None
    """Produktkategorie"""

    hersteller: Optional[str] = None
    """Hersteller/Marke"""

    ek_netto: Optional[float] = None
    """Einkaufspreis netto in Euro"""

    uvp_brutto: Optional[float] = None
    """Unverbindliche Preisempfehlung brutto in Euro"""

    mwst_satz: float = 19.0
    """Mehrwertsteuersatz in Prozent (Standard: 19%)"""

    def __str__(self) -> str:
        """String-Repräsentation des Artikels"""
        if self.name:
            return f"Artikel({self.ean or 'N/A'}, {self.name})"
        return f"Artikel({self.ean or 'Leer'})"

    def ist_vollstaendig(self) -> bool:
        """
        Prüft, ob alle wichtigen Felder ausgefüllt sind.

        Returns:
            True wenn EAN, Name und EK vorhanden sind
        """
        return all([
            self.ean is not None,
            self.name is not None,
            self.ek_netto is not None
        ])
