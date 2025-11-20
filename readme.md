# Flet WebApp **Margen-Rechner**

**Ziel:**
Erstelle eine moderne, responsive und erweiterbare Flet-WebApp namens **Margen-Rechner**.
Die App berechnet Händler-Margen (Rohertrag) auf Basis von EK, VK, Rabatten und MwSt.
Der Code soll **klar, modular, erweiterbar und vollständig in Python (Flet)** sein.
Fokus: *klare Architektur, strikter Modulaufbau, sehr präzise Aufgabenbeschreibung – optimiert für agentisches Arbeiten von Claude.*

---

# 1. KLARE TECHNISCHE VORGABEN

### **Framework:** Flet (Python)

* WebApp via `flet.app(target=main, view="web")`
* Später optional als Android-App kompilierbar

### **Pflichtanforderungen für Claude:**

* sehr klare Datei- & Modultrennung
* Funktionen und Klassen **vollständig deutsch kommentiert**
* berechenbare, deterministische Code-Struktur
* kein unnötiges CSS/JS
* sauberer Python-Code, PEP8-konform
* keine unnötigen Abhängigkeiten

### **Verzeichnisstruktur (muss exakt so umgesetzt werden):**

```
/app
  main.py

  /ui
    layout_main.py
    form_preiseingabe.py
    result_anzeige.py
    komponenten.py

  /core
    kalkulation.py

  /models
    artikel.py
    user_settings.py

  /services
    api_service.py
    barcode_service.py

  /strategien
    amazon.py
    ebay.py

  /config
    settings.py

  /i18n
    strings_de.py
    strings_en.py
```

Claude muss ALLE Dateien erstellen.

---

# 2. MINI-MVP FUNKTIONEN (SOFORT UMSETZEN)

## **2.1 Pflicht-Eingaben**

* Einkaufspreis netto (EK)
* Verkaufspreis brutto (VK brutto)
* MwSt-Satz (Standard 19 %)
* Dynamische Rabattliste:

  * „+ Rabatt hinzufügen“ Button
  * beliebig viele Rabatte
* Moduswahl:

  * **addiert**
  * **nachgelagert (kaufmännisch korrekt)**

## **2.2 Berechnung (verpflichtend implementieren)**

* VK netto
* effektiver EK (nach Rabatten)
* effektiver Gesamtrabatt (%)
* Rohertrag in Euro
* Rohertrag in Prozent
* Ampel (rot/gelb/grün):

  * rot: < 20 %
  * gelb: 20–35 %
  * grün: > 35 %

## **2.3 UI-Anforderungen**

* Material-Design-Anmutung
* mobilfreundlich / responsive
* Zwei Bereiche:

  * links: Eingabeformular
  * rechts: Ergebnisbox
* Live-Berechnung bei jeder Eingabeänderung

---

# 3. ZUKUNFTSFUNKTIONEN (ARCHITEKTUR JETZT VORBEREITEN)

**Diese Funktionen NICHT implementieren — aber alle Module/Strukturen vorbereiten.**

## **3.1 produktdaten.org API Anbindung**

Datei: `/services/api_service.py`

* Funktion anlegen (nur Stub):

```
async def get_artikel_by_ean(ean: str) -> dict:
    """Platzhalter: später API-Call zu produktdaten.org."""
    return {}
```

* Base-URL & Keys in `/config/settings.py` vorbereiten.

## **3.2 Barcode-Scanner (Stub)**

Datei: `/services/barcode_service.py`
Vorbereitung:

* Funktion `def on_barcode_input(value: str)` (Stub)
* UI-Hook im Formular (noch ohne Funktion)

## **3.3 Szenarien (Amazon, eBay etc.)**

Ordner: `/strategien/`

* leere Klassen anlegen:

  * `AmazonStrategie`
  * `EbayStrategie`
* Parameterstruktur per Dictionary

## **3.4 Benutzerkonten / Einstellungen (Stub)**

Datei: `/models/user_settings.py`

* Klasse `UserSettings` mit Beispiel-Properties

## **3.5 Mehrsprachigkeit (vorbereiten)**

Ordner `/i18n/`

* Datei `strings_de.py` → deutsche UI-Texte
* Datei `strings_en.py` → englische Platzhalter

---

# 4. KLARE ERWARTUNG AN DEN CODE (Claude soll exakt liefern)

### Claude muss liefern:

1. **Komplettes Flet-Projekt** (alle Dateien!)
2. **Baumstruktur der Ordner**
3. **Lauffähiges Beispiel**: `flet run main.py --web`
4. **Alle Module vollständig erstellt** (auch Stubs/Funktionskörper)
5. **Saubere Trennung von UI, Logik und Services**
6. **Alle Berechnungen in `/core/kalkulation.py`**
7. **Null Hardcoding** (keine Preise, keine Beispiele)
8. **Kommentare auf Deutsch**, sehr ausführlich

---

# 5. STARTANLEITUNG (Claude muss sie erzeugen)

* Installation von Flet
* Start als WebApp
* Hinweise zum späteren Android-Build

---

# 6. WICHTIGE REGELN (Claude MUSS sie einhalten)

* keine HTML/JS Hacks
* kein CSS außerhalb von Flet-Styles
* keine zusätzlichen Frameworks
* keine Chatty-Kommentare
* nur saubere strukturierte Ausgabe
* Funktionsnamen müssen deutschsprachig sein
* UI-Texte müssen aus Sprachdatei kommen

---

# 7. ABSCHLUSS

Erstelle jetzt das **vollständige Flet-Projekt** für den **Margen-Rechner** exakt nach dieser Spezifikation.


