import random
a = 1
b = 100
usr_input = ""
computer_ans = ""
counter = 0
while usr_input != "r":
    computer_ans = random.randint(a, b)
    usr_input = input(f"{computer_ans}? ")

    if usr_input == "k":
        a = computer_ans + 1
        computer_ans = random.randint(a, b)
        counter += 1

    elif usr_input == "g":
        b = computer_ans - 1
        computer_ans = random.randint(a, b)
        counter += 1
    elif usr_input == "r":
        counter += 1
    else:
        print("Fehlerhafte Eingabe")

print(f'Der Computer hat {counter} Versuche benötig, um die Zahl zu erraten')
