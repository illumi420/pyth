zahl = int(input("Bitte Zahl eingeben: "))
teiler = int(input("Bitte Teiler eingeben :"))
if teiler > zahl:
    print("Teiler ist größer als die Zahl")
elif zahl % teiler > 0:
    print("Eine Division ohne Rest ist nicht möglich")
else:
    print(
        f"Die Division ist ohne Rest möglich. Das Ergebnis {zahl} / {teiler} lautet:", zahl / teiler)
