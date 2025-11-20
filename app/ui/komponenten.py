"""
UI Komponenten - Wiederverwendbare UI-Elemente

Dieses Modul enthält wiederverwendbare Flet-UI-Komponenten,
die in verschiedenen Teilen der Anwendung genutzt werden.
"""

import flet as ft
from typing import Optional, Callable


def erstelle_eingabefeld(
    label: str,
    hint: Optional[str] = None,
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
    wert: str = "",
    on_change: Optional[Callable] = None,
    keyboard_type: ft.KeyboardType = ft.KeyboardType.NUMBER,
    breite: Optional[int] = None
) -> ft.TextField:
    """
    Erstellt ein standardisiertes Eingabefeld.

    Args:
        label: Beschriftung des Feldes
        hint: Platzhalter-Text
        prefix: Präfix (z.B. "€")
        suffix: Suffix (z.B. "%")
        wert: Initialer Wert
        on_change: Callback bei Wertänderung
        keyboard_type: Tastatur-Typ (NUMBER, TEXT, etc.)
        breite: Optionale feste Breite

    Returns:
        Flet TextField Widget
    """
    return ft.TextField(
        label=label,
        hint_text=hint,
        prefix_text=prefix,
        suffix_text=suffix,
        value=wert,
        on_change=on_change,
        keyboard_type=keyboard_type,
        width=breite,
        text_size=16,
        label_style=ft.TextStyle(size=16),
        border_radius=8,
    )


def erstelle_dropdown(
    label: str,
    optionen: list,
    wert: Optional[str] = None,
    on_change: Optional[Callable] = None,
    breite: Optional[int] = None
) -> ft.Dropdown:
    """
    Erstellt ein standardisiertes Dropdown-Menü.

    Args:
        label: Beschriftung des Dropdowns
        optionen: Liste von Optionen (kann Strings oder Dicts mit 'label' und 'value' sein)
        wert: Initial ausgewählter Wert
        on_change: Callback bei Auswahländerung
        breite: Optionale feste Breite

    Returns:
        Flet Dropdown Widget
    """
    # Optionen konvertieren wenn nötig
    dropdown_options = []
    for option in optionen:
        if isinstance(option, dict):
            dropdown_options.append(
                ft.dropdown.Option(key=str(option["value"]), text=option["label"])
            )
        else:
            dropdown_options.append(
                ft.dropdown.Option(key=str(option), text=str(option))
            )

    return ft.Dropdown(
        label=label,
        options=dropdown_options,
        value=wert,
        on_change=on_change,
        width=breite,
        text_size=16,
        label_style=ft.TextStyle(size=16),
        border_radius=8,
    )


def erstelle_button(
    text: str,
    on_click: Optional[Callable] = None,
    icon: Optional[str] = None,
    farbe: Optional[str] = None,
    outlined: bool = False
) -> ft.ElevatedButton | ft.OutlinedButton:
    """
    Erstellt einen standardisierten Button.

    Args:
        text: Button-Text
        on_click: Callback bei Klick
        icon: Optionales Icon (z.B. ft.Icons.ADD)
        farbe: Button-Farbe
        outlined: True für Outlined-Style, False für Elevated-Style

    Returns:
        Flet Button Widget
    """
    button_args = {
        "text": text,
        "on_click": on_click,
        "icon": icon,
    }

    if farbe:
        button_args["bgcolor"] = farbe

    if outlined:
        return ft.OutlinedButton(**button_args)
    else:
        return ft.ElevatedButton(**button_args)


def erstelle_card(
    titel: Optional[str] = None,
    inhalt: Optional[ft.Control] = None,
    padding: int = 24
) -> ft.Card:
    """
    Erstellt eine Material-Design Card.

    Args:
        titel: Optionaler Titel der Card
        inhalt: UI-Inhalt der Card
        padding: Innenabstand (Standard: 24px für mehr Luft)

    Returns:
        Flet Card Widget
    """
    card_inhalt = []

    # Titel hinzufügen falls vorhanden
    if titel:
        card_inhalt.append(
            ft.Text(
                titel,
                size=24,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.PRIMARY
            )
        )
        card_inhalt.append(ft.Divider(height=10))

    # Hauptinhalt hinzufügen
    if inhalt:
        card_inhalt.append(inhalt)

    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=card_inhalt,
                spacing=10,
                tight=True
            ),
            padding=padding,
        ),
        elevation=2,
    )


