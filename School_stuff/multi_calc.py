import math


def computepay(h, r):
    working_hours = 40
    result = working_hours * r
    extra_h = h > working_hours
    if extra_h:
        extra_r = r * 1.5
        extra = (h - working_hours) * extra_r
        result += extra
    return result


def main_menu():
    print(
        " ____    ____          __   _    _    ______          __                   "
    )
    print(
        "|_   \  /   _|        [  | / |_ (_) .' ___  |        [  |                  "
    )
    print(
        "  |   \/   |  __   _   | |`| |-'__ / .'   \_|__   _   | |  .---.  __   _   "
    )
    print(
        "  | |\  /| | [  | | |  | | | | [  || |      [  | | |  | | / /'`\][  | | |  "
    )
    print(
        " _| |_\/_| |_ | \_/ |, | | | |, | |\ `.___.'\| \_/ |, | | | \__.  | \_/ |, "
    )
    print(
        "|_____||_____|'.__.'_/[___]\__/[___]`.____ .''.__.'_/[___]'.___.' '.__.'_/ "
    )
    print()
    print()
    print("Calculate Volume of a geometric body")
    print(" (1) Cone")
    print(" (2) Cylinder")
    print(" (3) Cuboid")
    print(" (4) Cube")
    print(" (5) Sphere")
    print(" (6) Pyramid")
    print(" (7) Circle")
    print(" (8) Tin can")
    print()
    print("Other Calculations")
    print(" (9) How much Time in a Month")
    print("(10) Leap Year")
    print("(11) Temperature")
    print("(12) Meter to inch/foot/yard")
    print("(13) Your weight on the Moon")
    print("(14) Sum of Digits in a number")
    print("(15) Factorial")
    print("(16) Divisiblity with no Rest")
    print()
    print("Economical Calculations")
    print("(17) Saving account after 1 year")
    print("(18) Commission (bounus for employees of 5 years and above)")
    print("(19) Project Profitability and Payback time")
    print("(20) Gross pay")
    print()
    print("(q) leave program")
    print()


main_menu()

list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
        "14", "15", "16", "17", "18", "19", "20", "q")
