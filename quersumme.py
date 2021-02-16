sum_of_digits = 0
number = input(
    "Geben Sie die Zahl ein, von wem die Queersumme gebeldit werden soll: ")
for digit in str(number):
    sum_of_digits += int(digit)
print(f"Variante1: Die Quersumme von {number} lautet: {sum_of_digits}")
sum_of_digits = sum(int(digit) for digit in str(number))
print(f"Variante2: Die Quersumme von {number} lautet: {sum_of_digits}")
