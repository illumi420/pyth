def gleichZahl(zahl):
    erste_digit = (zahl // 100)
    last_2_digits = zahl % 100
    if last_2_digits == 11:
        zahl = 111 * erste_digit
        return zahl


for i in reversed(range(111, 1000, 100)):
    print(gleichZahl(i))
