# Klassen Definition

class Pferd():

    # Konstruktor
    def __init__(self, mein_name, meine_groesse):
        print("Hier wird ein Pferd geboren!")
        print("Das Pferd ist", meine_groesse)

        # Das erste Attribut hinzufügen
        self.groesse = meine_groesse
        self.name = mein_name
        self.geschwindigkeit = "0 km/h"

    def sich_vorstellen(self):
        print("Ich bin", self.name, "und bin", self.groesse, "groß!")

    def laufen(self, geschwindigkeit):
        self.geschwindigkeit = geschwindigkeit
        print("Ich laufe mit", self.geschwindigkeit)

# Instanziierung eines Objekts

# Self müssen wir nie übergeben!
pf1 = Pferd("Beauty", "1,70 m")
pf2 = Pferd("Black", "2,20 m")

pf1.sich_vorstellen()
pf2.sich_vorstellen()

pf1.laufen("30 km/h")