import math

print("Von welchem geometriischen Körper wollen Sie das Volumen berechnen")
print("(1) Kreiskegel")
print("(2) Kreiszylinder")
print("(3) Quader")
print("(4) Würfel")
print("(q) Programm verlassen")

list = ("1", "2", "3", "4", "q")
for element in list:
    num = input("Ihre Wahl: ").lower()

    if num == list[0]:
        r = float(input("Bitte Radius eingeben: "))
        # if  r >= 0:
        #   continue
        # else:
        #print("fehlerhafte Eingabe! bitte versuch nochmal")

        h = float(input("Bitte Höhe eingeben: "))
        print(f"Volumen:", (1/3) * math.pi * math.pow(r, 2) * h, "cm\u00b3")

    elif num == list[1]:
        r = float(input("Bitte Radius eingeben: "))
        h = float(input("Bitte Höhe eingeben: "))
        print("Volumen:", math.pi * math.pow(r, 2) * h, "cm\u00b3")

    elif num == list[2]:
        a = float(input("Bitte Breite eingeben: "))
        b = float(input("Bitte Länge eingeben: "))
        c = float(input("bitte Höhe eingeben: "))
        print("Volumen:", a*b*c, "cm\u00b3")

    elif num == list[3]:
        a = float(input("Bitte Seitenlänge eingeben: "))
        print("Volumen:", a**3, "cm\u00b3")

    elif num == list[4]:
        exit()
    else:
        print("Sie habe eine fehlerhafte Auswahl getroffen.")
