# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project: Margen-Rechner (Margin Calculator)

A Flet-based WebApp for calculating dealer margins (Rohertrag) based on purchase price (EK), sales price (VK), discounts, and VAT. Built entirely in Python using Flet framework, designed to be extensible for future Android deployment.

**Primary Specification**: See [readme.md](readme.md) for complete requirements (in German).

---

## Development Commands

### Running the App
```bash
# Run as web application
flet run app/main.py --web

# Future: Android build (when ready)
flet build apk
```

### Installation
```bash
pip install flet
```

---

## Critical Architecture Rules

### Directory Structure (MUST BE EXACT)

```
/app
  main.py                    # Entry point: flet.app(target=main, view="web")

  /ui                        # All UI components
    layout_main.py           # Main two-column layout
    form_preiseingabe.py     # Price input form with dynamic discount list
    result_anzeige.py        # Results display with traffic light indicator
    komponenten.py           # Reusable UI components

  /core                      # Business logic ONLY
    kalkulation.py           # ALL calculations must be here

  /models                    # Data structures
    artikel.py               # Article/product model
    user_settings.py         # User settings (stub for future)

  /services                  # External integrations
    api_service.py           # produktdaten.org API (stub)
    barcode_service.py       # Barcode scanner (stub)

  /strategien                # Marketplace-specific logic
    amazon.py                # Amazon strategy (stub)
    ebay.py                  # eBay strategy (stub)

  /config
    settings.py              # Configuration constants, API keys

  /i18n
    strings_de.py            # German UI strings
    strings_en.py            # English UI strings (stub)
```

### Module Responsibilities

**STRICT SEPARATION:**
- **`/core/kalkulation.py`**: Contains ALL price/margin calculations. NO calculations in UI code.
- **`/ui/*`**: UI rendering and user interaction only. NO business logic.
- **`/services/*`**: External API calls and integrations.
- **`/models/*`**: Data structures and models only.

---

## Code Standards (Non-Negotiable)

### Language Requirements
- **All comments must be in German**
- **All function names must be in German** (e.g., `berechne_rohertrag()`, not `calculate_margin()`)
- UI text must come from `/i18n/strings_*.py`, never hardcoded

### Python Standards
- PEP8-compliant code
- No HTML/CSS/JavaScript hacks
- Only Flet styling (no external CSS)
- No hardcoded values (prices, thresholds, etc. → use config)
- No unnecessary dependencies

### Documentation
- Very detailed German comments explaining logic
- Function docstrings in German
- Optimized for agent-based development (clear, deterministic structure)

---

## Key Calculation Logic

### Discount Modes (in `/core/kalkulation.py`)

Two modes must be implemented:

1. **Addiert (Additive)**: Discounts sum directly
   ```
   Total discount = discount1 + discount2 + discount3
   ```

2. **Nachgelagert (Commercial/Chain)**: Discounts apply sequentially
   ```
   After discount1: price * (1 - d1)
   After discount2: result * (1 - d2)
   After discount3: result * (1 - d3)
   ```

### Margin Traffic Light (Ampel)

Color coding for margin percentage:
- **Red (Rot)**: < 20%
- **Yellow (Gelb)**: 20–35%
- **Green (Grün)**: > 35%

### Required Calculations
- VK netto (from VK brutto and MwSt)
- Effective EK (after discounts)
- Total effective discount percentage
- Rohertrag (gross profit) in EUR
- Rohertrag as percentage

### Live Calculation
UI must recalculate results on every input change (no "Calculate" button).

---

## UI Architecture

### Layout Structure
- **Two-column responsive layout**:
  - Left: Input form (`form_preiseingabe.py`)
  - Right: Results display (`result_anzeige.py`)
- Material Design styling via Flet components
- Mobile-responsive

### Dynamic Discount List
- "+" button to add discount fields
- Remove button for each discount
- Arbitrary number of discounts supported

---

## Future Features (Stubs Required)

These features are NOT implemented but architecture must be prepared:

### API Integration (`/services/api_service.py`)
```python
async def get_artikel_by_ean(ean: str) -> dict:
    """Platzhalter: später API-Call zu produktdaten.org."""
    return {}
```
- Base URL and API keys in `/config/settings.py`

### Barcode Scanner (`/services/barcode_service.py`)
```python
def on_barcode_input(value: str):
    """Stub für Barcode-Scanner Integration."""
    pass
```

### Marketplace Strategies (`/strategien/`)
- Empty classes: `AmazonStrategie`, `EbayStrategie`
- Structure for marketplace-specific fee calculations

### Internationalization (`/i18n/`)
- `strings_de.py`: Complete German strings
- `strings_en.py`: Placeholder structure for English

---

## Important Implementation Notes

### What to Avoid
- NO backwards-compatibility hacks (unused vars, re-exports, `# removed` comments)
- NO Chatty comments (keep professional and technical)
- NO mixing of business logic in UI code
- NO additional frameworks beyond Flet

### What to Prioritize
- Clear module boundaries
- Deterministic code structure (predictable for agents)
- Extensibility for future features
- Type hints where beneficial

---

## Testing Approach

When implementing tests:
- Test calculation logic in `/core/kalkulation.py` thoroughly
- Test both discount modes (addiert vs. nachgelagert)
- Test edge cases (negative values, zero, very large numbers)
- Verify traffic light thresholds
- Test VAT calculations

---

## Configuration Management

All constants belong in `/config/settings.py`:
- VAT rates (standard: 19%)
- Margin thresholds (red/yellow/green)
- API endpoints and keys
- Default values

NO magic numbers in calculation code.