# Versionsplanung Margen-Rechner

# Eine produktdaten.org White-Label Anwendung

Diese Datei beschreibt die vollständige, priorisierte Versionsplanung des Margen-Rechners als White-Label-Tool innerhalb des produktdaten.org Ökosystems.

---

# **Gesamtpriorisierung je Version**

| Version | Inhalt                                                       |
| ------- | ------------------------------------------------------------ |
| **v1**  | Kleine Fixes,Impressum, FAQ, Dark/Light Mode                              |
| **v2**  | EAN-Suche                                                    |
| **v3**  | White-Label Theming (Branding pro Kunde)                     |
| **v4**  | Login über produktdaten.org                                  |
| **v5**  | Kalkulation speichern, laden, Excel-Export                   |
| **v6**  | Barcode-/QR-Scanner, Händler-Defaults                        |
| **v7**  | SSO für Business-Kunden                                      |
| **v8**  | Werbebanner (Partner-/Werbepartner-Modell)                   |


---

# **v1 – Statische Grundfunktionen & UI-Basis**

### **1. Impressumsseite**

* Menüpunkt mit *i*-Icon
* Tooltip: „Impressum“
* Route `/impressum`
* Inhalt dynamisch per Theme/JSON/API

### **2. FAQ-Seite**

* Menüpunkt „FAQ“
* Tooltip „FAQ“
* Route `/faq`
* Accordion-Anzeige
* Inhalte über API (oder JSON):

  * Was ist Marge?
  * Was bedeutet nachgelagert?

### **3. Light Mode / Dark Mode**

* Umschalter im Menü
* Lokale Speicherung (später user settings via API)
* Wechsel zwischen `ThemeMode.LIGHT`/`ThemeMode.DARK`

---

# **v2 – Artikelsuche (EAN)**

### EAN-basierte Artikelsuche

* Eingabefeld „EAN suchen“
* Request an produktdaten.org API:

  ```
  GET /api/v1/artikel/ean/{ean}
  ```
* Anzeige:

  * Artikelbezeichnung
  * Hersteller
  * Herstellerartikelnummer
  * Optional: Produktbild

---

# **v3 – White-Label Theming (Branding pro Kunde)**

### Dynamisches Theme-System

* Zugriff vorzugsweise per Subdomain:

  * `https://duo.produktdaten.org/margenrechner`
* Alternativ per Query-Parameter:

  * `?theme=duo`

### **Zu ladende Theme-Daten:**

* Logo
* Farben
* Impressum des Business-Kunden
* Footer-Branding je nach Partner
* Optional: Compact/Embed-Modus

### **Technische Umsetzung**

* Theme JSON Dateien:

  ```
  /themes/duo.json
  /themes/vedes.json
  /themes/evendo.json
  /themes/default.json
  ```
* Oder API-Endpunkt:

  ```
  GET /api/theme/{key}
  ```

---

# **v4 – Login über produktdaten.org**

### Login / Authentifizierung via produktdaten.org

* Weiterleitung zum produktdaten.org Login-System
* Rückgabe JWT Token
* Speicherung im LocalStorage
* Nur eingeloggte Nutzer dürfen speichern/laden/exportieren

---

# **v5 – Speichern, Laden & Exportieren**

### Kalkulation speichern

* Button „Speichern“ (Save-Icon)
* API:

  ```
  POST /api/margenrechner/kalkulationen
  ```
* Speicherung inkl.:

  * EK
  * VK
  * Rabatte
  * MwSt
  * Rabattmodus
  * EAN
  * berechnete Marge

### Kalkulation laden

* Button „Kalkulation laden“ (Load-Icon)
* UI zeigt gespeicherte Einträge an
* API:

  ```
  GET /api/margenrechner/kalkulationen
  ```

### Excel-Export

* Button „Exportieren“
* API-Endpunkt:

  ```
  GET /api/margenrechner/kalkulationen/export
  ```
* Falls API noch nicht existiert: lokaler Export mittels openpyxl

---

# **v6 – Optional: Erweiterte Funktionen**

### Barcode-/QR-Scanner

* Webkamera-Scanner
* Mobile/Android-Scanner via Flet
* Bluetooth-Handscanner

### Händler-Defaults aus Produktdatenbank

* Standard-Rabatte, MwSt, Konditionen
* Automatisiertes Vorbefüllen

---

# **v7 – Single Sign-On (SSO) für Business-Kunden**

### SSO Integration

* Mitglieder/Kunden von Business-Kunden können sich ohne extra Konto einloggen
* Kostenpflichtiges Feature je Business-Kunden-Instanz

---

# **v8 – Werbebanner-System (White-Label & Partnerbasiert)**

### Einblendbare Werbebanner

* API liefert aktiven Werbebanner je Business-Kunde oder Partner:

  ```
  GET /api/margenrechner/banner/{business_kunde_key}
  ```
* Inhalte des Banners:

  * Bild-URL
  * Link-URL
  * Tracking-Key
  * Laufzeiten / Aktivierungsstatus
* Darstellung als Kopfzeilen- oder Footer-Banner
* Partner kann Werbepartner freischalten