num = ""
while num != "q":
    for i in list:
        num = input("select: ").lower()

        # Cone
        if num == list[0]:
            print("Cone")
            print("(0) to go back to main menu")
            r = float(input("Radius: "))
            if r == 0:
                main_menu()
                break
            h = float(input("Height: "))
            if h == 0:
                main_menu()
                break
            if r > 0 and h > 0:
                print(f"Volume:", (1 / 3) * math.pi * math.pow(r, 2) * h,
                      "cm\u00b3")
                input("press Enter to continue")
                main_menu()

            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Cylinder
        elif num == list[1]:
            print("Cylinder")
            print("(0) to go back to main menu")
            r = float(input("Radius: "))
            if r == 0:
                main_menu()
                break
            h = float(input("Height: "))
            if h == 0:
                main_menu()
                break
            if r > 0 and h > 0:
                print(f"Volume:", math.pi * math.pow(r, 2) * h, "cm\u00b3")
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Cuboid
        elif num == list[2]:
            print("Cuboid")
            print("(0) to go back to main menu")
            a = float(input("Width: "))
            if a == 0:
                main_menu()
                break
            b = float(input("Length: "))
            if b == 0:
                main_menu()
                break
            c = float(input("Height: "))
            if c == 0:
                main_menu()
                break
            if a > 0 and b > 0 and c > 0:
                print(f"Volume:", a * b * c, "cm\u00b3")
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()
    # Cube
        elif num == list[3]:
            print("Cube")
            print("(0) to go back to main menu")
            a = float(input("Side Length: "))
            if a == 0:
                main_menu()
                break
            if a > 0:
                print(f"Volume:", a**3, "cm\u00b3")
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()
    # Sphere
        elif num == list[4]:
            print("Sphere")
            print("(0) to go back to main menu")
            r = float(input("Radius: "))
            if r == 0:
                main_menu()
                break
            if r > 0:
                print(f"Volume:", 4 / 3 * math.pi * math.pow(r, 3), "cm\u00b3")
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Pyramid
        elif num == list[5]:
            print("Pyramid")
            print("(0) to go back to main menu")
            l = float(input("Base Length: "))
            if l == 0:
                main_menu()
                break
            w = float(input("Base Width: "))
            if w == 0:
                main_menu()
                break
            h = float(input("Height: "))
            if h == 0:
                main_menu()
                break
            if l > 0 and w > 0 and h > 0:
                print(f"Volume:", 1 / 3 * l * w * h, "cm\u00b3")
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Circle
        elif num == list[6]:
            print("Circle")
            print("(0) to go back to main menu")
            pi = 3.1415
            r = float(input("Radius: "))
            if r == 0:
                main_menu()
                break
            if r > 0:
                print(f"a Circle with a Radius of {r} has ...")
                print(f"... a Diameter of", 2 * r)
                print(f"... an Area of", r**2 * pi)
                print(f"... an Extent of", r * 2 * pi)
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()
    # Tin Can
        elif num == list[7]:
            print("Tin Can")
            print("(0) to go back to main menu")
            pi = 3.1415
            r = float(input("Radius: "))
            if r == 0:
                main_menu()
                break
            h = float(input("Height: "))
            if h == 0:
                main_menu()
                break
            if r <= 0 or h <= 0:
                print("False input Value")
                input("press Enter to continue")
                main_menu()
            else:
                print(
                    f"A Tin Can with the radius of {r} and the height of {h} has the following values:"
                )
                print(f"... a Diameter of", 2 * r)
                print(f"... an Extent of", r * 2 * pi)
                print(f"... an Area of", r**2 * pi)
                print(f"... an Outer surface of", h * (r * 2 * pi))
                print(f"... a Volume of",
                      (r**2 * pi * h) - 0.1 * (r**2 * pi * h), "cm\u00b3")
                input("press Enter to continue")
                main_menu()

    # Time in a Month
        elif num == list[8]:
            print("Time in Month")
            print("(0) to go back to main menu")
            month = input("Which month do you want to calculate Time ")
            if month == "0":
                main_menu()
                break
            days = int(input(f"How many Days are in {month} "))
            if days == 0:
                main_menu()
                break
            if days == 28 or days == 29 or days == 30 or days == 31:
                print(f"{month} has")
                print(24 * days, "Hours")
                print((24 * days) * 60, "Minutes")
                print((24 * days * 60 * 3600) / 60, "Seconds")
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Leap Year

        elif num == list[9]:
            print("Leap Year")
            print("(0) to go back to main menu")
            my_year = int(input("Please Input a Year: "))
            if my_year == 0:
                main_menu()
                break

            sentence_to_print_if_leap_year = "is a leap year"
            sentence_to_print_if_not_leap_year = "is not a leap year"

            is_my_year_divisible_by_4 = my_year % 4 == 0
            is_my_year_divisible_by_100 = my_year % 100 == 0
            is_my_year_divisible_by_400 = my_year % 400 == 0

            if is_my_year_divisible_by_4 and is_my_year_divisible_by_100 and is_my_year_divisible_by_400 or is_my_year_divisible_by_4 and not is_my_year_divisible_by_100 and not is_my_year_divisible_by_400:
                print(my_year, sentence_to_print_if_leap_year)

            else:
                print(my_year, sentence_to_print_if_not_leap_year)
                input("press Enter to continue")
                main_menu()

    # Temperature
        elif num == list[10]:
            print("Temperature")
            celsius = float(input("Degree Celsius "))
            print(f"{int(celsius)}° Celsius in")
            print("Kelvin:", celsius + 273.15)
            print("Fahrenheit:", (celsius * 90 / 50) + 32)
            input("press Enter to continue")
            main_menu()

    # Meter
        elif num == list[11]:
            print("Meter")
            print("(0) to go back to main menu")
            distance = float(input("Distance in Meter "))
            if distance == 0:
                main_menu()
                break
            if distance > 0:
                print("inch", distance * 39.3700787402)
                print("foot", distance * 3.280839894)
                print("yard", distance * 1.0936133)
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Weight on Moon
        elif num == list[12]:
            print("Weight on Moon")
            print("(0) to go back to main menu")
            weight = int(input("How much you weight "))
            if weight == 0:
                main_menu()
                break
            if weight > 0:
                print(f"on moon you weight {weight * 0.17} kg ")
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Sum of Digits
        elif num == list[13]:
            print("Sum of Digits")
            print("(0) to go back to main menu")
            sum_of_digits = 0
            number = input(
                "Please give a number in which You want to Calculate its Digits: "
            )
            if weight == "0":
                main_menu()
                break
            sum_of_digits = sum(int(digit) for digit in str(number))
            if sum_of_digits > 0:
                print(f"the Digit sum of {number} is: {sum_of_digits}")
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Factorial
        elif num == list[14]:
            print("Fractorial")
            print("(0) to go back to main menu")

            def factorial(n):

                if n == 0:
                    return 1
                else:
                    return n * factorial(n - 1)

            num_input = int(
                input("which number do you want to get it's factorial? "))
            if num_input == 0:
                main_menu()
                break
            print(f"The Factorial of {num_input} is", factorial(num_input))
            input("press Enter to continue")
            main_menu()

    # Divisibility
        elif num == list[15]:
            print("Divisibility")
            dividend = int(input("Dividend: "))
            divisor = int(input("Divisor: "))
            if divisor > dividend:
                print("is not divisibl: Divisor is bigger than Dividend")
                input("press Enter to continue")
                main_menu()
            elif dividend % divisor > 0:
                print("a division with no Rest is not possible")
                input("press Enter to continue")
                main_menu()
            else:
                print(
                    f"a division with no Rest is possible. the Result of {dividend} / {divisor} is:",
                    dividend / divisor)
                input("press Enter to continue")
                main_menu()

    # Savings in 1 year
        elif num == list[16]:
            print("Savings in 1 year")
            print("(0) to go back to main menu")
            savings = float(input("Savings on account: "))
            if savings == 0:
                main_menu()
                break
            intrest_rate = float(input("how much is the rate of Intrest: % "))
            if intrest_rate == 0:
                main_menu()
                break
            if savings > 0:
                print(f"your Savings after 1 Year:",
                      (savings * intrest_rate) / 100 + savings)
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Commission
        elif num == list[17]:
            print("Commission")
            print("(0) to go back to main menu")
            annual_turnover = int(input("annual turnover: "))
            if annual_turnover == 0:
                main_menu()
                break
            years = int(input("period of years: "))
            etc_commission = annual_turnover * 0.01
            if annual_turnover <= 10000:
                commission = annual_turnover * 0.05
            elif annual_turnover > 10000 and annual_turnover < 20000:
                commission = annual_turnover * 0.15
            elif annual_turnover >= 20000:
                commission = annual_turnover * 0.20
            if years >= 5:
                commission = commission + etc_commission
            if annual_turnover > 0:
                print(commission, "Euro")
                input("press Enter to continue")
                main_menu()
            else:
                print("False input Value")
                input("press Enter to continue")
                main_menu()

    # Project Profitability and Payback time
        elif num == list[18]:
            print("Project Profitability")
            print("(0) to go back to main menu")
            capital_used = int(input("capital: "))
            if capital_used == 0:
                main_menu()
                break
            win_per_year = int(input("Win / Year: "))
            duration_depreciaton = int(
                input("Duration of imputed depreciation: "))
            depreciation = capital_used / duration_depreciaton
            profitability = round(win_per_year * 100 / capital_used, 2)
            payback_time = capital_used / (depreciation + win_per_year)
            print(f"Profitability: {profitability} %")
            year = int(payback_time)
            month = math.ceil(payback_time * 12) % 12
            print(f"Payback in: {year} Years, {month} Months")
            input("press Enter to continue")
            main_menu()

    # Gross pay
        elif num == list[19]:
            print("Gross pay")
            print("(0) to go back to main menu")
            hrs = int(input("Enter Working Hours: "))
            if hrs == 0:
                main_menu()
                break
            rate = float(input("Enter Rate/hour: "))
            p = computepay(hrs, rate)
            print("Pay", p)
            input("press Enter to continue")
            main_menu()

        elif num == list[-1]:
            exit()
        else:
            print("False selection.")
