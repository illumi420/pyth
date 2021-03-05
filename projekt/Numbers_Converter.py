import numeral_sys_converter as sysconv


def main_menu():
    print("Numbers Converter")
    print("Please Choose ....")
    print("(1) Hexadecimal number convert.")
    print("(2) Decimal number convert.")
    print("(3) Octal number convert.")
    print("(4) Binary number convert.")
    print("(q) quit")


main_menu()

choice = ""
while choice != "q":
    choice = input(f"\nYour choice: ").lower()

    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
        num = input("Please insert a number to convert in: ").upper()

        if choice != "1":
            print("(h) Hexadecimal number")
        if choice != "2":
            print("(d) Decimal number")
        if choice != "3":
            print("(o) Octal number")
        if choice != "4":
            print("(b) Binary number")

        sys_select = input("Your choice: ").lower()

        if choice == "2":
            result = sysconv.decTo(int(num), sys_select)
        else:
            if sys_select == "d":
                result = sysconv.toDec(num, choice)
            else:
                mid_result = sysconv.toDec(num, choice)
                result = sysconv.decTo(mid_result, sys_select)
        print("")
        print("result:", result)

        input(f"\nPress Enter to continue")
        print("")
        main_menu()

    else:
        if choice == "q":
            print("End.")
        else:
            print("Failure please choose Item from Menu")
