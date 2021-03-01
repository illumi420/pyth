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
# menu = ("1", "2", "3", "4", "q")
while wahl != "q":
    # for i in menu:
    wahl = input(f"\nIhre Wahl: ").lower()

    if wahl == "1" or wahl == "2" or wahl == "3" or wahl == "4":
        zahl = input("Bitte Zahl für Umrechnung eingeben: ").upper()
        if wahl != "1":
            print("(h) Hexadezimalzahl")
        if wahl != "2":
            print("(d) Dezimalzahl")
        if wahl != "3":
            print("(o) Oktalzahl")
        if wahl != "4":
            print("(b) Dualzahl")
    else:
        if wahl == "q":
            print("End.")
        else:
            print("Fehlerhafte Auswahl versuchen Sie bitte nochmal")

"""  
           # convert from Hex
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
               

      # convert from Dec

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
               

      # convert from Bin

       

         
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
               

                """
