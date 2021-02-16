user_input = int(input("Bitte Zahl eingeben :"))


def zero(zahl):
    last_2_digits = zahl % 100

    if user_input > 100:
        zahl = zahl - last_2_digits
        return zahl
    elif user_input < 0:
        zahl = zahl - last_2_digits + 100
        return zahl


print("Ausgabe ist :", zero(user_input))
