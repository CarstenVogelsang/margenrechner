# Phasenplanung Margen-Rechner
# Eine produktdaten.org White-Label Anwendung

Diese Markdown-Datei beschreibt die vollständige, priorisierte Entwicklungsplanung des Margen-Rechners als White-Label-Tool innerhalb des produktdaten.org Ökosystems.

## Gesamtpriorisierung (empfohlene Reihenfolge)

1. Impressum
2. FAQ / Hilfe
3. Dark/Light Mode
4. EAN-Suche
5. White-Label Theming
6. Login über produktdaten.org
7. Kalkulation speichern
8. Kalkulation laden
9. Excel-Export
10. Barcode-Scanner 
11. Händler-Defaults 
12. Single Sign-On (SSO) Verbände, Drittfirmen



## Phase 1 – Statische Grundfunktionen & UI-Basis

### 1. Impressumsseite

* Menüpunkt mit *i*-Icon
* Tooltip: „Impressum“
* Route `/impressum`
* Inhalt dynamisch per Theme/JSON/API

### **2. FAQ-Seite**

* Menüpunkt „FAQ“
* Tooltip „FAQ“
* Route `/faq`
* Anzeigen als Accordion
* Erste Inhalte:

  * „Was ist Marge?“
  * „Was bedeutet nachgelagert?“

* Inhalte via API

### 3. Light Mode / Dark Mode

* Umschalter im Menü
* Speicherung zunächst im LocalStorage, später über User-Settings in produktdaten.org
* Wechsel zwischen `ThemeMode.LIGHT` und `ThemeMode.DARK`


## Phase 2 – Artikelsuche (EAN)

### 4. EAN-basierte Artikelsuche (Frontend)

* Eingabefeld „EAN suchen“
* API-Call an produktdaten.org:

  ```
  GET /api/v1/artikel/ean/{ean}
  ```
* Anzeige:

  * Artikelbezeichnung
  * Hersteller
  * Herstellerartikelnummer
  * Optional: Artikelbild
* Keine eigene Datenhaltung

## Phase 3 – White-Label Theming (Branding pro Kunde)


### 5. Dynamisches Theme-System

* Zugriff per Subdomain:

  * `https://duo.produktdaten.org/margenrechner`
* Oder Query-Parameter:

  * `?theme=duo`

### Theming lädt dynamisch:

* Logo
* Primärfarbe / Sekundärfarbe
* Textfarben
* Impressumsdaten
* Optionale kundenspezifische Anpassungen

### Technik:

* Theme JSON Dateien:

  ```
  /themes/duo.json
  /themes/vedes.json
  /themes/evendo.json
  /themes/default.json
  ```
* Alternativ API:

  ```
  GET /api/theme/{key}
  ```
* Dynamische Anpassung der UI-Komponenten

## Phase 4 – Login & Speicherung über produktdaten.org

### 6. Login (ohne Registrierung in der App)

* Weiterleitung zum produktdaten.org Login
* Rückgabe eines JWT Tokens
* Token wird im LocalStorage gespeichert
* Berechtigter Nutzer kann speichern/laden/exportieren

### 7. Kalkulation speichern

* Button „Speichern“ (Save-Icon)
* API-Call:

  ```
  POST /api/margenrechner/kalkulationen
  ```
* Body enthält:

  * EK, VK, Rabatte, MwSt
  * berechnete Werte
  * EAN (falls vorhanden)
  * User-ID (aus Token)

### 8. Kalkulation laden

* Button „Kalkulation laden“ (Load-Icon)
* UI zeigt Liste der gespeicherten Kalkulationen
* API:

  ```
  GET /api/margenrechner/kalkulationen
  ```
* Klick → Werte werden ins UI geladen

---

## Phase 5 – Export

### 9. Excel-Export

* Button „Exportieren“ (Download-Icon)
* API-Endpunkt:

  ```
  GET /api/margenrechner/kalkulationen/export
  ```
* Exportformat `.xlsx`
* Inhalt:

  * Alle gespeicherten Kalkulationen pro User
  * EAN, Bezeichnung, EK, VK, Rabatte, Modus, Marge €, Marge %, Datum

Falls API noch nicht vorhanden: lokaler Export per Flet + openpyxl.

---

## Phase 6 – Optionale Erweiterungen

### 10. Barcode-/QR-Scanner

* Kamera-Scanner (Web)
* Scanner-Modus (Mobile / App)
* Bluetooth-Handscanner (Keyboard-Input)

### 11. Händler-Defaults aus Produktdatenbank

* Rabatte / MwSt / Profile pro Händler
* Automatisches Vorbefüllen

### 12. Single Sign-On für Verbände / Händlergruppen

* SSO mit gruppenspezifischen Rechten




