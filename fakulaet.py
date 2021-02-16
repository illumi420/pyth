user_input = int(
    input("Von welcher Zahl soll die Facultät ermittelt werden? "))


def fakulaet(zahl):

    if zahl == 0:
        return 1
    else:
        return zahl * fakulaet(zahl-1)


print(f"Die Fakultät von {user_input} ist", fakulaet(user_input))
