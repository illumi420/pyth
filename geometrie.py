import math

volumen = 0


def kreiskegelVolumen(radius, hoehe):
    return (1/3) * math.pi * math.pow(radius, 2) * hoehe


def kreiszylinderVolumen(radius, hoehe):
    return math.pi * math.pow(radius, 2) * hoehe


def quaderVolumen(breite, laenge, hoehe):
    return breite * laenge * hoehe


def wuerfelVolumen(seitenlaenge):
    return seitenlaenge**3


print("Von welchem geometrieschen Körper wollen Sie das Volumen berechnen")
print("(1) Kreiskegel")
print("(2) Kreiszylinder")
print("(3) Quader")
print("(4) Würfel")
print("(q) Programm verlassen")

list = ("1", "2", "3", "4", "q")
for element in list:
    num = input("Ihre Wahl: ").lower()
# kreiskegel
    if num == list[0]:
        try:
            r = float(input("Bitte Radius eingeben: "))
            h = float(input("Bitte Höhe eingeben: "))
            volumen = kreiskegelVolumen(r, h)
        except:
            print("Fehlerhafte Eingabe von Radius oder Hoehe")
# kreiszylinder
    elif num == list[1]:
        try:
            r = float(input("Bitte Radius eingeben: "))
            h = float(input("Bitte Höhe eingeben: "))
            volumen = kreiszylinderVolumen(r, h)
        except:
            print("Fehlerhafte Eingabe von Radius oder Hoehe")
# Quader
    elif num == list[2]:
        try:
            a = float(input("Bitte Breite eingeben: "))
            b = float(input("Bitte Länge eingeben: "))
            c = float(input("bitte Höhe eingeben: "))
            volumen = quaderVolumen(a, b, c)
        except:
            print("Fehlerhafte Eingabe von Breite, Länge oder Hoehe")
# Würfel
    elif num == list[3]:
        try:
            a = float(input("Bitte Seitenlänge eingeben: "))
            volumen = wuerfelVolumen(a)
        except:
            print("Fehlerhafte Eingabe von Seitenlänge")

    elif num == list[4]:
        exit()
    else:
        print("Sie haben eine fehlerhafte Auswahl getroffen.")
    if volumen != 0:
        print(f"Volume :", volumen, "cm\u00b3")
