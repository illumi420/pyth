# to convert in between hex, oct and bin first the value will be converted to Decimal and then from Decimal to one of the other numeral systems

# [converts from Hexdecimal to Decimal]
def hexToDec(zahl_eingabe):
    dec_ergebnis = list(zahl_eingabe)
    dec = 0
    counter = 0
    for i in reversed(dec_ergebnis):
        if i == 'A':
            i = 10
        elif i == 'B':
            i = 11
        elif i == 'C':
            i = 12
        elif i == 'D':
            i = 13
        elif i == 'E':
            i = 14
        elif i == 'F':
            i = 15
        dec += (16**counter) * int(i)
        counter += 1

    del dec_ergebnis[:]
    dec_ergebnis.append(dec)
    return print(*dec_ergebnis, end=' ')


# [converts from Hexdecimal to Octal]
def hexToOct(zahl_eingabe):
    oct_ergebnis = list(zahl_eingabe)
    oct = 0
    counter = 0
    for i in reversed(oct_ergebnis):
        if i == 'A':
            i = 10
        elif i == 'B':
            i = 11
        elif i == 'C':
            i = 12
        elif i == 'D':
            i = 13
        elif i == 'E':
            i = 14
        elif i == 'F':
            i = 15
        oct += (16**counter) * int(i)
        counter += 1

    del oct_ergebnis[:]
    oct_ergebnis.append(oct)

    if oct < 0:
        oct_ergebnis.append(0)
    elif oct < 8:
        oct_ergebnis.append(oct)
    else:
        decToOct(oct // 8)
        rest = oct % 8
        del oct_ergebnis[:]
        if rest < 8:
            oct_ergebnis.append(rest)
        elif rest > 7:
            oct_ergebnis.append(rest + 3)
    return print(*oct_ergebnis, end=' ')


# [converts from Hexdecimal to Binary]
def hexToBin(zahl_eingabe):
    bin_ergebnis = list(zahl_eingabe)
    bin = 0
    counter = 0
    for i in reversed(bin_ergebnis):
        if i == 'A':
            i = 10
        elif i == 'B':
            i = 11
        elif i == 'C':
            i = 12
        elif i == 'D':
            i = 13
        elif i == 'E':
            i = 14
        elif i == 'F':
            i = 15
        bin += (16**counter) * int(i)
        counter += 1

    del bin_ergebnis[:]
    bin_ergebnis.append(bin)
    decToBin(bin // 2)
    rest = bin % 2
    del bin_ergebnis[:]
    bin_ergebnis.append(rest)
    return print(*bin_ergebnis, end=' ')


# [converts from Decimal to Hexdecimal]


def decToHex(zahl_eingabe):
    hex_ergebnis = []

    if zahl_eingabe < 0:
        hex_ergebnis.append(0)
    elif zahl_eingabe < 10:
        hex_ergebnis.append(zahl_eingabe)
    else:
        decToHex(zahl_eingabe // 16)
        rest = zahl_eingabe % 16
        if rest < 10:
            hex_ergebnis.append(rest)
        elif rest == 10:
            hex_ergebnis.append("A")
        elif rest == 11:
            hex_ergebnis.append("B")
        elif rest == 12:
            hex_ergebnis.append("C")
        elif rest == 13:
            hex_ergebnis.append("D")
        elif rest == 14:
            hex_ergebnis.append("E")
        elif rest == 15:
            hex_ergebnis.append("F")

    # * is to unpack the list(no commas and bracets) end = '' to let element print on the same line
    return print(*hex_ergebnis, end=' ')

# [converts from Decimal to Octal]


def decToOct(zahl_eingabe):
    oct_ergebnis = []

    if zahl_eingabe < 0:
        oct_ergebnis.append(0)
    elif zahl_eingabe < 8:
        oct_ergebnis.append(zahl_eingabe)
    else:
        decToOct(zahl_eingabe // 8)
        rest = zahl_eingabe % 8
        if rest < 8:
            oct_ergebnis.append(rest)
        elif rest > 7:
            oct_ergebnis.append(rest + 3)  # from octal 7 add 3
    return print(*oct_ergebnis, end='')

# [converts from Decimal to Binary]


def decToBin(zahl_eingabe):
    bin_ergebnis = []

    if zahl_eingabe <= 0:
        bin_ergebnis.append(0)
    elif zahl_eingabe == 1:
        bin_ergebnis.append(zahl_eingabe)
    else:
        decToBin(zahl_eingabe // 2)
        rest = zahl_eingabe % 2
        bin_ergebnis.append(rest)

    return print(*bin_ergebnis, end=' ')


# [converts from Octal to Decimal]


def octToDec(zahl_eingabe):
    dec_ergebnis = list(str(zahl_eingabe))
    dec = 0
    counter = 0

    for i in reversed(dec_ergebnis):
        dec += (8**counter) * int(i)
        counter += 1

    del dec_ergebnis[:]
    dec_ergebnis.append(dec)
    return print(*dec_ergebnis, end='')

# [converts from Octal to Hexdecimal]


def octToHex(zahl_eingabe):
    hex_ergebnis = list(str(zahl_eingabe))
    hex = 0
    counter = 0

    for i in reversed(hex_ergebnis):
        hex += (8**counter) * int(i)
        counter += 1

    del hex_ergebnis[:]
    hex_ergebnis.append(hex)

    decToHex(hex // 16)
    rest = hex % 16
    del hex_ergebnis[:]
    if rest < 10:
        hex_ergebnis.append(rest)
    elif rest == 10:
        hex_ergebnis.append("A")
    elif rest == 11:
        hex_ergebnis.append("B")
    elif rest == 12:
        hex_ergebnis.append("C")
    elif rest == 13:
        hex_ergebnis.append("D")
    elif rest == 14:
        hex_ergebnis.append("E")
    elif rest == 15:
        hex_ergebnis.append("F")

    return print(*hex_ergebnis, end=' ')


# [converts from Octal to Binary]


def octToBin(zahl_eingabe):
    bin_ergebnis = list(str(zahl_eingabe))
    bin = 0
    counter = 0

    for i in reversed(bin_ergebnis):
        bin += (8**counter) * int(i)
        counter += 1

    del bin_ergebnis[:]
    bin_ergebnis.append(bin)
    decToBin(bin // 2)
    rest = bin % 2
    del bin_ergebnis[:]
    bin_ergebnis.append(rest)
    return print(*bin_ergebnis, end=' ')


# [converts from Binary to Decimal]


def binToDec(zahl_eingabe):
    # convert  int to string, to break it into list of digits
    dec_ergebnis = list(str(zahl_eingabe))
    dec = 0
    counter = 0

    # reversed to calculate Bin string from right to left
    # go trough the list in reverse and multiply every element(i) by 2^counter, the counter starts from 0 and will be addup 1 for every loop iteration
    for i in reversed(dec_ergebnis):
        dec += (2**counter) * int(i)
        counter += 1

    del dec_ergebnis[:]     # delete old values(zahl_eingabe)
    dec_ergebnis.append(dec)  # add new values(dec sum)
    return print(*dec_ergebnis, end=' ')

# [converts from Binary to Hexdecimal]


def binToHex(zahl_eingabe):
    hex_ergebnis = list(str(zahl_eingabe))
    hex = 0
    counter = 0

    for i in reversed(hex_ergebnis):
        hex += (2**counter) * int(i)
        counter += 1

    del hex_ergebnis[:]
    if hex < 0:
        hex_ergebnis.append(hex)
    elif hex < 10:
        hex_ergebnis.append(hex)
    else:
        decToHex(hex // 16)
        rest = hex % 16
        if rest < 10:
            hex_ergebnis.append(rest)
        elif rest == 10:
            hex_ergebnis.append("A")
        elif rest == 11:
            hex_ergebnis.append("B")
        elif rest == 12:
            hex_ergebnis.append("C")
        elif rest == 13:
            hex_ergebnis.append("D")
        elif rest == 14:
            hex_ergebnis.append("E")
        elif rest == 15:
            hex_ergebnis.append("F")

    return print(*hex_ergebnis, end=' ')


# [converts from Binary to Octal]


def binToOct(zahl_eingabe):
    oct_ergebnis = list(str(zahl_eingabe))
    oct = 0
    counter = 0

    for i in reversed(oct_ergebnis):
        oct += (2**counter) * int(i)
        counter += 1

    del oct_ergebnis[:]
    if oct < 8:
        oct_ergebnis.append(oct)
    elif oct > 7:
        decToOct(oct // 8)
        rest = oct % 8
        if rest < 8:
            oct_ergebnis.append(rest)
        elif rest > 7:
            oct_ergebnis.append(rest + 3)
    return print(*oct_ergebnis, end='')
