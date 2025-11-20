"""
UserSettings - Datenmodell für Benutzereinstellungen

Dieses Modul definiert die Datenstruktur für benutzerspezifische Einstellungen.
Aktuell als Stub für zukünftige Erweiterungen (Benutzerkonten, persistente Settings).
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class UserSettings:
    """
    Datenmodell für Benutzereinstellungen.

    Vorbereitet für zukünftige Features:
    - Benutzerkonten
    - Persistente Einstellungen
    - Benutzerdefinierte Standardwerte
    - Theme-Präferenzen
    """

    sprache: str = "de"
    """Bevorzugte Sprache (de, en)"""

    standard_mwst_satz: float = 19.0
    """Standard-Mehrwertsteuersatz in Prozent"""

    standard_rabatt_modus: str = "nachgelagert"
    """Standard-Rabattmodus (addiert, nachgelagert)"""

    ampel_schwelle_rot: float = 20.0
    """Schwellwert für rote Ampel in Prozent (< Wert = rot)"""

    ampel_schwelle_gelb: float = 35.0
    """Schwellwert für gelbe Ampel in Prozent (<= Wert = gelb, > Wert = grün)"""

    theme: str = "light"
    """UI-Theme (light, dark) - für zukünftige Implementierung"""

    benutzername: Optional[str] = None
    """Benutzername (für zukünftige Multi-User-Unterstützung)"""

    email: Optional[str] = None
    """E-Mail-Adresse (für zukünftige Account-Funktionen)"""

    api_key_produktdaten: Optional[str] = None
    """API-Key für produktdaten.org (benutzerspezifisch)"""

    def __str__(self) -> str:
        """String-Repräsentation der Einstellungen"""
        return f"UserSettings(Sprache={self.sprache}, MwSt={self.standard_mwst_satz}%)"
