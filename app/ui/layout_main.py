"""
Haupt-Layout der Anwendung

Dieses Modul definiert das zweispaltige Hauptlayout:
- Links: Eingabeformular (form_preiseingabe)
- Rechts: Ergebnisanzeige (result_anzeige)

Verwaltet die Kommunikation zwischen Formular und Ergebnisanzeige.
"""

import flet as ft
from typing import Optional

from .form_preiseingabe import PreiseingabeFormular
from .result_anzeige import ErgebnisAnzeige
from ..core.kalkulation import berechne_komplett, RabattModus
from ..i18n import strings_de as strings
from ..config import settings


class HauptLayout:
    """
    Haupt-Layout der Anwendung mit zweispaltiger Ansicht.

    Eigenschaften:
        - Responsive Design (passt sich an Bildschirmgröße an)
        - Live-Berechnung bei jeder Eingabe
        - Zentrale Koordination zwischen Eingabe und Ausgabe
    """

    def __init__(self, page: ft.Page):
        """
        Initialisiert das Haupt-Layout.

        Args:
            page: Flet Page-Objekt
        """
        self.page = page
        self.page.title = strings.APP_TITEL
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = settings.PADDING_STANDARD

        # Formular und Ergebnisanzeige erstellen
        self.formular = PreiseingabeFormular(on_change=self._on_formular_change)
        self.ergebnis = ErgebnisAnzeige()

        # Layout aufbauen
        self._erstelle_layout()

    def _erstelle_layout(self):
        """
        Erstellt das zweispaltige responsive Layout.
        """
        # AppBar (Kopfzeile)
        self.page.appbar = ft.AppBar(
            title=ft.Text(strings.APP_TITEL, size=24, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.PRIMARY,
            color=ft.Colors.WHITE,
            center_title=False,
        )

        # Zweispaltige Ansicht (responsive)
        self.haupt_row = ft.ResponsiveRow(
            controls=[
                # Linke Spalte: Formular
                ft.Container(
                    content=self.formular,
                    col={"sm": 12, "md": 6, "lg": 6},
                    padding=ft.padding.only(right=10)
                ),

                # Rechte Spalte: Ergebnisse
                ft.Container(
                    content=self.ergebnis,
                    col={"sm": 12, "md": 6, "lg": 6},
                    padding=ft.padding.only(left=10)
                ),
            ],
            spacing=settings.SPACING_STANDARD,
            vertical_alignment=ft.CrossAxisAlignment.START
        )

        # Haupt-Container mit Scrolling und maximaler Breite (Boxed Layout)
        content_container = ft.Container(
            content=ft.Column(
                controls=[
                    self.haupt_row
                ],
                scroll=ft.ScrollMode.AUTO,
                spacing=settings.SPACING_STANDARD
            ),
            padding=settings.PADDING_STANDARD,
            expand=True
        )

        # Äußerer Container für Zentrierung mit max_width
        outer_container = ft.Container(
            content=content_container,
            alignment=ft.alignment.top_center,
            expand=True
        )

        # Zur Page hinzufügen
        self.page.add(outer_container)

        # Maximale Breite setzen (responsive: nur auf großen Bildschirmen)
        self.page.on_resize = lambda _: self._update_max_width()
        self._update_max_width()

    def _update_max_width(self):
        """
        Aktualisiert die maximale Breite basierend auf der Fenstergröße.
        Auf großen Bildschirmen: max 1400px, zentriert
        Auf kleinen Bildschirmen: volle Breite
        """
        if self.page.width and self.page.width > 1400:
            # Desktop: Zentriert mit max_width
            self.haupt_row.width = 1400
        else:
            # Mobile/Tablet: Volle Breite
            self.haupt_row.width = None

    def _on_formular_change(self, e):
        """
        Callback der bei jeder Formular-Änderung aufgerufen wird.
        Führt Live-Berechnung durch und aktualisiert Ergebnisse.

        Args:
            e: Flet Event-Objekt
        """
        try:
            # Werte aus Formular holen
            werte = self.formular.hole_werte()

            # Validierung: mindestens EK und VK müssen > 0 sein
            if werte['ek_netto'] <= 0 or werte['vk_brutto'] <= 0:
                # Ergebnisse zurücksetzen
                self.ergebnis.aktualisiere_ergebnisse(None)
                return

            # Rabatt-Modus konvertieren
            modus = RabattModus.ADDIERT if werte['rabatt_modus'] == settings.RABATT_MODUS_ADDIERT else RabattModus.NACHGELAGERT

            # Berechnung durchführen
            ergebnisse = berechne_komplett(
                ek_netto=werte['ek_netto'],
                vk_brutto=werte['vk_brutto'],
                mwst_satz=werte['mwst_satz'],
                rabatte=werte['rabatte'],
                modus=modus
            )

            # Ergebnisse anzeigen
            self.ergebnis.aktualisiere_ergebnisse(ergebnisse)

        except Exception as ex:
            # Bei Fehler: Fehlermeldung loggen und Ergebnisse zurücksetzen
            print(f"Fehler bei Berechnung: {ex}")
            self.ergebnis.aktualisiere_ergebnisse(None)

        # UI aktualisieren
        self.page.update()

    def zeige(self):
        """
        Zeigt das Layout an.
        (Wird nach Initialisierung aufgerufen)
        """
        # Initial-Berechnung durchführen falls Formular bereits Werte hat
        self._on_formular_change(None)
        self.page.update()
