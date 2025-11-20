# Deployment-Anleitung für Margen-Rechner

## Coolify Deployment

### Voraussetzungen
- Coolify-Installation
- Git-Repository mit dem Code

### Deployment-Schritte

1. **Neues Projekt in Coolify erstellen**
   - Git-Repository URL hinzufügen
   - Branch: `main` (oder Ihr bevorzugter Branch)

2. **Build-Einstellungen**
   - Build Pack: **Nixpacks** (wird automatisch erkannt)
   - Die `Procfile` und `nixpacks.toml` werden automatisch verwendet

3. **Umgebungsvariablen** (optional)
   ```
   PORT=8550          # Standard-Port (wird automatisch von Coolify gesetzt)
   HOST=0.0.0.0       # Für externe Erreichbarkeit
   ```

4. **Deployment starten**
   - Coolify baut die Anwendung automatisch mit Nixpacks
   - Der Start-Befehl aus der `Procfile` wird verwendet: `python run.py`

### Port-Konfiguration

Die Anwendung liest den Port aus der Umgebungsvariable `PORT`:
- **Lokal**: Standard-Port 8550
- **Coolify**: Automatisch gesetzter Port (meist 3000 oder 8000)

### Health Check

Die Anwendung läuft als Flet-WebApp und ist nach dem Start sofort erreichbar:
- Health Check URL: `http://your-domain.com/`
- Die Web-UI sollte die Eingabeformulare anzeigen

## Lokale Entwicklung

```bash
# Virtual Environment erstellen
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# oder
.venv\Scripts\activate     # Windows

# Dependencies installieren
pip install -r requirements.txt

# Anwendung starten
python run.py
```

Die Anwendung öffnet sich automatisch im Browser unter `http://localhost:8550`

## Docker (Alternative)

Falls Sie Docker statt Nixpacks verwenden möchten:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8550
ENV HOST=0.0.0.0

EXPOSE 8550

CMD ["python", "run.py"]
```

## Troubleshooting

### Problem: Anwendung startet nicht
- Prüfen Sie die Logs in Coolify
- Stellen Sie sicher, dass `flet>=0.24.0` installiert ist
- Überprüfen Sie, ob alle Dependencies korrekt installiert wurden

### Problem: Port-Konflikt
- Setzen Sie die Umgebungsvariable `PORT` auf einen freien Port
- Coolify setzt diese Variable normalerweise automatisch

### Problem: Anwendung nicht erreichbar
- Stellen Sie sicher, dass `HOST=0.0.0.0` gesetzt ist
- Prüfen Sie die Firewall-Einstellungen in Coolify
