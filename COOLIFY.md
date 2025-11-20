# Coolify Deployment - Quick Start

## 🚀 Schnellstart

### 1. Repository in Coolify hinzufügen
```
Git Repository URL: https://github.com/IHR-USERNAME/margenrechner.git
Branch: main
```

### 2. Build-Pack
**Nixpacks** wird automatisch erkannt durch:
- ✅ `Procfile` vorhanden
- ✅ `nixpacks.toml` vorhanden
- ✅ `requirements.txt` vorhanden

### 3. Start-Befehl (automatisch aus Procfile)
```
web: python run.py
```

### 4. Port-Einstellungen
Die Anwendung nutzt automatisch den von Coolify bereitgestellten Port über die `PORT` Umgebungsvariable.

**Standard-Port (lokal):** 8550
**Coolify-Port:** Wird automatisch gesetzt

### 5. Umgebungsvariablen (optional)
| Variable | Standardwert | Beschreibung |
|----------|--------------|--------------|
| `PORT` | 8550 | Port für die Anwendung (wird von Coolify automatisch gesetzt) |
| `HOST` | 0.0.0.0 | Host-Adresse für externe Erreichbarkeit |

### 6. Deploy!
Nach dem Push zum Git-Repository deployed Coolify automatisch.

## ✅ Deployment-Checklist

- [ ] Git-Repository in Coolify hinzugefügt
- [ ] Branch ausgewählt (main)
- [ ] Build Pack: Nixpacks (automatisch erkannt)
- [ ] Domain konfiguriert (optional)
- [ ] SSL-Zertifikat aktiviert (optional)
- [ ] Deployment gestartet

## 🔍 Logs prüfen

In Coolify unter "Logs" können Sie den Build- und Start-Prozess überwachen:

**Erwartete Log-Ausgaben:**
```
Installing dependencies from requirements.txt...
Successfully installed flet-0.28.3
Starting application on port 3000...
Flet web server running at http://0.0.0.0:3000
```

## 🌐 Zugriff auf die Anwendung

Nach erfolgreichem Deployment:
```
https://ihre-domain.coolify.app
```

Die Web-Oberfläche sollte das Eingabeformular mit folgenden Feldern zeigen:
- Einkaufspreis (EK netto)
- Verkaufspreis (VK brutto)
- MwSt-Satz
- Rabatte (dynamisch hinzufügbar)
- Ergebnisanzeige mit Ampel-Status

## 🐛 Troubleshooting

### Problem: "Port already in use"
**Lösung:** Coolify setzt den Port automatisch. Keine Änderung nötig.

### Problem: "Module 'flet' not found"
**Lösung:** Prüfen Sie, ob `requirements.txt` korrekt commited wurde.

### Problem: "Application not responding"
**Lösung:**
1. Logs in Coolify prüfen
2. Sicherstellen, dass `HOST=0.0.0.0` gesetzt ist
3. Port-Freigabe in Coolify überprüfen

### Problem: Build schlägt fehl
**Lösung:**
1. Prüfen Sie, ob `nixpacks.toml` vorhanden ist
2. Stellen Sie sicher, dass Python 3.13 verfügbar ist
3. Checken Sie die Build-Logs für spezifische Fehler

## 📊 Performance

Die Flet-Anwendung ist eine Single-Page-WebApp:
- **Memory:** ~100-200 MB
- **CPU:** Minimal (nur bei Benutzereingaben)
- **Start-Zeit:** 5-10 Sekunden

## 🔄 Updates deployen

```bash
git add .
git commit -m "Update: Beschreibung der Änderungen"
git push origin main
```

Coolify erkennt den Push automatisch und deployed die neue Version.

## 📝 Weitere Informationen

- Vollständige Deployment-Anleitung: Siehe [DEPLOYMENT.md](DEPLOYMENT.md)
- Projekt-Dokumentation: Siehe [readme.md](readme.md)
- Installations-Anleitung: Siehe [INSTALLATION.md](INSTALLATION.md)
