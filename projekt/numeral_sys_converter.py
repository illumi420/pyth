def hexToInt(number_input):
    if number_input == 'A':
        return 10
    elif number_input == 'B':
        return 11
    elif number_input == 'C':
        return 12
    elif number_input == 'D':
        return 13
    elif number_input == 'E':
        return 14
    elif number_input == 'F':
        return 15


def toDec(number_input, numbersystem):
    if numbersystem == "1":
        base = 16
    elif numbersystem == "3":
        base = 8
    elif numbersystem == "4":
        base = 2
    dec = 0
    length = len(number_input) - 1
    exponent = 0
    for i in range(length, -1, -1):
        try:
            zahl = int(number_input[i])
        except:
            zahl = hexToInt(number_input[i])
        dec += base**exponent * zahl
        exponent += 1
    return dec


def intToHex(number_input):
    if number_input == 10:
        return "A"
    elif number_input == 11:
        return "B"
    elif number_input == 12:
        return "C"
    elif number_input == 13:
        return "D"
    elif number_input == 14:
        return "E"
    elif number_input == 15:
        return "F"


def decTo(number_input, resultsystem):
    if resultsystem == "h":
        divisor = 16
    if resultsystem == "o":
        divisor = 8
    if resultsystem == "b":
        divisor = 2
    result = ""
    while number_input != 0:
        if number_input % divisor >= 10:
            rest = intToHex(number_input % divisor)
        else:
            rest = str(number_input % divisor)
        result = rest + result
        number_input = number_input // divisor
    return result
