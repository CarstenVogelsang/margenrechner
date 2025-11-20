"""
Ergebnis-Anzeige

Dieses Modul zeigt die berechneten Ergebnisse an:
- VK netto
- Effektiver EK
- Gesamtrabatt
- Rohertrag (Euro und Prozent)
- Ampel-Status (rot/gelb/grün)
"""

import flet as ft
from typing import Optional, Dict

from . import komponenten as ui
from ..i18n import strings_de as strings
from ..config import settings


class ErgebnisAnzeige(ft.Container):
    """
    Komponente zur Anzeige der Berechnungsergebnisse.

    Zeigt alle berechneten Werte übersichtlich an,
    inklusive farbiger Ampel-Bewertung der Marge.
    """

    def __init__(self):
        """Initialisiert die Ergebnis-Anzeige."""
        super().__init__()

        # Ergebnis-Felder (als Text-Widgets) - größere Fonts
        self.vk_netto_text = ft.Text("—", size=18, weight=ft.FontWeight.BOLD)
        self.effektiver_ek_text = ft.Text("—", size=18, weight=ft.FontWeight.BOLD)
        self.gesamtrabatt_text = ft.Text("—", size=18, weight=ft.FontWeight.BOLD)
        self.rohertrag_euro_text = ft.Text("—", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PRIMARY)
        self.rohertrag_prozent_text = ft.Text("—", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PRIMARY)

        # Ampel-Anzeige - größer und prominenter
        self.ampel_widget = ui.erstelle_ampel_anzeige("rot", groesse=60)
        self.ampel_text = ft.Text(
            "",
            size=18,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.LEFT
        )
        self.ampel_beschreibung = ft.Text(
            "",
            size=14,
            color=ft.Colors.GREY_700,
            text_align=ft.TextAlign.LEFT
        )

        # Layout aufbauen
        self.content = ui.erstelle_card(
            titel=strings.ERGEBNIS_TITEL,
            inhalt=ft.Column(
                controls=[
                    # Berechnete Werte
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_VK_NETTO_BERECHNET,
                        self.vk_netto_text
                    ),
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_EFFEKTIVER_EK,
                        self.effektiver_ek_text
                    ),
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_GESAMTRABATT,
                        self.gesamtrabatt_text
                    ),

                    ui.erstelle_trennlinie(),

                    # Rohertrag (hervorgehoben)
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_ROHERTRAG_EURO,
                        self.rohertrag_euro_text
                    ),
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_ROHERTRAG_PROZENT,
                        self.rohertrag_prozent_text
                    ),

                    ui.erstelle_trennlinie(),

                    # Ampel-Bewertung
                    ft.Text(
                        strings.LABEL_BEWERTUNG,
                        size=16,
                        weight=ft.FontWeight.BOLD
                    ),
                    # Ampel links, Text rechts (vertikal zentriert)
                    ft.Row(
                        controls=[
                            # Ampel-Widget
                            self.ampel_widget,
                            # Text-Bereich (vertikal zentriert, linksbündig)
                            ft.Column(
                                controls=[
                                    self.ampel_text,
                                    self.ampel_beschreibung
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                spacing=5,
                                expand=True
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                spacing=12
            )
        )

    def _erstelle_ergebnis_zeile(self, label: str, wert_widget: ft.Text) -> ft.Row:
        """
        Erstellt eine Ergebnis-Zeile (Label + Wert).

        Args:
            label: Beschriftung
            wert_widget: Text-Widget für den Wert

        Returns:
            Row mit Label und Wert
        """
        # Wert-Widget rechtsbündig ausrichten
        wert_widget.text_align = ft.TextAlign.RIGHT

        return ft.Row(
            controls=[
                ft.Text(
                    label + ":",
                    size=16,
                    width=200
                ),
                ft.Container(
                    content=wert_widget,
                    expand=True,
                    alignment=ft.alignment.center_right
                )
            ],
            spacing=10
        )

    def aktualisiere_ergebnisse(self, ergebnisse: Optional[Dict] = None):
        """
        Aktualisiert die Anzeige mit neuen Berechnungsergebnissen.

        Args:
            ergebnisse: Dictionary mit Berechnungsergebnissen von kalkulation.berechne_komplett()
                       oder None zum Zurücksetzen
        """
        if ergebnisse is None:
            # Zurücksetzen
            self.vk_netto_text.value = "—"
            self.effektiver_ek_text.value = "—"
            self.gesamtrabatt_text.value = "—"
            self.rohertrag_euro_text.value = "—"
            self.rohertrag_prozent_text.value = "—"
            self.ampel_text.value = ""
            self.ampel_beschreibung.value = ""
            self._setze_ampel("rot")
        else:
            # Werte formatieren und anzeigen
            self.vk_netto_text.value = ui.formatiere_euro(ergebnisse['vk_netto'])
            self.effektiver_ek_text.value = ui.formatiere_euro(ergebnisse['effektiver_ek'])
            self.gesamtrabatt_text.value = ui.formatiere_prozent(ergebnisse['gesamtrabatt_prozent'])

            # Rohertrag hervorheben
            rohertrag_euro = ergebnisse['rohertrag_euro']
            rohertrag_prozent = ergebnisse['rohertrag_prozent']

            self.rohertrag_euro_text.value = ui.formatiere_euro(rohertrag_euro)
            self.rohertrag_prozent_text.value = ui.formatiere_prozent(rohertrag_prozent)

            # Farbe des Rohertrags basierend auf Ampel
            ampel_status = ergebnisse['ampel_status']
            if ampel_status == "rot":
                self.rohertrag_euro_text.color = ft.Colors.RED_700
                self.rohertrag_prozent_text.color = ft.Colors.RED_700
            elif ampel_status == "gelb":
                self.rohertrag_euro_text.color = ft.Colors.AMBER_700
                self.rohertrag_prozent_text.color = ft.Colors.AMBER_700
            else:  # grün
                self.rohertrag_euro_text.color = ft.Colors.GREEN_700
                self.rohertrag_prozent_text.color = ft.Colors.GREEN_700

            # Ampel setzen
            self._setze_ampel(ampel_status)

        # UI aktualisieren (nur wenn bereits zur Page hinzugefügt)
        if hasattr(self, 'page') and self.page is not None:
            self.update()

    def _setze_ampel(self, status: str):
        """
        Setzt die Ampel auf den gegebenen Status.

        Args:
            status: Ampel-Status ("rot", "gelb", "grün")
        """
        # Farben
        farben = {
            "rot": ft.Colors.RED,
            "gelb": ft.Colors.AMBER,
            "grün": ft.Colors.GREEN,
            "gruen": ft.Colors.GREEN
        }

        farbe = farben.get(status.lower(), ft.Colors.GREY)

        # Ampel-Widget aktualisieren (größer)
        self.ampel_widget = ui.erstelle_ampel_anzeige(status, groesse=80)

        # Text und Beschreibung setzen
        if status == "rot":
            self.ampel_text.value = strings.AMPEL_ROT_TEXT
            self.ampel_beschreibung.value = strings.AMPEL_ROT_BESCHREIBUNG
            self.ampel_text.color = ft.Colors.RED_700
        elif status == "gelb":
            self.ampel_text.value = strings.AMPEL_GELB_TEXT
            self.ampel_beschreibung.value = strings.AMPEL_GELB_BESCHREIBUNG
            self.ampel_text.color = ft.Colors.AMBER_700
        else:  # grün
            self.ampel_text.value = strings.AMPEL_GRUEN_TEXT
            self.ampel_beschreibung.value = strings.AMPEL_GRUEN_BESCHREIBUNG
            self.ampel_text.color = ft.Colors.GREEN_700

        # Container-Inhalt neu aufbauen (wegen Ampel-Widget)
        self.content = ui.erstelle_card(
            titel=strings.ERGEBNIS_TITEL,
            inhalt=ft.Column(
                controls=[
                    # Berechnete Werte
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_VK_NETTO_BERECHNET,
                        self.vk_netto_text
                    ),
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_EFFEKTIVER_EK,
                        self.effektiver_ek_text
                    ),
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_GESAMTRABATT,
                        self.gesamtrabatt_text
                    ),

                    ui.erstelle_trennlinie(),

                    # Rohertrag (hervorgehoben)
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_ROHERTRAG_EURO,
                        self.rohertrag_euro_text
                    ),
                    self._erstelle_ergebnis_zeile(
                        strings.LABEL_ROHERTRAG_PROZENT,
                        self.rohertrag_prozent_text
                    ),

                    ui.erstelle_trennlinie(),

                    # Ampel-Bewertung
                    ft.Text(
                        strings.LABEL_BEWERTUNG,
                        size=16,
                        weight=ft.FontWeight.BOLD
                    ),
                    # Ampel links, Text rechts (vertikal zentriert)
                    ft.Row(
                        controls=[
                            # Ampel-Widget
                            self.ampel_widget,
                            # Text-Bereich (vertikal zentriert, linksbündig)
                            ft.Column(
                                controls=[
                                    self.ampel_text,
                                    self.ampel_beschreibung
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                spacing=5,
                                expand=True
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                spacing=12
            )
        )
