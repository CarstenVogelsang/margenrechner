"""
Margen-Rechner - Starter-Skript

Dieses Skript startet die Flet-Anwendung.
"""

import sys
from pathlib import Path

# Projektverzeichnis zum Python-Pfad hinzufügen
projekt_root = Path(__file__).parent
sys.path.insert(0, str(projekt_root))

import flet as ft
from app.ui.layout_main import HauptLayout


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
    # Anwendung starten als WebApp
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
