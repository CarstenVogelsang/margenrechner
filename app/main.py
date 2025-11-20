"""
Margen-Rechner - Haupteinstiegspunkt

Flet WebApp zur Berechnung von Händler-Margen (Rohertrag)
basierend auf Einkaufspreis, Verkaufspreis, Rabatten und MwSt.

Autor: Claude Code
Version: 1.0.0
"""

import flet as ft
from .ui.layout_main import HauptLayout


def main(page: ft.Page):
    """
    Haupt-Einstiegspunkt der Flet-Anwendung.

    Args:
        page: Flet Page-Objekt (wird automatisch übergeben)
    """
    # Haupt-Layout erstellen und anzeigen
    layout = HauptLayout(page)
    layout.zeige()


if __name__ == "__main__":
    # Anwendung starten
    # Als WebApp (Standard)
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)

    # Alternative Startmodi (auskommentiert):
    # ft.app(target=main, view=ft.AppView.FLET_APP)  # Desktop-App
    # ft.app(target=main, port=8080)  # Als Web-Server auf Port 8080
