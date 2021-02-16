eingabe_liste = []
for i in range(1, 11):
    eingabe_liste.append(int(input(f"Bitte Zahl {i} eingeben : ")))


def kleinsteEingabe(liste):
    min = liste[0]
    for i in range(1, 10):
        if liste[i] < min:
            min = liste[i]
    return min


def groessteEingabe(liste):
    max = liste[0]
    for i in range(1, 10):
        if liste[i] > max:
            max = liste[i]
    return max


def durchschnitt(liste):
    sum = 0
    count = 0
    for i in liste:
        count += 1
        sum += i
        avg = sum / count

    return avg


print(f"Kleinste eingegebene Zahl:", kleinsteEingabe(eingabe_liste))
print(f"Größte eingegebene Zahl:", groessteEingabe(eingabe_liste))
print("Durchschnitt der eingegeben Zahlen:", durchschnitt(eingabe_liste))
