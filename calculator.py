"""Ein einfacher Taschenrechner mit tkinter."""

import ast
import operator
import tkinter as tk

# Welche Rechenzeichen erlaubt sind
RECHENZEICHEN = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def auswerten(knoten):
    """Rechnet einen geprueften Ausdruck aus (sicherer als eval)."""
    if isinstance(knoten, ast.Constant) and isinstance(knoten.value, (int, float)):
        return knoten.value
    if isinstance(knoten, ast.BinOp) and type(knoten.op) in RECHENZEICHEN:
        links = auswerten(knoten.left)
        rechts = auswerten(knoten.right)
        return RECHENZEICHEN[type(knoten.op)](links, rechts)
    if isinstance(knoten, ast.UnaryOp) and isinstance(knoten.op, (ast.UAdd, ast.USub)):
        wert = auswerten(knoten.operand)
        return wert if isinstance(knoten.op, ast.UAdd) else -wert
    raise ValueError("Nicht erlaubt")

# Farben fuer das Aussehen
HINTERGRUND = "#1e1e2e"
ANZEIGE_FARBE = "#2a2a3c"
TASTE_FARBE = "#15151f"
AKTION_FARBE = "#25406e"
GEDRUECKT_FARBE = "#040404"
TEXT_FARBE = "#c8c8d4"

# Die Tasten, Zeile fuer Zeile
TASTEN = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "<", "="],
]


class Taschenrechner:
    def __init__(self, fenster):
        self.eingabe = ""

        fenster.title("Taschenrechner")
        fenster.configure(bg=HINTERGRUND)
        fenster.resizable(False, False)

        self.anzeige = tk.Label(
            fenster,
            text="0",
            font=("Helvetica", 32),
            bg=ANZEIGE_FARBE,
            fg=TEXT_FARBE,
            anchor="e",
            padx=16,
            pady=24,
        )
        self.anzeige.grid(row=0, column=0, columnspan=4, sticky="we", padx=12, pady=12)

        for zeile, tastenzeile in enumerate(TASTEN, start=1):
            for spalte, taste in enumerate(tastenzeile):
                farbe = AKTION_FARBE if taste in ("=", "C") else TASTE_FARBE
                knopf = tk.Button(
                    fenster,
                    text=taste,
                    font=("Helvetica", 18),
                    bg=farbe,
                    fg=TEXT_FARBE,
                    activebackground=GEDRUECKT_FARBE,
                    activeforeground=TEXT_FARBE,
                    relief="flat",
                    width=4,
                    height=2,
                    command=lambda t=taste: self.druecke(t),
                )
                knopf.grid(row=zeile, column=spalte, padx=6, pady=6, sticky="we")

        # Tastatur kann auch benutzt werden
        fenster.bind("<Key>", self.tastatur)

    def druecke(self, taste):
        """Reagiert auf einen Tastendruck."""
        if taste == "C":
            self.eingabe = ""
        elif taste == "<":
            self.eingabe = self.eingabe[:-1]
        elif taste == "=":
            self.rechne()
            return
        else:
            self.eingabe += taste
        self.zeige(self.eingabe or "0")

    def rechne(self):
        """Berechnet das Ergebnis der Eingabe."""
        try:
            baum = ast.parse(self.eingabe, mode="eval")
            ergebnis = auswerten(baum.body)
            # 6 sieht schoener aus als 6.0
            if isinstance(ergebnis, float) and ergebnis.is_integer():
                ergebnis = int(ergebnis)
            self.eingabe = str(ergebnis)
            self.zeige(self.eingabe)
        except Exception:
            self.eingabe = ""
            self.zeige("Fehler")

    def zeige(self, text):
        self.anzeige.config(text=text)

    def tastatur(self, ereignis):
        if ereignis.char in "0123456789.+-*/()":
            self.druecke(ereignis.char)
        elif ereignis.keysym in ("Return", "equal"):
            self.druecke("=")
        elif ereignis.keysym == "BackSpace":
            self.druecke("<")
        elif ereignis.keysym == "Escape":
            self.druecke("C")


if __name__ == "__main__":
    fenster = tk.Tk()
    Taschenrechner(fenster)
    fenster.mainloop()
