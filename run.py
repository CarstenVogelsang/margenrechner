"""
Margen-Rechner - Starter-Skript

Dieses Skript startet die Flet-Anwendung.
Unterstützt lokale Entwicklung und Produktions-Deployment.
"""

import sys
import os
from pathlib import Path

# Projektverzeichnis zum Python-Pfad hinzufügen
projekt_root = Path(__file__).parent
sys.path.insert(0, str(projekt_root))

import flet as ft
from flet.fastapi import app as flet_fastapi
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


# FastAPI-App für Production (Uvicorn)
app = flet_fastapi(session_handler=main)

if __name__ == "__main__":
    # Port aus Umgebungsvariable lesen (für Coolify/Cloud-Deployment)
    port = int(os.environ.get("PORT", 8550))

    # Host-Adresse (0.0.0.0 für externe Erreichbarkeit im Deployment)
    host = os.environ.get("HOST", "0.0.0.0")

    # Erkenne Umgebung: Produktions-Deployment oder lokale Entwicklung
    # Wenn PORT gesetzt ist, laufen wir im Deployment (Coolify/Cloud)
    is_production = "PORT" in os.environ

    if is_production:
        # Produktions-Deployment: Uvicorn verwendet die FastAPI-App automatisch
        print(f"🚀 Starting Flet with Uvicorn in PRODUCTION mode on {host}:{port}")
        import uvicorn
        uvicorn.run(app, host=host, port=port)
    else:
        # Lokale Entwicklung: Browser öffnet sich automatisch
        print(f"🔧 Starting Flet in DEVELOPMENT mode (Web Browser) on {host}:{port}")
        ft.app(
            target=main,
            view=ft.AppView.WEB_BROWSER,
            port=port,
            host=host
        )
