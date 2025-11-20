# Margen-Rechner - Quick Start Guide

## 🚀 In 3 Schritten zur laufenden Anwendung

### 1. Flet installieren
```bash
pip install flet
```

### 2. Anwendung starten
```bash
cd app
python main.py
```

### 3. Fertig!
Die WebApp öffnet sich automatisch im Browser.

---

## 📋 Was kann die App?

- **Preise eingeben**: EK netto, VK brutto, MwSt-Satz
- **Rabatte hinzufügen**: Beliebig viele Rabatte (+ Button)
- **Rabatt-Modi**: Addiert oder Nachgelagert (kaufmännisch)
- **Live-Berechnung**: Ergebnisse aktualisieren sich automatisch
- **Übersichtliche Ergebnisse**:
  - VK netto
  - Effektiver EK
  - Gesamtrabatt
  - Rohertrag (€ und %)
  - Ampel-Bewertung (🔴 gelb/grün)

---

## 💡 Beispiel-Berechnung

**Eingabe:**
- EK netto: 100,00 €
- VK brutto: 178,50 €
- MwSt: 19%
- Rabatte: 5%, 10% (nachgelagert)

**Ergebnis:**
- VK netto: 150,00 €
- Effektiver EK: 85,50 € (nach 14,5% Gesamtrabatt)
- Rohertrag: 64,50 € (43,0%)
- Bewertung: 🟢 Gute Marge

---

## 📁 Projekt-Struktur

```
app/
├── main.py              # ← Start hier!
├── core/                # Berechnungslogik
├── ui/                  # User Interface
├── models/              # Datenmodelle
├── services/            # API & Barcode (Stubs)
├── strategien/          # Amazon, eBay (Stubs)
├── config/              # Einstellungen
└── i18n/                # Sprachen (DE/EN)
```

---

## 🔧 Hilfe bei Problemen

**App startet nicht?**
```bash
# Python-Version prüfen (mind. 3.10)
python --version

# Flet neu installieren
pip install --upgrade flet
```

**Import-Fehler?**
```bash
# Sicherstellen dass du im app/ Ordner bist
cd app
python main.py
```

**Port belegt?**
In `main.py` Port ändern:
```python
ft.app(target=main, port=8080)
```

---

## 📚 Weitere Dokumentation

- [INSTALLATION.md](INSTALLATION.md) - Ausführliche Installationsanleitung
- [readme.md](readme.md) - Vollständige Spezifikation
- [CLAUDE.md](CLAUDE.md) - Entwickler-Guidelines
