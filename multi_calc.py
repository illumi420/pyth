import math

print(" ____    ____          __   _    _    ______          __                   ")
print(
    "|_   \  /   _|        [  | / |_ (_) .' ___  |        [  |                  ")
print("  |   \/   |  __   _   | |`| |-'__ / .'   \_|__   _   | |  .---.  __   _   ")
print(
    "  | |\  /| | [  | | |  | | | | [  || |      [  | | |  | | / /'`\][  | | |  ")
print(" _| |_\/_| |_ | \_/ |, | | | |, | |\ `.___.'\| \_/ |, | | | \__.  | \_/ |, ")
print(
    "|_____||_____|'.__.'_/[___]\__/[___]`.____ .''.__.'_/[___]'.___.' '.__.'_/ ")
print()
print()
print("Calculate Volume of a geometric body")
print(" (1) Cone")
print(" (2) Cylinder")
print(" (3) Cuboid")
print(" (4) Cube")
print(" (5) Sphere")
print(" (6) Pyramid")
print()
print("Other Calculations")
print(" (7) Circle")
print(" (8) Tin can")
print(" (9) How much Time in a Month")
print("(10) Temperature")
print("(11) Meter to inch/foot/yard")
print("(12) Your weight on the Moon")
print("(13) Sum of Digits in a number")
print("(14) Factorial")
print("(15) Divisiblity with no Rest")
print("(16) Saving account after 1 year")
print("(17) Commission (bounus for employees of 5 years and above)")
print()
print("(q) leave program")
print()

list = ("1", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "q")
for element in list:
    num = input("select: ").lower()

# Cone
    if num == list[0]:
        r = float(input("Radius: "))
        h = float(input("Height: "))
        if r > 0 and h > 0:
            print(f"Volume:", (1/3) * math.pi * math.pow(r, 2) * h, "cm\u00b3")
        else:
            print("False input Value")

# Cylinder
    elif num == list[1]:
        r = float(input("Radius: "))
        h = float(input("Height: "))
        if r > 0 and h > 0:
            print(f"Volume:", math.pi * math.pow(r, 2) * h, "cm\u00b3")
        else:
            print("False input Value")

# Cuboid
    elif num == list[2]:
        a = float(input("Width: "))
        b = float(input("Length: "))
        c = float(input("Height: "))
        if a > 0 and b > 0 and c > 0:
            print(f"Volume:", a*b*c, "cm\u00b3")
        else:
            print("False input Value")
# Cube
    elif num == list[3]:
        a = float(input("Side Length: "))
        if a > 0:
            print(f"Volume:", a**3, "cm\u00b3")
        else:
            print("False input Value")
# Sphere
    elif num == list[4]:
        r = float(input("Radius: "))
        if r > 0:
            print(f"Volume:", 4/3 * math.pi * math.pow(r, 3), "cm\u00b3")
        else:
            print("False input Value")

# Pyramid
    elif num == list[5]:
        l = float(input("Base Length: "))
        w = float(input("Base Width: "))
        h = float(input("Height: "))
        if l > 0 and w > 0 and h > 0:
            print(f"Volume:", 1/3 * l * w * h, "cm\u00b3")
        else:
            print("False input Value")

# Circle
    elif num == list[6]:
        pi = 3.1415
        r = float(input("Radius: "))
        if r > 0:
            print(f"a Circle with a Radius of {r} has ...")
            print(f"... a Diameter of", 2 * r)
            print(f"... an Area of", r**2 * pi)
            print(f"... an Extent of", r * 2 * pi)
        else:
            print("False input Value")
# Tin Can
    elif num == list[7]:
        pi = 3.1415
        r = float(input("Radius: "))
        h = float(input("Height: "))
        if r <= 0 or h <= 0:
            print("False input Value")
        else:
            print(
                f"A Tin Can with the radius of {r} and the height of {h} has the following values:")
            print(f"... a Diameter of", 2 * r)
            print(f"... an Extent of", r * 2 * pi)
            print(f"... an Area of", r**2 * pi)
            print(f"... an Outer surface of", h * (r * 2 * pi))
            print(f"... a Volume of", (r**2 * pi * h) -
                  0.1 * (r**2 * pi * h), "cm\u00b3")

# Time in a Month
    elif num == list[8]:
        month = input("Which month do you want to calculate Time ")
        days = int(input(f"How many Days are in {month} "))
        if days == 28 or days == 29 or days == 30 or days == 31:
            print(f"{month} has")
            print(24 * days, "Hours")
            print((24 * days) * 60, "Minutes")
            print((24 * days * 60 * 3600)/60, "Seconds")
        else:
            print("False input Value")

# Temperature
    elif num == list[9]:
        celsius = float(input("Degree Celsius "))
        print(f"{int(celsius)}° Celsius in")
        print("Kelvin:", celsius + 273.15)
        print("Fahrenheit:", (celsius * 90/50)+32)

# Meter
    elif num == list[10]:
        distance = float(input("Distance in Meter "))
        if distance > 0:
            print("inch", distance * 39.3700787402)
            print("foot", distance * 3.280839894)
            print("yard", distance * 1.0936133)
        else:
            print("False input Value")

# Weight on Moon
    elif num == list[11]:
        weight = int(input("How much you weight "))
        if weight > 0:
            print(f"on moon you weight {weight * 0.17} kg ")
        else:
            print("False input Value")

# Sum of Digits
    elif num == list[12]:
        sum_of_digits = 0
        number = input(
            "Please give a number in which You want to Calculate its Digits: ")
        sum_of_digits = sum(int(digit) for digit in str(number))
        if sum_of_digits > 0:
            print(f"the Digit sum of {number} is: {sum_of_digits}")
        else:
            print("False input Value")

# Factorial
    elif num == list[13]:
        def factorial(n):

            if n == 0:
                return 1
            else:
                return n * factorial(n-1)

        num_input = int(
            input("which number do you want to get it's factorial? "))
        print(f"The Factorial of {num_input} is", factorial(num_input))

# Divisibility
    elif num == list[14]:
        dividend = int(input("Dividend: "))
        divisor = int(input("Divisor: "))
        if divisor > dividend:
            print("is not divisibl: Divisor is bigger than Dividend")
        elif dividend % divisor > 0:
            print("a division with no Rest is not possible")
        else:
            print(
                f"a division with no Rest is possible. the Result of {dividend} / {divisor} is:", dividend / divisor)

# Savings in 1 year
    elif num == list[15]:
        savings = float(input("Savings on account: "))
        intrest_rate = float(input("how much is the rate of Intrest: % "))
        if savings > 0:
            print(f"your Savings after 1 Year:",
                  (savings * intrest_rate)/100 + savings)
        else:
            print("False input Value")

# Commission
    elif num == list[16]:
        annual_turnover = int(input("annual turnover: "))
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
        else:
            print("False input Value")

    elif num == list[-1]:
        exit()
    else:
        print("False selection.")
