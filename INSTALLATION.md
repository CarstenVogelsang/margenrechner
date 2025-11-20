# Installation und Start-Anleitung

## Voraussetzungen

- Python 3.10 oder höher
- pip (Python Package Manager)

## Installation

### 1. Repository klonen oder herunterladen

```bash
cd margenrechner
```

### 2. Virtuelle Umgebung erstellen (empfohlen)

```bash
# Virtuelle Umgebung erstellen
python -m venv venv

# Virtuelle Umgebung aktivieren
# Auf macOS/Linux:
source venv/bin/activate

# Auf Windows:
venv\Scripts\activate
```

### 3. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

## Anwendung starten

### Als WebApp (Standard)

```bash
cd app
python main.py
```

oder alternativ:

```bash
flet run app/main.py --web
```

Die Anwendung öffnet sich automatisch im Browser.

### Als Desktop-App

In `app/main.py` die letzte Zeile ändern von:
```python
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```
zu:
```python
ft.app(target=main, view=ft.AppView.FLET_APP)
```

Dann starten:
```bash
python app/main.py
```

### Als Web-Server auf bestimmtem Port

In `app/main.py` die letzte Zeile ändern zu:
```python
ft.app(target=main, port=8080)
```

## Projekt-Struktur

```
margenrechner/
├── app/
│   ├── main.py                 # Einstiegspunkt
│   ├── core/
│   │   └── kalkulation.py      # Berechnungslogik
│   ├── ui/
│   │   ├── layout_main.py      # Haupt-Layout
│   │   ├── form_preiseingabe.py
│   │   ├── result_anzeige.py
│   │   └── komponenten.py
│   ├── models/
│   │   ├── artikel.py
│   │   └── user_settings.py
│   ├── services/
│   │   ├── api_service.py
│   │   └── barcode_service.py
│   ├── strategien/
│   │   ├── amazon.py
│   │   └── ebay.py
│   ├── config/
│   │   └── settings.py
│   └── i18n/
│       ├── strings_de.py
│       └── strings_en.py
├── requirements.txt
├── .gitignore
├── CLAUDE.md
└── readme.md
```

## Funktionen (MVP)

- ✅ Eingabe von Einkaufspreis (EK netto)
- ✅ Eingabe von Verkaufspreis (VK brutto)
- ✅ MwSt-Auswahl (19%, 7%, 0%)
- ✅ Dynamische Rabattliste (beliebig viele Rabatte hinzufügen)
- ✅ Rabatt-Modi:
  - Addiert (5% + 10% = 15%)
  - Nachgelagert/kaufmännisch (5% + 10% = 14,5%)
- ✅ Live-Berechnung bei jeder Eingabe
- ✅ Ergebnisse:
  - VK netto
  - Effektiver EK (nach Rabatten)
  - Gesamtrabatt in %
  - Rohertrag in € und %
  - Ampel-Bewertung (rot/gelb/grün)

## Zukünftige Features (vorbereitet, noch nicht implementiert)

- 🔜 produktdaten.org API-Integration
- 🔜 Barcode-Scanner (Kamera & Hardware)
- 🔜 Marketplace-Strategien (Amazon, eBay)
- 🔜 Mehrsprachigkeit (Deutsch/Englisch)
- 🔜 Benutzerkonten & persistente Einstellungen
- 🔜 Android-App Build

## Android-App erstellen (zukünftig)

Wenn die Anwendung stabil läuft, kann sie als Android-App kompiliert werden:

```bash
flet build apk
```

Siehe [Flet Dokumentation](https://flet.dev/docs/guides/python/packaging-app-for-distribution) für Details.

## Fehlerbehebung

### Import-Fehler

Falls Import-Fehler auftreten, stelle sicher dass du im `app/` Verzeichnis bist:
```bash
cd app
python main.py
```

### Flet installiert sich nicht

Prüfe Python-Version:
```bash
python --version  # Sollte >= 3.10 sein
```

Aktualisiere pip:
```bash
pip install --upgrade pip
```

### Port bereits belegt

Wenn Port 8000 (Standard) bereits belegt ist, nutze einen anderen Port:
```python
ft.app(target=main, port=8080)  # In main.py
```

## Entwicklung

### Code-Struktur

- **ALLE Berechnungen** müssen in `core/kalkulation.py` sein
- **UI-Code** nur in `ui/` Modulen
- **Keine Hardcoding** von Werten - alle Konstanten in `config/settings.py`
- **UI-Texte** nur aus `i18n/strings_*.py` laden
- **Deutsche Kommentare** im gesamten Code

### Tests schreiben

```bash
# pytest installieren
pip install pytest

# Tests ausführen (wenn vorhanden)
pytest
```

## Support

Bei Fragen siehe:
- [Flet Dokumentation](https://flet.dev/docs/)
- [readme.md](readme.md) für vollständige Spezifikation
- [CLAUDE.md](CLAUDE.md) für Entwickler-Guidelines