def erstelle_ampel_anzeige(
    status: str,
    groesse: int = 40
) -> ft.Container:
    """
    Erstellt eine echte Ampel-Anzeige mit 3 Farben (rot/gelb/grün).
    Die aktive Farbe leuchtet hell, die anderen sind gedimmt.
    Optisch gestaltet wie eine echte Ampel mit hellem Gehäuse und dunkelgrauem Rahmen.

    Args:
        status: Ampel-Status ("rot", "gelb", "grün")
        groesse: Größe jeder Ampel-Lampe in Pixeln

    Returns:
        Flet Container mit 3-farbiger Ampel in hellem Gehäuse
    """
    status_lower = status.lower()
    if status_lower == "gruen":
        status_lower = "grün"

    # Intensität: aktive Farbe = 100%, inaktive = 20%
    rot_opacity = 1.0 if status_lower == "rot" else 0.2
    gelb_opacity = 1.0 if status_lower == "gelb" else 0.2
    gruen_opacity = 1.0 if status_lower == "grün" else 0.2

    # Border für aktive Phase (6px dunkelgrau), inaktive Phase (6px Hintergrundfarbe)
    # Damit alle Phasen gleich groß bleiben
    rot_border = ft.border.all(6, ft.Colors.GREY_700) if status_lower == "rot" else ft.border.all(6, ft.Colors.GREY_200)
    gelb_border = ft.border.all(6, ft.Colors.GREY_700) if status_lower == "gelb" else ft.border.all(6, ft.Colors.GREY_200)
    gruen_border = ft.border.all(6, ft.Colors.GREY_700) if status_lower == "grün" else ft.border.all(6, ft.Colors.GREY_200)

    return ft.Container(
        content=ft.Column(
            controls=[
                # Rot (oben) - als Container mit bgcolor statt Icon
                ft.Container(
                    width=groesse,
                    height=groesse,
                    bgcolor=ft.Colors.RED,
                    opacity=rot_opacity,
                    border=rot_border,
                    border_radius=groesse // 2,  # Perfekt rund
                    alignment=ft.alignment.center
                ),
                # Gelb (mitte) - als Container mit bgcolor statt Icon
                ft.Container(
                    width=groesse,
                    height=groesse,
                    bgcolor=ft.Colors.AMBER,
                    opacity=gelb_opacity,
                    border=gelb_border,
                    border_radius=groesse // 2,  # Perfekt rund
                    alignment=ft.alignment.center
                ),
                # Grün (unten) - als Container mit bgcolor statt Icon
                ft.Container(
                    width=groesse,
                    height=groesse,
                    bgcolor=ft.Colors.GREEN,
                    opacity=gruen_opacity,
                    border=gruen_border,
                    border_radius=groesse // 2,  # Perfekt rund
                    alignment=ft.alignment.center
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2
        ),
        # Helles Gehäuse mit dunkelgrauem Rahmen
        bgcolor=ft.Colors.GREY_300,
        border=ft.border.all(6, ft.Colors.GREY_500),
        border_radius=10,
        padding=10,
        alignment=ft.alignment.center
    )


def erstelle_info_zeile(
    label: str,
    wert: str,
    fett: bool = False
) -> ft.Row:
    """
    Erstellt eine zweispaltige Info-Zeile (Label: Wert).

    Args:
        label: Beschriftung (links)
        wert: Wert (rechts)
        fett: True für fette Schrift

    Returns:
        Flet Row Widget
    """
    schriftgewicht = ft.FontWeight.BOLD if fett else ft.FontWeight.NORMAL

    return ft.Row(
        controls=[
            ft.Text(
                label + ":",
                weight=schriftgewicht,
                size=14,
                width=200
            ),
            ft.Text(
                wert,
                weight=schriftgewicht,
                size=14,
                color=ft.Colors.PRIMARY
            ),
        ],
        spacing=10,
    )


def erstelle_trennlinie() -> ft.Divider:
    """
    Erstellt eine horizontale Trennlinie.

    Returns:
        Flet Divider Widget
    """
    return ft.Divider(height=20, thickness=1)


def erstelle_abstand(hoehe: int = 10) -> ft.Container:
    """
    Erstellt einen unsichtbaren Abstandhalter.

    Args:
        hoehe: Höhe des Abstands in Pixeln

    Returns:
        Flet Container (leer, für Spacing)
    """
    return ft.Container(height=hoehe)


def formatiere_euro(betrag: float, dezimalstellen: int = 2) -> str:
    """
    Formatiert einen Betrag als Euro-String.

    Args:
        betrag: Betrag in Euro
        dezimalstellen: Anzahl Dezimalstellen

    Returns:
        Formatierter String (z.B. "123,45 €")
    """
    # Deutsche Formatierung (Komma statt Punkt)
    formatiert = f"{betrag:,.{dezimalstellen}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{formatiert} €"


def formatiere_prozent(wert: float, dezimalstellen: int = 2) -> str:
    """
    Formatiert einen Wert als Prozent-String.

    Args:
        wert: Prozentwert
        dezimalstellen: Anzahl Dezimalstellen

    Returns:
        Formatierter String (z.B. "12,34 %")
    """
    # Deutsche Formatierung
    formatiert = f"{wert:.{dezimalstellen}f}".replace(".", ",")
    return f"{formatiert} %"


def parse_deutsche_zahl(text: str) -> float:
    """
    Parst eine deutsche Zahleneingabe (Komma statt Punkt).

    Args:
        text: Eingabetext (z.B. "123,45")

    Returns:
        Float-Wert

    Raises:
        ValueError: Bei ungültiger Eingabe
    """
    if not text or text.strip() == "":
        return 0.0

    # Punkte (Tausendertrennzeichen) entfernen
    text = text.replace(".", "")
    # Komma durch Punkt ersetzen
    text = text.replace(",", ".")

    try:
        return float(text)
    except ValueError:
        raise ValueError(f"Ungültige Zahleneingabe: {text}")
