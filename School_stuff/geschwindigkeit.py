toleranz = 3/100
speed = int(input("Bitte gemessene Geschwindigkeit eingeben: "))
strafe = 0
punkte = 0
verbot = 0
above_speed = speed - (speed * toleranz) - 80


if speed > 80:

    if above_speed > 1 and above_speed <= 10:
        strafe = 10

    elif above_speed > 10 and above_speed <= 15:
        strafe = 20

    elif above_speed > 15 and above_speed <= 20:
        strafe = 30

    elif above_speed > 20 and above_speed <= 25:
        strafe = 70

    elif above_speed > 25 and above_speed <= 30:
        strafe = 80

    elif above_speed > 30 and above_speed <= 40:
        strafe = 120

    elif above_speed > 40 and above_speed <= 50:
        strafe = 160

    elif above_speed > 50 and above_speed <= 60:
        strafe = 240

    elif above_speed > 60 and above_speed <= 70:
        strafe = 440
    else:
        strafe = 600

    if above_speed > 20 and above_speed <= 40:
        punkte = 1

    if above_speed > 40 and above_speed <= 70:
        punkte = 2

    if above_speed > 25 and above_speed <= 60:
        verbot = 1

    if above_speed > 60 and above_speed <= 70:
        verbot = 2

    if above_speed >= 70:
        verbot = 3

    print(
        f"Der Verkehrsteilnehmer war um {above_speed} zu schnell unterwegs.")
    print(f"Strafe beträgt {strafe} Euro.")
    if punkte > 0:
        print(f"Es gibt {punkte} Punkte in Flensburg")
    if verbot > 0:
        print(
            f"Es wird ein Fahrverbot in Höhe von {verbot} Monaten ausgesprochen")
else:
    print("Geschwindigkeit war in Ordnung")
