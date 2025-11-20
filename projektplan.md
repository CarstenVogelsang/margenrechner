# Versionsplanung Margen-Rechner

# Eine produktdaten.org White-Label Anwendung

Diese Datei beschreibt die vollständige, priorisierte Versionsplanung des Margen-Rechners als White-Label-Tool innerhalb des produktdaten.org Ökosystems.

---

# **Gesamtpriorisierung je Version**

| Version | Inhalt                                                       |
| ------- | ------------------------------------------------------------ |
| **v1**  | Impressum, FAQ, Dark/Light Mode                              |
| **v2**  | EAN-Suche                                                    |
| **v3**  | White-Label Theming (Branding pro Kunde)                     |
| **v4**  | Login über produktdaten.org                                  |
| **v5**  | Kalkulation speichern, laden, Excel-Export                   |
| **v6**  | Barcode-/QR-Scanner, Händler-Defaults                        |
| **v7**  | SSO für Business-Kunden                                      |
| **v8**  | Werbebanner (Partner-/Werbepartner-Modell)                   |
| **v9**  | Monetarisierungsmodell, Stripe-Abos, Rollen & Berechtigungen |

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

### **4. EAN-basierte Artikelsuche**

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

### **5. Dynamisches Theme-System**

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

### **6. Login / Auth**

* Weiterleitung zum produktdaten.org Login-System
* Rückgabe JWT Token
* Speicherung im LocalStorage
* Nur eingeloggte Nutzer dürfen speichern/laden/exportieren

---

# **v5 – Speichern, Laden & Exportieren**

### **7. Kalkulation speichern**

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

### **8. Kalkulation laden**

* Button „Kalkulation laden“ (Load-Icon)
* UI zeigt gespeicherte Einträge an
* API:

  ```
  GET /api/margenrechner/kalkulationen
  ```

### **9. Excel-Export**

* Button „Exportieren“
* API-Endpunkt:

  ```
  GET /api/margenrechner/kalkulationen/export
  ```
* Falls API noch nicht existiert: lokaler Export mittels openpyxl

---

# **v6 – Optional: Erweiterte Funktionen**

### **10. Barcode-/QR-Scanner**

* Webkamera-Scanner
* Mobile/Android-Scanner via Flet
* Bluetooth-Handscanner

### **11. Händler-Defaults aus Produktdatenbank**

* Standard-Rabatte, MwSt, Konditionen
* Automatisiertes Vorbefüllen

---

# **v7 – Single Sign-On (SSO) für Business-Kunden**

### **12. SSO Integration**

* Mitglieder/Kunden von Business-Kunden können sich ohne extra Konto einloggen
* Kostenpflichtiges Feature je Business-Kunden-Instanz

---

# **v8 – Werbebanner-System (White-Label & Partnerbasiert)**

### **13. Einblendbare Werbebanner**

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

---

# **v9 – Rollenmodell & Monetarisierungsmodell (Stripe Abo)**

## **Rollenmodell im produktdaten.org Ökosystem**

### **1. Betreiber (pdo – produktdaten.org)**

* Eigentümer der Plattform und der Tools
* Default-Partner, wenn kein anderer Partner definiert ist
* Verantwortlich für Abrechnung (Stripe)

### **2. Partner (z. B. e-vendo)**

* Wird im Footer angezeigt („präsentiert von e-vendo“)
* Kann Business-Kunden betreuen und Lizenzen weitergeben
* Partner kann Werbebanner für Business-Kunden aktivieren
* Partner ist selbst ebenfalls Business-Kunde (mit eigener Instanz)

### **3. Business-Kunden (duo, Verbände, Unternehmen)**

* Buchen eine instanzbasierte White-Label-Version der App
* 1 Business-Kunde = 1 kostenpflichtige Instanz
* Können Tool auf ihrer Website einbetten oder verlinken
* Nutzen Partner als Abwickler und Hauptkontakt
* Optional: SSO für ihre eigenen Endkunden/Mitglieder

### **4. Endkunden (Händler, Filialen, Mitarbeiter)**

* Nutzen die App im Browser
* Wenn sie Kunde eines Business-Kunden sind → SSO möglich

### **5. Werbepartner**

* Werben innerhalb des Margen-Rechners
* Freischaltung durch Partner
* Einnahmen fließen an Betreiber (pdo)

---

## **Monetarisierbare Funktionen über Stripe**

| Feature                           | Beschreibung                                      | Abrechnung               |
| --------------------------------- | ------------------------------------------------- | ------------------------ |
| **Business-Kunden-Instanz**       | White-Label-Version für einen Verband / Firma     | Monatliche Grundgebühr   |
| **Partner-Abo**                   | Partner darf Weitergabe + Branding vornehmen      | Monatliche Partnergebühr |
| **SSO Add-on**                    | Single Sign-On für Mitglieder des Business-Kunden | Aufpreis pro BK-Instanz  |
| **Werbebanner-Paket**             | Aktivierbare Bannerflächen                        | Paketpreis oder CPM      |
| **Premium API Nutzung**           | Erweiterter Datenzugriff via produktdaten.org     | API-Tarife               |
| **Speicherung von Kalkulationen** | Cloud-Speicher für User                           | Optionales Add-on        |

---

Diese Versionsplanung stellt die vollständige technische, organisatorische und geschäftliche Roadmap des Margen-Rechners für das produktdaten.org Ökosystem dar.
