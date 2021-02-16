pi = 3.1415
radius = float(input("Bitte Radius der Dose eingeben :"))
hoehe = float(input("Bitte Höhe der Dose eingeben :"))
print(f"Eine Dose mit dem Radius {radius} und der Höhe {hoehe} hat folgende Werte:")
durchmesser = radius * 2
print(f"Durchmesser: {durchmesser}")
umfang = pi * radius * 2
print(f"Umfang: {umfang}")
flaeche = pi * (radius**2)
print(f"Deckelbodenfläche: {flaeche}")
mantelflaeche = hoehe * umfang
print(f"Mantelfläche: {mantelflaeche}")
print(f"Zuschnitt Breite {hoehe} * Länge {umfang}")
fassungs = (flaeche * hoehe) - 0.1 * (flaeche * hoehe)
print(f"Fassungsvermögen: {(fassungs)}")
