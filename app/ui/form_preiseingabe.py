"""
Preiseingabe-Formular

Dieses Modul enthält das Eingabeformular für:
- Einkaufspreis (EK netto)
- Verkaufspreis (VK brutto)
- MwSt-Satz
- Dynamische Rabattliste
- Rabatt-Modus
"""

import flet as ft
from typing import Callable, List

from . import komponenten as ui
from ..i18n import strings_de as strings
from ..config import settings


class PreiseingabeFormular(ft.Container):
    """
    Formular für die Eingabe aller Preis- und Rabattdaten.

    Eigenschaften:
        - Live-Validierung
        - Dynamische Rabattfelder (hinzufügen/entfernen)
        - Callback bei jeder Änderung für Live-Berechnung
    """

    def __init__(self, on_change: Callable):
        """
        Initialisiert das Preiseingabe-Formular.

        Args:
            on_change: Callback-Funktion die bei jeder Änderung aufgerufen wird
        """
        super().__init__()

        self.on_change_callback = on_change
        self.rabatt_felder: List[ft.TextField] = []
        self.rabatt_zeilen: List[ft.Row] = []

        # Hauptfelder erstellen
        self.ek_feld = ui.erstelle_eingabefeld(
            label=strings.LABEL_EK_NETTO,
            hint=strings.HINT_EK_NETTO,
            suffix=strings.PREFIX_EK_NETTO,
            on_change=self._on_input_change,
            breite=settings.EINGABE_BREITE
        )

        self.vk_feld = ui.erstelle_eingabefeld(
            label=strings.LABEL_VK_BRUTTO,
            hint=strings.HINT_VK_BRUTTO,
            suffix=strings.PREFIX_VK_BRUTTO,
            on_change=self._on_input_change,
            breite=settings.EINGABE_BREITE
        )

        self.mwst_dropdown = ui.erstelle_dropdown(
            label=strings.LABEL_MWST,
            optionen=settings.MWST_OPTIONEN,
            wert=str(settings.MWST_STANDARD),
            on_change=self._on_input_change,
            breite=settings.EINGABE_BREITE
        )

        self.rabatt_modus_dropdown = ui.erstelle_dropdown(
            label=strings.LABEL_RABATT_MODUS,
            optionen=settings.RABATT_MODI_OPTIONEN,
            wert=settings.RABATT_MODUS_NACHGELAGERT,
            on_change=self._on_input_change,
            breite=settings.EINGABE_BREITE
        )

        # Container für Rabatt-Felder
        self.rabatt_container = ft.Column(
            controls=[],
            spacing=10,
            tight=True
        )

        # Button zum Hinzufügen von Rabatten
        self.rabatt_hinzufuegen_button = ui.erstelle_button(
            text=strings.BUTTON_RABATT_HINZUFUEGEN,
            on_click=self._rabatt_hinzufuegen,
            icon=ft.Icons.ADD,
            outlined=True
        )

        # Formular-Layout aufbauen
        self.content = ui.erstelle_card(
            titel=strings.FORMULAR_TITEL,
            inhalt=ft.Column(
                controls=[
                    self.ek_feld,
                    self.vk_feld,
                    self.mwst_dropdown,
                    ui.erstelle_trennlinie(),
                    ft.Text(
                        strings.LABEL_RABATTE,
                        size=16,
                        weight=ft.FontWeight.BOLD
                    ),
                    self.rabatt_modus_dropdown,
                    self.rabatt_container,
                    self.rabatt_hinzufuegen_button,
                ],
                spacing=15,
                scroll=ft.ScrollMode.AUTO
            )
        )

        # Initial ein Rabattfeld hinzufügen
        self._rabatt_hinzufuegen(None)

    def _on_input_change(self, e):
        """
        Wird bei jeder Eingabeänderung aufgerufen.
        Ruft den externen Callback auf für Live-Berechnung.
        """
        if self.on_change_callback:
            self.on_change_callback(e)

    def _rabatt_hinzufuegen(self, e):
        """
        Fügt ein neues Rabattfeld hinzu.
        """
        # Maximum erreicht?
        if len(self.rabatt_felder) >= settings.MAX_ANZAHL_RABATTE:
            # TODO: Snackbar/Warnung anzeigen
            print(strings.MAX_RABATTE_ERREICHT)
            return

        # Neues Rabattfeld erstellen
        rabatt_nummer = len(self.rabatt_felder) + 1
        rabatt_feld = ui.erstelle_eingabefeld(
            label=f"Rabatt {rabatt_nummer}",
            hint=strings.HINT_RABATT,
            suffix=strings.SUFFIX_RABATT,
            on_change=self._on_input_change,
            breite=settings.EINGABE_BREITE - 60
        )

        # Entfernen-Button
        entfernen_button = ft.IconButton(
            icon=ft.Icons.DELETE,
            icon_color=ft.Colors.RED_400,
            tooltip=strings.BUTTON_RABATT_ENTFERNEN,
            on_click=lambda e, feld=rabatt_feld: self._rabatt_entfernen(feld)
        )

        # Row mit Feld und Button
        rabatt_zeile = ft.Row(
            controls=[rabatt_feld, entfernen_button],
            spacing=10,
            alignment=ft.MainAxisAlignment.START
        )

        # Zu Listen hinzufügen
        self.rabatt_felder.append(rabatt_feld)
        self.rabatt_zeilen.append(rabatt_zeile)
        self.rabatt_container.controls.append(rabatt_zeile)

        # UI aktualisieren (nur wenn bereits zur Page hinzugefügt)
        if hasattr(self, 'page') and self.page is not None:
            self.update()

    def _rabatt_entfernen(self, feld: ft.TextField):
        """
        Entfernt ein Rabattfeld.

        Args:
            feld: Das zu entfernende TextField
        """
        # Finde den Index
        if feld in self.rabatt_felder:
            index = self.rabatt_felder.index(feld)

            # Aus Listen entfernen
            self.rabatt_felder.pop(index)
            zeile = self.rabatt_zeilen.pop(index)
            self.rabatt_container.controls.remove(zeile)

            # Nummern aktualisieren
            self._rabatt_nummern_aktualisieren()

            # UI aktualisieren (nur wenn bereits zur Page hinzugefügt)
            if hasattr(self, 'page') and self.page is not None:
                self.update()

            # Neuberechnung triggern
            self._on_input_change(None)

    def _rabatt_nummern_aktualisieren(self):
        """
        Aktualisiert die Nummerierung der Rabattfelder nach dem Löschen.
        """
        for i, feld in enumerate(self.rabatt_felder):
            feld.label = f"Rabatt {i + 1}"

    def hole_werte(self) -> dict:
        """
        Holt alle Eingabewerte aus dem Formular.

        Returns:
            Dictionary mit allen Werten:
            {
                'ek_netto': float,
                'vk_brutto': float,
                'mwst_satz': float,
                'rabatte': List[float],
                'rabatt_modus': str
            }
        """
        try:
            # Hauptfelder parsen
            ek_netto = ui.parse_deutsche_zahl(self.ek_feld.value or "0")
            vk_brutto = ui.parse_deutsche_zahl(self.vk_feld.value or "0")
            mwst_satz = float(self.mwst_dropdown.value or settings.MWST_STANDARD)

            # Rabatte sammeln (nur gefüllte Felder)
            rabatte = []
            for feld in self.rabatt_felder:
                if feld.value and feld.value.strip():
                    try:
                        rabatt = ui.parse_deutsche_zahl(feld.value)
                        if 0 <= rabatt <= 100:  # Validierung
                            rabatte.append(rabatt)
                    except ValueError:
                        pass  # Ungültige Rabatte ignorieren

            rabatt_modus = self.rabatt_modus_dropdown.value or settings.RABATT_MODUS_NACHGELAGERT

            return {
                'ek_netto': ek_netto,
                'vk_brutto': vk_brutto,
                'mwst_satz': mwst_satz,
                'rabatte': rabatte,
                'rabatt_modus': rabatt_modus
            }
        except Exception as e:
            print(f"Fehler beim Parsen der Eingaben: {e}")
            # Fallback: leere/ungültige Werte
            return {
                'ek_netto': 0.0,
                'vk_brutto': 0.0,
                'mwst_satz': settings.MWST_STANDARD,
                'rabatte': [],
                'rabatt_modus': settings.RABATT_MODUS_NACHGELAGERT
            }
