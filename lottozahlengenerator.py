import random as r

# To make sure that no random number is duplicated in the list


def pruefeZahl(liste, zahl):
    if len(liste) == 0:
        return 0
    for i in range(len(liste)):
        if liste[i] == zahl:
            return 1
    return 0
# To sort the list (Badzura recommendation)


"""
def sortierListe(liste):
    n = len(liste)
    i = 0
    j = 1
    while i < n-1:
        while j < n:
            if liste[i-1] > liste[j]:
                temp = liste[j-1]
                liste[j-1] = liste[j]
                liste[j] = temp
            return liste
"""

lotto_zahlen = []
counter = 0
while counter < 6:
    random_zahl = r.randint(1, 49)
    pruef = pruefeZahl(lotto_zahlen, random_zahl)
    if pruef == 0:
        lotto_zahlen.append(random_zahl)
        sorted_liste = sortierListe(lotto_zahlen)
        counter = counter + 1
    lotto_zahlen = sorted(lotto_zahlen, reverse=False)
    print(f"Zahl {counter}:", random_zahl)
print(lotto_zahlen)
print(sorted_liste)
