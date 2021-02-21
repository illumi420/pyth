import numeral_sys_converter as sysconv


def main_menu():
    print("Zahlenumrechner")
    print("Bitte wählen Sie ....")
    print("(1) Hexadezimalzahl umwandeln.")
    print("(2) Dezimalzahl umwandeln.")
    print("(3) Oktalzahl umwandeln.")
    print("(4) Dualzahl umwandeln.")
    print("(q) Beenden")


main_menu()

wahl = ""
menu = ("1", "2", "3", "4", "q")
while wahl != "q":
    for i in menu:
        wahl = input(f"\nIhre Wahl: ").lower()

      # convert from Hex

        if wahl == "1":
            zahl = input("Bitte Zahl für Umrechnung eingeben: ").upper()
            print("Eingegebene Zahl umrechnen in ...")
            print("(d) Dezimalzahl")
            print("(o) Oktalzahl")
            print("(b) Dualzahl")

            sub_menu = ("d", "o", "b")
            select = input("Ihre Wahl: ").lower()
            for element in sub_menu:
                if select == "d":
                    sysconv.hexToDec(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                elif select == "o":
                    sysconv.hexToOct(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                elif select == "b":
                    sysconv.hexToBin(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                else:
                    print("Fehlerhafte Auswahl versuchen Sie bitte nochmal")

      # convert from Dec

        elif wahl == "2":
            zahl = int(input("Bitte Zahl für Umrechnung eingeben: "))
            print("Eingegebene Zahl umrechnen in ...")
            print("(h) Hexdezimalzahl")
            print("(o) Oktalzahl")
            print("(b) Dualzahl")

            sub_menu = ("h", "o", "b")
            select = input("Ihre Wahl: ").lower()
            for element in sub_menu:
                if select == "h":
                    sysconv.decToHex(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                elif select == "o":
                    sysconv.decToOct(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                elif select == "b":
                    sysconv.decToBin(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                else:
                    print("Fehlerhafte Auswahl versuchen Sie bitte nochmal")
                    break

      # convert from Oct

        elif wahl == "3":
            zahl = int(input("Bitte Zahl für Umrechnung eingeben: "))
            print("Eingegebene Zahl umrechnen in ...")
            print("(d) Dezimalzahl")
            print("(h) Hexdezimalzahl")
            print("(b) Dualzahl")

            sub_menu = ("d", "h", "b")
            select = input("Ihre Wahl: ").lower()
            for element in sub_menu:
                if select == "d":
                    sysconv.octToDec(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                elif select == "h":
                    sysconv.octToHex(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                elif select == "b":
                    sysconv.octToBin(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                else:
                    print("Fehlerhafte Auswahl versuchen Sie bitte nochmal")

      # convert from Bin

        elif wahl == "4":
            zahl = int(input("Bitte Zahl für Umrechnung eingeben: "))
            print("Eingegebene Zahl umrechnen in ...")
            print("(d) Dezimalzahl")
            print("(h) Hexdezimalzahl")
            print("(o) Oktalzahl")

            sub_menu = ("d", "h", "o")
            select = input("Ihre Wahl: ").lower()
            for element in sub_menu:
                if select == "d":
                    sysconv.binToDec(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                elif select == "h":
                    sysconv.binToHex(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                elif select == "o":
                    sysconv.binToOct(zahl)
                    input(f"\nWeiter mit der Eingabe-Taste")
                    print("")
                    main_menu()
                    break
                else:
                    print("Fehlerhafte Auswahl versuchen Sie bitte nochmal")

        elif wahl == "q":
            exit()
        else:
            print("Fehlerhafte Auswahl versuchen Sie bitte nochmal")
